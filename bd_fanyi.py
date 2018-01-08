# -*- coding: utf-8 -*-
'''
baidu fanyi, token diy
OBRSTR and Cookie from: https://gitee.com/o0elias0o/eliaspython/tree/master

# 需要安装的库
# pip install requests
# pip install PyExecJS

PyExecJS 需 js 环境或解释器（如 nodejs 或 phantomjs.exe)
'''

from __future__ import print_function
import logging
# import json

import requests
import execjs

# from utils import (obrstr, headers, gtk, token)
# from utils import (obrstr, headers)

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

OBRSTR = \
'''function wods(r,gtk) {
    function a(df, o) {
        for (var t = 0; t < o.length - 2; t += 3) {
            var a = o.charAt(t + 2);
            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a), a = "+" === o.charAt(t + 1) ? df >>> a : df << a, df = "+" === o.charAt(t) ? df + a & 4294967295 : df ^ a
        }
        return df
    }
    var o = r.length;
    o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substr(-10, 10));
    var t = gtk, e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0;
    for (var  g = 0; g < r.length; g++) {
        var m = r.charCodeAt(g);
        128 > m ? d[f++] = m : (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320 === (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)), d[f++] = m >> 18 | 240, d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224, d[f++] = m >> 6 & 63 | 128), d[f++] = 63 & m | 128)
    }
    var S = h, u = "+-a^+6", l = "+-3^+b+-f";
    for (var s = 0; s < d.length; s++) S += d[s], S = a(S, u);
    return S = a(S, l), S ^= i, 0 > S && (S = (2147483647 & S) + 2147483648), S %= 1e6, S.toString() + "." + (S ^ h) }'''  # NOQA

HEADERS = {
    'Cookie':'BAIDUID=99C3CE30DA0FE8FD336F4428DA0DFDFC:FG=1; BIDUPSID=99C3CE30DA0FE8FD336F4428DA0DFDFC; PSTM=1515055428; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; locale=zh; PSINO=7; H_PS_PSSID=1443_25549_21127_22157; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1514859052,1515028770,1515029153,1515114213; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1515134327; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',  # NOQA
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'  # NOQA
}

GTK = '320305.131321201'
TOKEN = '46e5646d48c43e676f955dc7fdece81f'
PARSERCALL = execjs.compile(OBRSTR).call
# SIGN = lambda que: PARSERCALL("wods", que, GTK)
URL = 'http://fanyi.baidu.com/v2transapi/'


def sign_text(text):
    '''sign text'''
    return PARSERCALL("wods", text, GTK)


def bd_fanyi(text, from_lang='auto', to_lang='zh'):
    '''translate from user input, q to quit

    :text: str
    :from_lang: str
    :to_lang: str
    :rtype: dict

    quick doctest with py.test or nosetest:

    py.test --doctest-modules bd_fanyi.py or
    nosetests --with-doctest bd_fanyi.p

    >>> text = 'test'
    >>> bd_fanyi(text)[0].keys() == [{'result': [[0, '测试', ['0|4'], [], ['0|4'], ['0|6']]], 'prefixWrap': 0, 'dst': '测试', 'relation': [], 'src': 'test'}][0].keys()
    True
    >>> bd_fanyi(text)[0].get('dst')
    '测试'
    '''
    text = text.strip()

    if not text.strip():
        return ''

    # sign = SIGN(text)
    sign = sign_text(text)
    data = {
        'from': from_lang,
        'to': to_lang,
        'query': text,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': TOKEN
    }

    try:
        response = requests.post(URL, data=data, headers=HEADERS)
        # response.encoding = 'utf-8'
        response.raise_for_status()
    except Exception as exc:
        LOGGER.error(exc)
        return str(exc)

    try:
        resu = response.json().get('trans_result').get('data')  # NOQA
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
