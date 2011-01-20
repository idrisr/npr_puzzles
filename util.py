# Contains common utility functions used to solve NPR word puzzles
from nltk.corpus import wordnet as wn

def load_word_dictionary(path='/home/idris/word_lists/CROSSWD.TXT'):
    """takes "path" that is path of word list file. Function assumes one word per line.
    White space and capitalization stripped out.  returns dictionary of words with key=word, and value=None"""
    f = open(path, 'r')
    d= dict()
    for line in f.readlines():
        d[line.strip().lower()] = None
    return d

def check_synonym(word, word2):
    """checks to see if word2 is a synonym of word2"""
    l_syns = list()
    synsets = wn.synsets(word)
    for synset in synsets:
        if word2 in synset.lemma_names:
            l_syns.append( (word, word2) )
    return l_syns

def ends_with_letter(word, letter):
    """takes "word" and tests to see if last letter is 'letter'"""
    if len(word)>0:
        return word[-1] == letter
    else:
        return False

def split_word_once(word, min_char=2):
    """takes a word and splits it into two segments, with at least 'min_char' in
    each segment. Stores segment in a list, and ultimately returns a list of the
    segment lists"""
    l_segments = list()
    for split in range(min_char, len(word) - min_char + 1):
        l_segment = list()
        l_segment.append( word[:split] )
        l_segment.append( word[split:] )
        l_segments.append( l_segment ) 

    return l_segments

def word_in_dict(word, d):
    return word in d
