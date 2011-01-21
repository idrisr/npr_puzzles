# http://www.npr.org/series/4473090/sunday-puzzle

# Next Week's Challenge

# From listener Mike Shteyman of Reisterstown, Md.: Take the first seven letters of the alphabet, A through G,
# change one of these letters to another letter that is also either A, B, C, D, E, F or G.
# Rearrange the result to spell a familiar seven-letter word. What word is it

import sys
sys.path.append('/home/idris/work/npr_puzzles')
#sys.path.append('~/work/npr_puzzles/')

from util import load_word_dictionary
from util import swap_letter
from util import permutate
from util import word_in_dict

# string from a to g
s = 'abcdefg'

l_words = list()

# loads word list into dict()
d_dict = load_word_dictionary()

#creates list of possible words when swapping one letter from 'abcdefg'
for i in range(0, len(s)):
    for j in range(0, len(s)):
        # i == j just reproduces original string
        if i <> j :
            swap_word = swap_letter(s, s[i], j) 
            l_words.append( swap_word )

#tests all permutations and checks if permutation of string is in dictionary and prints any finds
for i in l_words:
    l_perm = permutate(i)
    s_perm = set(l_perm)
    for j in s_perm:
        if word_in_dict(j, d_dict):
            print "Original String:\t%s" % ( i,) 
            print "Rearranged String:\t%s" % (j,)
