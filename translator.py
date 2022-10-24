import sys
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class Translator:
    ENGLISH = 'en'
    ICELANDIC = 'is'

    def __init__(self):
        print('Setting up translator..')
        model_en_is = AutoModelForSeq2SeqLM.from_pretrained('Helsinki-NLP/opus-mt-en-is')
        model_is_en = AutoModelForSeq2SeqLM.from_pretrained('Helsinki-NLP/opus-mt-is-en')
        tokenizer_en_is = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-is')
        tokenizer_is_en = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-is-en')

        self.models = {'en': {'is': model_en_is},
                       'is': {'en': model_is_en}}
        self.tokenizers = {'en': {'is': tokenizer_en_is},
                            'is': {'en': tokenizer_is_en}}
        print('Translator ready.')


    def translate(self, from_lang, to_lang, sentence):
        # ensure sentence is a string
        if not isinstance(sentence, str):
            sys.exit('Translator: Given sentence is not a string.')

        if from_lang not in self.models or from_lang not in self.tokenizers or \
           to_lang not in self.models[from_lang] or to_lang not in self.tokenizers[from_lang]:
           sys.exit(f'Translator: translation {from_lang} to {to_lang} unsupported.')

        tokenizer = self.tokenizers[from_lang][to_lang]
        model = self.models[from_lang][to_lang]

        input_ids = tokenizer(sentence, return_tensors='pt').input_ids
        outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=3, max_new_tokens=512)

        return tokenizer.batch_decode(outputs, skip_special_tokens=True)

    
