from curses import keyname
import translator
import correction
import lemmatization
import warnings
warnings.filterwarnings('ignore')


def pipeline_en_is(sentence, tr):
    translated = tr.translate(tr.ENGLISH, tr.ICELANDIC, sentence)
    corrected, _ = correction.correct_sentence(translated)
    print('-----> ' + corrected)
    return lemmatization.generate_analysis(corrected, tr)


def pipeline_is_en(sentence, tr):
    translated = tr.translate(tr.ICELANDIC, tr.ENGLISH, sentence)
    print('-----> ' + translated)
    return correction.feedback(sentence, tr)


def pipeline(sentence, lang, tr):
    result = ''
    if lang == tr.ENGLISH:
        result = pipeline_en_is(sentence, tr)
    else:
        result = pipeline_is_en(sentence, tr)
    return result


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
                    print('-----> Language code not supported\n')
                language = input(f'Choose language of input ({tr.ENGLISH}/{tr.ICELANDIC}): ')
        
            print(f'-----> Input language set to: {language}\n')
            target_language = tr.ICELANDIC if language == tr.ENGLISH else tr.ENGLISH

            input_sentence = input(f'({language}) Input: ')
            while not input_sentence == '':
                output = pipeline(input_sentence, language, tr)
                print(output)
                input_sentence = input(f'({language}) Input: ')
    except KeyboardInterrupt:
        print('\n\n----- Goodbye!')
