# mgoogle_translate/googleapis_translate

## mgoogle_translate

Machine translation based on translate.google.cn/m? and requests_cache. Tested on Python 3.4 and Windows 7.

Key idea from core.py from https://github.com/littlecodersh/translation 

mgoogle_translate Example usage:

    text = "Moscou, entre le secrétaire d’Etat Rex Tillerson et son homologue Sergeï Lavrov. M. Trump a jugé « formidable si l’OTAN et [les Etats-Unis] pouvaient s’entendre avec la Russie », avant d’ajouter qu’« à l’heure actuelle, nous ne nous entendons pas du tout avec la Russie »."
    out = mgoogle_translate(text, from_lang='auto')
    # '莫斯科，国务卿雷克斯·蒂森和他的外长拉夫罗夫之间。 M·特朗普说，这是“巨大的，如果北约和[美国]可以与俄罗斯同意”，并补充说：“目前，我们不同意俄罗斯在所有”。'
    
    out = mgoogle_translate(text, from_lang='fr')
    # same as above
    
    out = mgoogle_translate(text, to_lang='en')
    # the same as mgoogle_translate(text, from_lang='en', to_lang='en'), hence out == text is True
    
    mgoogle_translate(text, from_lang='fr', to_lang='en')
    # 'Moscow, between Secretary of State Rex Tillerson and his counterpart Sergei Lavrov. Mr Trump said it was "formidable if NATO and [the United States] could reach an understanding with Russia", adding that "at the moment we do not agree with Russia at all ".'
      
## googleapis_translate

This one is based on https://www.v2ex.com/t/353781 which mentions a link https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q=Hello in stackoverflow. The stackoverflow link was from here http://stackoverflow.com/questions/8085743/google-translate-vs-translate-api dated Nov 19 '15. Yet the  https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=es&dt=t&q=Hello still works!

googleapis_translate Example usage:

    from nose.tools import eq_
    to_translate = 'More than three years ago, I put forward the "one way" initiative. For more than three years, more than 100 countries and international organizations have responded positively, and more than 40 countries and international organizations have signed cooperation agreements with China. The "circle of friends" is expanding.'
    out = googleapis_translate(to_translate, to_lang='zh-CN')
    exp = '三年多前，我提出了“单向”举措。三年来，100多个国家和国际组织积极响应，40多个国家和国际组织与中国签署了合作协议。 “朋友圈”正在扩大。'
    eq_(exp, out)

    text = "Moscou, entre le secrétaire d’Etat Rex Tillerson et son homologue Sergeï Lavrov. M. Trump a jugé « formidable si l’OTAN et [les Etats-Unis] pouvaient s’entendre avec la Russie », avant d’ajouter qu’« à l’heure actuelle, nous ne nous entendons pas du tout avec la Russie »."
    out = googleapis_translate(text, from_lang='fr', to_lang='en')
    exp = 'Moscow, between Secretary of State Rex Tillerson and his counterpart Sergei Lavrov. Mr Trump said it was "formidable if NATO and [the United States] c'  # noqa
    eq_(exp, out[:150])

    exp = '莫斯科，国务卿雷克斯·蒂森和他的外长拉夫罗夫之间。 M·特朗普说，这是“巨大的，如果北约和[美国]可以与俄罗斯同意”，并补充说：“目前，我们不同意俄罗斯在所有”。'
    out = googleapis_translate(text, from_lang='fr')
    eq_(exp, out)
