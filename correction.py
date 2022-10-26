import reynir
from reynir_correct import tokenize, check_single, check_errors
import re

def correct_sentence(sent):
    """ Takes an Icelandic sentence as input, returns it corrected. """

    err_str = check_errors(**{"input": sent, "annotations": True, "all_errors": True, "format": "text", "one_sent": True})
    corr_sent = ""
    annots = []
    for i, line in enumerate(err_str.split("\n")):
        if (i == 0):
            corr_sent = line
        else:
            annots.append(line)

    return corr_sent, annots

def correct_tokens(sent):
    """ Catches token-level errors such as spelling and bad phrases - does not correct grammatical errors. """
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



if __name__ == "__main__":

    sent1 = "Páli, vini mínum, langaði að horfa á sjónnvarpið eftir útileiguna."
    sent2 = "Af gefnu tilefni fékk daninn vilja sýnum framgengt í auknu mæli."
    sent3 = "Hann hlóg af mér til hins ítrasta, eins og mannsals grýnið hafi verið harmlaust."
    sent4 = "ég lýt á hann og spyr hann kvort ég meigi þetta."

    # Token-level correction
    corr_tok_sent1, err_tok_sent1 = correct_tokens(sent1)
    corr_tok_sent2, err_tok_sent2 = correct_tokens(sent2)
    corr_tok_sent3, err_tok_sent3 = correct_tokens(sent3)
    corr_tok_sent4, err_tok_sent4 = correct_tokens(sent4)

    # Full grammar correction
    corr_sent1, annots_sent1 = correct_sentence(corr_tok_sent1)
    corr_sent2, annots_sent2 = correct_sentence(corr_tok_sent2)
    corr_sent3, annots_sent3 = correct_sentence(corr_tok_sent3)
    corr_sent4, annots_sent4 = correct_sentence(corr_tok_sent4)

    # obj = correct_sentence(sent2)
    # print(obj)


