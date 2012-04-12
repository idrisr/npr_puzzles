"""
What is the longest familiar phrase, title or name in which the only consonants are N and T,
repeated as often as necessary? The other letters are vowels. Try to think of an answer with at least 18 letters.
"""

import string

def read_file(f_words):
    f = open(f_words)
    d = dict()
    for line in f:
        d [ line.strip().lower() ] = ''
    return d

def get_longest(d_words):
    l_letters = ['a', 'e', 'i', 'o', 'u', 'n', 't']
    for char in string.punctuation:
        l_letters.append(char)
    for char in string.whitespace:
        l_letters.append(char)
    """
    for char in string.digits:
        l_letters.append(char)
    """
    #holds words that fill criteria
    d = dict()
    

    for word in d_words:
        test = True
        for char in word:
            if char not in l_letters:
                test = False
        if test: d[word] = len(word)

    #list for moving items from dictionary
    l=list()

    for key, value in d.items():
        l.append((value, key))

    l.sort(reverse=True)
    return l

def main():
    """
    f = '/home/idris/word_lists/CROSSWD.TXT' #word list file
    f = '/home/idris/work/puzzle/phrases/a.txt'
    """
    f = '/home/idris/work/npr_puzzle/11_14_nt/dumps/all'
    f = '../12_12_waynemanor/wiki_title_dl.txt'
    d_words = read_file(f)

    l = get_longest(d_words)
    for item in l:
        if l.index(item) > 100: break
        print item 

if __name__ == '__main__':
    main()

