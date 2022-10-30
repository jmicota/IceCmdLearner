from curses import keyname
import translator
import warnings
warnings.filterwarnings('ignore')


def pipeline(sentence, lang, target_lang, translator=None, corrector=None):
    translated = tr.translate(lang, target_lang, sentence)
    return translated


if __name__ == '__main__':
    print('\n----- Setting up your personal AI teacher..')
    tr = translator.Translator()
    print('----- Teacher has arrived.')

    print('\n----- ICE CMD LEARNER READY')
    print('----- Currently supported 2 languages. Target translation language will be selected automatically.')
    print('----- Input empty sentence to switch languages.\n')

    try:
        while True:
            language = ''
            while language not in tr.available_languages:
                if language != '':
                    print('Language code not supported')
                language = input(f'Choose language of input ({tr.ENGLISH}/{tr.ICELANDIC}): ')
        
            print(f'Input language set to: {language}')
            target_language = tr.ICELANDIC if language == tr.ENGLISH else tr.ENGLISH

            input_sentence = input('Input: ')
            while not input_sentence == '':
                translated = pipeline(input_sentence, language, target_language)
                print(translated)
                input_sentence = input('Input: ')
    except KeyboardInterrupt:
        print('\n\n----- Goodbye!')
