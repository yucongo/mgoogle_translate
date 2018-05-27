#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
baidu fanyi, token diy

sign_text_js.js
sign.js from
https://www.devtool.top/article/42/
http://blog.csdn.net/m0_37953479/article/details/78929281

sign_text_js.js ==js2py==>sign_text_js.py
sign = sign_text_js.hash(text, GTK)

https://www.jianshu.com/p/38a65d8d3e80
	fetch cookie first

resp = requests.get(, headers=HEADERS)
TOKEN = re.findall(r"token: '(.*)'", resp.text)[0]

URL0 = 'http://fanyi.baidu.com/'
TOKEN = re.findall(r"token: '(.*)'", requests.get(URL0, headers=HEADERS).text)[0]


'''

from __future__ import print_function
import logging
# import json

import re
import requests
# import execjs

# from sign_text import sign_text
from sign_text_js import sign_text_js

# from utils import (obrstr, headers, gtk, token)
# from utils import (obrstr, headers)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

HEADERS = {
    'Cookie':'BAIDUID=99C3CE30DA0FE8FD336F4428DA0DFDFC:FG=1; BIDUPSID=99C3CE30DA0FE8FD336F4428DA0DFDFC; PSTM=1515055428; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; locale=zh; PSINO=7; H_PS_PSSID=1443_25549_21127_22157; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1514859052,1515028770,1515029153,1515114213; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1515134327; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',  # NOQA
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'  # NOQA
}

URL0 = 'http://fanyi.baidu.com/'
TOKEN = re.findall(r"token: '(.*)'", requests.get(URL0, headers=HEADERS).text)[0]

GTK = '320305.131321201'
# TOKEN = '46e5646d48c43e676f955dc7fdece81f'
# TOKEN = 'ecb9f034a0f6b4899b38204a821a6f14ecb9f034a0f6b4899b38204a821a6f14'

# PARSERCALL = execjs.compile(OBRSTR).call

# SIGN = lambda que: PARSERCALL("wods", que, GTK)
URL = 'http://fanyi.baidu.com/v2transapi/'

TMP = \
"""
# replace with sign_text.sign_text
# time reduced from 1-2 sec/req to 0.6s/req
def sign_text(text):
    '''sign text'''
    return PARSERCALL("wods", text, GTK)
"""


def bd_fanyi(text, from_lang='auto', to_lang='zh'):
    '''translate from user input, q to quit

    :text: str
    :from_lang: str
    :to_lang: str
    :rtype: dict

    quick doctest with py.test or nosetest:

    py.test --doctest-modules bd_fanyi.py or
    nosetests --with-doctest bd_fanyi.p

    text = 'test'
    from_lang='auto'
    to_lang='zh'

    >>> text = 'test'
    >>> bd_fanyi(text)[0].keys() == [{'result': [[0, '测试', ['0|4'], [], ['0|4'], ['0|6']]], 'prefixWrap': 0, 'dst': '测试', 'relation': [], 'src': 'test'}][0].keys()
    True
    >>> bd_fanyi(text)[0].get('dst')
    '测试'
    >>> bd_fanyi('测试')[0].get('dst')
    'test'
    >>> bd_fanyi('测试', to_lang='en')[0].get('dst')
    'test'
    '''
    if isinstance(text, list):
        text = ' '.join(text)

    if from_lang is None:
        from_lang = 'auto'
    else:
        from_lang = from_lang.strip()

    if not from_lang:
        from_lang = 'auto'
    try:
        from_lang = str(from_lang)
    except Exception as exc:
        del exc
        from_lang = 'auto'

    if to_lang is None:
        to_lang = 'zh'
    else:
        to_lang = to_lang.strip()

    if not to_lang:
        to_lang = 'zh'
    try:
        to_lang = str(to_lang)
    except Exception as exc:
        del exc
        to_lang = 'zh'

    text = text.strip()

    if not text.strip():
        return ''

    # sign = SIGN(text)
    # sign = sign_text(text)
    sign = sign_text_js.hash(text, GTK)

    data = {
        'from': from_lang,
        'to': to_lang,
        'query': text,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': TOKEN,
    }

    # response = requests.post(URL, data=data, headers=HEADERS)
    # response.json()

	# response = requests.get('http://fanyi.baidu.com/', headers=HEADERS)
	# response = REQ_SESS.get(URL)

    # response = requests.get('https://fanyi.baidu.com/#en/zh/currency', verify=False)

    try:
        response = requests.post(URL, data=data, headers=HEADERS)

        # response = REQ_SESS.post(URL, data=data, headers=HEADERS)
        # response.encoding = 'utf-8'
        response.raise_for_status()
    except Exception as exc:
        LOGGER.error(exc)
        return str(exc)


    try:
        j_data = response.json()
        resu = j_data.get('trans_result')
        if resu is None:
            resu = j_data.get('error')
            resu = 'errors occurred, code: %s' % resu
        else:
            resu = resu.get('data')
    except Exception as exc:
        LOGGER.error(exc)
        resu = str(exc)

    # print(resu)
    return resu


def main():
    '''main'''
    import sys

    fmt = '%(name)s - %(filename)s [line:%(lineno)d]'
    fmt += '%(asctime)s:%(levelname)s:%(message)s'

    # logging.basicConfig(format=fmt, level=logging.DEBUG)
    logging.basicConfig(format=fmt, level=logging.INFO)

    logging.getLogger("urllib3.connectionpool").level = 30

    while True:
        if sys.version_info.major < 3:
            text = raw_input("请输入翻译的内容(退出q)：")
        else:
            text = input("请输入翻译的内容(退出q)：")
        text = text.strip()
        if text in ['q', 'Q']:
            break
        elif not text:
            continue
        else:
            print(bd_fanyi(text, 'en', 'zh'))


if __name__ == '__main__':
    main()
