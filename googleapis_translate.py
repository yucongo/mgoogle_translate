# -*- coding: utf-8 -*-
"""
googleapis_translate

Refer to mgoogle_translate.py
"""
import logging
from nose.tools import (eq_, with_setup)

import requests

import requests_cache
requests_cache.configure(allowable_methods=('GET', 'POST',))  # noqa POST does not seem to work
requests_cache.configure(cache_name='baidu_cache', expire_after=604800, allowable_methods=('GET', 'POST'))  # noqa a week: 7*24*3600 = 604800
requests_cache.install_cache('googleapis_cache')

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
    "Referer": "http://wap.baidu.com"}

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

__date__ = '2017-04-13'
__version__ = '0.0.1'

def googleapis_translate(to_translate, from_lang="en", to_lang="zh-CN")->"str":
    """
    googleapis_translate.

    googleapis_translate(to_translate, from_lang="en", to_lang="zh-CN")
    """

    base_link = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=%s&tl=%s&dt=t&q=%s"

    # to_translate = urllib.parse.quote(to_translate)

    link = base_link % (from_lang, to_lang, to_translate)
    request = requests.get(link, headers=HEADERS)
    try:
        jdata = request.json()
    except Exception as exc:
        LOGGER.critical(
            " json data error, returning None, exception: %s ", exc)
        return None
    text = [elm[0] for elm in jdata[0]]
    return ''.join(text)


def my_setup():
    """my_setup."""

    fmt = '%(name)s-%(filename)s[ln:%(lineno)d]:'
    fmt += '%(levelname)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.DEBUG)


@with_setup(my_setup)
def test_en():
    """test_en+++."""
    to_translate = 'More than three years ago, I put forward the "one way" initiative. For more than three years, more than 100 countries and international organizations have responded positively, and more than 40 countries and international organizations have signed cooperation agreements with China. The "circle of friends" is expanding.'
    out = googleapis_translate(to_translate, to_lang='zh-CN')
    exp = '三年多前，我提出了“单向”举措。三年来，100多个国家和国际组织积极响应，40多个国家和国际组织与中国签署了合作协议。 “朋友圈”正在扩大。'
    eq_(exp, out)


@with_setup(my_setup)
def test_fr2en_zh():
    """test_fr2en+zh+++."""
    text = "Moscou, entre le secrétaire d’Etat Rex Tillerson et son homologue Sergeï Lavrov. M. Trump a jugé « formidable si l’OTAN et [les Etats-Unis] pouvaient s’entendre avec la Russie », avant d’ajouter qu’« à l’heure actuelle, nous ne nous entendons pas du tout avec la Russie »."
    out = googleapis_translate(text, from_lang='fr', to_lang='en')
    exp = 'Moscow, between Secretary of State Rex Tillerson and his counterpart Sergei Lavrov. Mr Trump said it was "formidable if NATO and [the United States] c'  # noqa
    eq_(exp, out[:150])

    exp = '莫斯科，国务卿雷克斯·蒂森和他的外长拉夫罗夫之间。 M·特朗普说，这是“巨大的，如果北约和[美国]可以与俄罗斯同意”，并补充说：“目前，我们不同意俄罗斯在所有”。'
    out = googleapis_translate(text, from_lang='fr')
    eq_(exp, out)
