# http://www.npr.org/2011/01/02/132556000/remember-these-names-from-2010  

# From Mark Leeper of Matawan, N.J.: Take a plural noun that ends with the letter S. Insert a space somewhere in this word, retainin
# g the order of the letters. The result will be a two-word phrase that has the same meaning as the original word, except in the si
# ngular. What word is this? 

import sys
sys.path.append('~/work/npr_puzzles')
from util import load_word_dictionary
from util import ends_with_letter
from util import split_word_once
from util import word_in_dict
from util import check_synonym

def main():
    path_dict = '/home/idris/word_lists/CROSSWD.TXT'
    d_word_list = load_word_dictionary( path_dict ) 
    l_words_end_s = [word for word in d_word_list if ends_with_letter(word, 's')]
    path_output = 'output.txt'
    fout = open(path_output, 'w')

    #go through list of words ending with s
    for word_end_s in l_words_end_s:
        #go through list of ways to split word_ending_with_s
        for splits in split_word_once( word_end_s ):
            if word_in_dict(splits[0], d_word_list) and word_in_dict(splits[1], d_word_list):
                s = '%s, %s %s\n' % (word_end_s, splits[0], splits[1])
                syn_test = '%s_%s' % (splits[0], splits[1])
                l_syns = check_synonym(word_end_s, syn_test)
                fout.write(s)

if __name__ == '__main__':
    main()
