import translator

ENGLISH = 'en'
ICELANDIC = 'is'

translator_obj = translator.Translator()

translated = translator_obj.translate(ENGLISH, ICELANDIC, 'I am leaving this place')
print(translated)

translated = translator_obj.translate(ICELANDIC, ENGLISH, 'Ég ætla ađ fara héđan')
print(translated)

translated = translator_obj.translate(ENGLISH, ICELANDIC, 'Ég ætla ađ fara héđan')
print(translated)