# What: Python Solution to Will Shortz NPR Word 1/30/2011
# work puzzle at http://www.npr.org/2011/01/30/133338451/no-business-like-snow-business
#
# From Alan Meyer of Newberg, Ore.: Think of a common word that's six letters
# long and includes a Q. Change the Q to an N, and rearrange the result to
# form a new word that's a synonym of the first one. What are the words?
# Author: Idris Raja
# email: idris.raja@gmail.com
# date: 1-30-2011

import sys
sys.path.append('/home/idris/work/npr_puzzles')

from util import load_word_dictionary
from util import permutate
from util import swap_letter
from util import check_synonym
from util import is_len
from util import has_string
from util import word_in_dict

#dict to hold all words
d_words = load_word_dictionary()

#dict to hold all words of length 6 with letter q
d_6q_words = dict()
for word in d_words:
    if has_string(word, 'q') and is_len(word, 6):
        d_6q_words[word]=None

#dict to hold all words of length with letter q, and 'q' swapped for 'n'
d_6n_words = dict()
for word in d_6q_words:
    new_word = swap_letter(word,'n',word.find('q'))
    d_6n_words[new_word] = word

for word in d_6n_words:
    #get all anagrams of words with q already swapped for n
    l_perm = permutate(word)
    s_perm = set(l_perm)

    for j in s_perm:
        #for each anagram, see if anagram is in dictionary
        if word_in_dict(j, d_words):
            q_word = d_6n_words[word ]
            n_word = j
            #if anagram in dictionary, use WordNet functionality to see if q_word and n_word are synonyms
            if check_synonym( q_word, n_word):
                print 'Orig q-word:%s, New n-word:%s' % (q_word, n_word)
