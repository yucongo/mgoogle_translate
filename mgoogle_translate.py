#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://github.com/littlecodersh/translation core.py

Based on http://translate.google.com/m?, use urllib.request

Modified to http://translate.google.cn/m? + requests_cache

MIT License

Copyright (c) 2016 Arnaud Aliès

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import logging
import re
import html.parser
import urllib.parse

from nose.tools import (eq_, with_setup)
import requests

import requests_cache
requests_cache.configure(allowable_methods=('GET', 'POST',))  # noqa POST does not seem to work
requests_cache.configure(cache_name='baidu_cache', expire_after=604800, allowable_methods=('GET', 'POST'))  # noqa a week: 7*24*3600 = 604800
requests_cache.install_cache('mgoogle_cache')

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

__date__ = '2017-04-13'
__version__ = '0.0.1'

AGENT = {
    'User-Agent':
    "Mozilla/4.0 (\
    compatible;\
    MSIE 6.0;\
    Windows NT 5.1;\
    SV1;\
    .NET CLR 1.1.4322;\
    .NET CLR 2.0.50727;\
    .NET CLR 3.0.04506.30\
    )"}

# expr = r'class="t0">(.*?)<'
EXPR = re.compile(r'class="t0">(.*?)<')


def mgoogle_translate(to_translate, from_lang="en", to_lang="zh-CN"):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default

    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """

    # from_language = from_lang
    # to_language = to_lang

    # if not isinstance(to_translate, str):
        # LOGGER.debug(" Input not a str, return None")
        # return None

    # base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    base_link = "http://translate.google.cn/m?hl=%s&sl=%s&q=%s"
    to_translate = urllib.parse.quote(to_translate)
    link = base_link % (to_lang, from_lang, to_translate)

    # request = urllib.request.Request(link, headers=agent)
    request = requests.get(link, headers=AGENT)

    # raw_data = urllib.request.urlopen(request).read()
    # raw_data = request.content

    # data = raw_data.decode("utf-8")

    # re_result = re.findall(expr, data)
    # re_result = re.findall(expr, request.text)
    re_result = EXPR.findall(request.text, 1)

    # result = len(re_result) and re_result[0]
    # result = 'Nothing retrieved...' if not len(re_result) else re_result[0]
    # return 'Nothing retrieved...' if not len(re_result) else re_result[0]

    parser = html.parser.HTMLParser(convert_charrefs=True)

    return parser.unescape('Nothing retrieved...' if not re_result else re_result[0])


def my_setup():
    """my_setup."""

    fmt = '%(name)s-%(filename)s[ln:%(lineno)d]:'
    fmt += '%(levelname)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.DEBUG)


@with_setup(my_setup)
def test_fr():
    """test_fr+++."""
    text = "Moscou, entre le secrétaire d’Etat Rex Tillerson et son homologue Sergeï Lavrov. M. Trump a jugé « formidable si l’OTAN et [les Etats-Unis] pouvaient s’entendre avec la Russie », avant d’ajouter qu’« à l’heure actuelle, nous ne nous entendons pas du tout avec la Russie »."
    out = mgoogle_translate(text, from_lang='auto')
    exp = '莫斯科，国务卿雷克斯·蒂森和他的外长拉夫罗夫之间。 M·特朗普说，这是“巨大的，如果北约和[美国]可'
    eq_(exp, out[:50])


@with_setup(my_setup)
def test_fr2en():
    """test_fr2en+++."""
    text = "Moscou, entre le secrétaire d’Etat Rex Tillerson et son homologue Sergeï Lavrov. M. Trump a jugé « formidable si l’OTAN et [les Etats-Unis] pouvaient s’entendre avec la Russie », avant d’ajouter qu’« à l’heure actuelle, nous ne nous entendons pas du tout avec la Russie »."
    out = mgoogle_translate(text, from_lang='fr', to_lang='en')
    exp = 'Moscow, between Secretary of State Rex Tillerson and his counterpart Sergei Lavrov. Mr Trump said it was "formidable if NATO and [the United States] c'  # noqa
    eq_(exp, out[:150])


@with_setup(my_setup)
def test_gr():
    """test_gr+++."""
    text = "συνήθης ἤδη μοί ἐστιν, ὦ Σώκρατες, διὰ τὸ πολλάκις δεῦρο φοιτᾶν, καί τι καὶ εὐεργέτηται ὑπ᾽ ἐμοῦ."
    out = mgoogle_translate(text, from_lang='auto')
    exp = '通常已经分子Estin，AZ Sokratous，对于多取代，前来出席，并Ti和我evergetit'
    eq_(exp, out[:50])
