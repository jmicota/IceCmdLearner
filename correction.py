from reynir_correct import tokenize, check_errors
import re

LEN_BASE = 20


# Takes an Icelandic sentence as input, returns it corrected.
def correct_sentence(sent):
    err_str = check_errors(**{"input": sent, "annotations": True, "all_errors": True, "format": "text", "one_sent": True})
    corr_sent = ""
    annots = []
    for i, line in enumerate(err_str.split("\n")):
        if (i == 0):
            corr_sent = line
        else:
            annots.append(line)

    return corr_sent, annots


# Catches token-level errors such as spelling and bad phrases - does not correct grammatical errors.
def correct_tokens(sent):
    err_tokens = tokenize(sent)
    corr_tokens = []
    annot_obj = {}
    for tok in err_tokens:
        if tok.txt != "":
            annot_obj[tok.txt] = tok.error_description
            corr_tokens.append(tok.txt)
        #print("{0:10} {1}".format(tok.txt or "", tok.error_description))

    corr_tok_str = " ".join(corr_tokens)
    corr_tok = re.sub(r'\s([?.!,:;"](?:\s|$))', r'\1', corr_tok_str)
    return corr_tok, annot_obj


def build_feedback_line(w1, text):
    line = ''
    line += w1
    line += ' ' * (LEN_BASE - len(w1))
    line += text
    return line


def build_feedback(tok_err_dict, correct_sent):
    feedback = ''
    if len(tok_err_dict) == 0:
        feedback += '\n-----> All tokens correct.\n'
    else:
        feedback += '\nToken correction:\n' + 60 * '-' + '\n'
        for key in tok_err_dict.keys():
            feedback += build_feedback_line(key, tok_err_dict[key])
            feedback += '\n'
    
    feedback += f'\nCorrect sentence:\n' + 60 * '-' + f'\n{correct_sent}\n'
    # feedback += '\n'
    # if len(sent_err_list) == 0:
    #     feedback += 'Sentence correct.\n'
    # else:
    #     feedback += 'Sentence level correction:\n'
        # for value in sent_err_list:
        #     feedback += value
        #     feedback += '\n'

    return feedback


def feedback(sentence, tr):
    _, err_tok = correct_tokens(sentence)
    corr_sent, _ = correct_sentence(sentence)

    corr_tok_dict = {}
    for key in err_tok:
        if err_tok[key] != '':
            feedback = tr.translate(tr.ICELANDIC, tr.ENGLISH, err_tok[key])
            corr_tok_dict[key] = feedback

    # corr_sent_list = []
    # for value in err_sent:
    #     feedback = tr.translate(tr.ICELANDIC, tr.ENGLISH, value)
    #     corr_sent_list.append(feedback)

    return build_feedback(corr_tok_dict, corr_sent)
