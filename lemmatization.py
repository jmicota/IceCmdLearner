from reynir import Greynir
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

LEN_BASE = 20


def build_line(w1, w2, w3):
    line = ''
    line += w1
    line += ' ' * (LEN_BASE - len(w1))
    line += w2
    line += ' ' * (LEN_BASE - len(w2))
    line += w3
    line += ' ' * (LEN_BASE - len(w3))
    return line


# Generate analysis for en to is translation
def generate_analysis(sentence, tr):
    analysis = ''
    g = Greynir()
    job = g.submit(sentence)
    
    # Error example: 'thank you'
    # Iterate through sentences and parse each one
    try:
        tokens = word_tokenize(sentence)
        lemmas = []
        tr_lemmas = []

        # Extract lemmas
        for sent in job:
            sent.parse()
            lemmas = sent.lemmas

        # Extract lemma translations
        for lemma in lemmas:
            tr_lemmas.append(tr.translate(tr.ICELANDIC, tr.ENGLISH, lemma))

        # Return ERROR for definitely incorrect token translations
        for i in range(len(tr_lemmas)):
            if len(tr_lemmas[i].split(' ')) > 1:
                tr_lemmas[i] = 'ERROR'
        
        for i in range(len(tokens)):
            analysis += build_line(tokens[i], lemmas[i], tr_lemmas[i])
            analysis += '\n'
    except:
        analysis = 'Greynir parse failed. :(\n'

    return analysis
