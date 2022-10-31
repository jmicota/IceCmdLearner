import sys
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class Translator():

    def __init__(self):
        # Set up dictionary of language codes
        self.ENGLISH = 'en'
        self.ICELANDIC = 'is'
        self.available_languages = {self.ENGLISH, self.ICELANDIC}

        # Download part could be rewritten for more languages using defined language codes
        model_en_is = AutoModelForSeq2SeqLM.from_pretrained('Helsinki-NLP/opus-mt-en-is')
        model_is_en = AutoModelForSeq2SeqLM.from_pretrained('Helsinki-NLP/opus-mt-is-en')
        tokenizer_en_is = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-is')
        tokenizer_is_en = AutoTokenizer.from_pretrained('Helsinki-NLP/opus-mt-is-en')

        # Prepare model and tokenizer dictionaries
        self.models = {self.ENGLISH: {self.ICELANDIC: model_en_is},
                       self.ICELANDIC: {self.ENGLISH: model_is_en}}
        self.tokenizers = {self.ENGLISH: {self.ICELANDIC: tokenizer_en_is},
                           self.ICELANDIC: {self.ENGLISH: tokenizer_is_en}}


    def translate(self, from_lang, to_lang, sentence):
        # Ensure input type
        if not isinstance(sentence, str):
            sys.exit('Translator: Given sentence is not a string.\n')

        # Ensure existing support for chosen languages
        if from_lang not in self.models or from_lang not in self.tokenizers or \
           to_lang not in self.models[from_lang] or to_lang not in self.tokenizers[from_lang]:
           sys.exit(f'Translator: translation {from_lang} to {to_lang} unsupported.\n')

        # Extract correct tokenizer and model
        tokenizer = self.tokenizers[from_lang][to_lang]
        model = self.models[from_lang][to_lang]

        # Generate output
        input_ids = tokenizer(sentence, return_tensors='pt').input_ids
        outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=3, max_new_tokens=512)

        # Return best translation option
        outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        if len(outputs) == 0:
            return ''
        return outputs[0]