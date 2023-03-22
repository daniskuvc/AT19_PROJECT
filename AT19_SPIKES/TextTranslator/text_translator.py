#
# @text_translator.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import googletrans
from googletrans import Translator


print(googletrans.__version__)
print(googletrans.LANGUAGES)
translator = Translator()
text1 = 'おはようございます'
language = 'es'
translated = translator.translate(text1, dest = language)
languages = googletrans.LANGUAGES
lang = str(languages[str(translated.src)])

translation: dict = {
            "Source language": languages[str(translated.src)].capitalize(),
            "Translation": str(translated.text),
            "Pronunciation": str(translated.extra_data['origin_pronunciation'])
        }
print(translation)
# for python 3.8 or below
