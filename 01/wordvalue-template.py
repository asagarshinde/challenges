from data import DICTIONARY, LETTER_SCORES
import operator

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [word.strip() for word in f]

def calc_word_value(words):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    d = {}
    for word in words:
        score = 0
        for letter in word.strip():
            if letter.isalpha():
                score = score + LETTER_SCORES[letter.upper()]
                d[word] = score
    return d

def max_word_value(d):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    return(sorted_d[len(sorted_d)-1])
if __name__ == "__main__":
    words = load_words() # run unittests to validate
    values = calc_word_value(words)
    max_word = max_word_value(values)
    print max_word
