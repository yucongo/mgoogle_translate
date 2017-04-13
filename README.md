# mgoogle_translate

Machine translation based on translate.google.cn/m? and requests_cache. Tested on Python 3.4 and Windows 7.

Key idea from core.py from https://github.com/littlecodersh/translation 

Example usage:

    text = "Moscou, entre le secrétaire d’Etat Rex Tillerson et son homologue Sergeï Lavrov. M. Trump a jugé « formidable si l’OTAN et [les Etats-Unis] pouvaient s’entendre avec la Russie », avant d’ajouter qu’« à l’heure actuelle, nous ne nous entendons pas du tout avec la Russie »."
    out = mgoogle_translate(text, from_lang='auto')
    # '莫斯科，国务卿雷克斯·蒂森和他的外长拉夫罗夫之间。 M·特朗普说，这是“巨大的，如果北约和[美国]可以与俄罗斯同意”，并补充说：“目前，我们不同意俄罗斯在所有”。'
    
    out = mgoogle_translate(text, from_lang='fr')
    # same as above
    
    out = mgoogle_translate(text, to_lang='en')
    # the same as mgoogle_translate(text, from_lang='en', to_lang='en'), hence out == text is True
    
    mgoogle_translate(text, from_lang='fr', to_lang='en')
    # 'Moscow, between Secretary of State Rex Tillerson and his counterpart Sergei Lavrov. Mr Trump said it was "formidable if NATO and [the United States] could reach an understanding with Russia", adding that "at the moment we do not agree with Russia at all ".'
      
