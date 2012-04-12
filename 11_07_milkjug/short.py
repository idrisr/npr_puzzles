"""
You are given a word and must provide a second word to complete a familiar two-word phrase. The first letter of the word must be the last letter of the word given, and the last letter of the word must be the first letter of the word given. For example, given the clue "photo," the answer would be "op."def dict_load():


"""   
   fin = open(f_dict)
    d=dict()
    for line in fin:
        d[ line.strip().lower() ] = ''
    return d

NUM_LET = 7
f_dict = '/home/idris/word_lists/CROSSWD.TXT'#word list file
f = '/home/idris/work/puzzle/output.txt'#output file
d_dict = dict_load()

def create_seven_letter_seq():
    """create NUM_LET letter conseq string"""
    l=list()
    for i in range(0, 26-(NUM_LET)+1):
        word=''
        for j in range(0,NUM_LET):
            word+= chr(j+i+97) 
        l.append(word)
    word=''
    return l

def replace_letter(l_seqs, letter='u'):
    """replace one letter of word with new letter"""
    l=list()
    for item in l_seqs:
        l2=list()
        for i in range(0,NUM_LET): 
            word = item[:i] + letter + item[i+1:]
            l2.append(word)
        l.append(l2)
    return l

def perm_seqs(l_seq):
    """scramble 7 letter seq into all possibile arrangements - return list of combinations"""
    l_perms=list()
    for l_item in  l_seq:
        #items in l_seq are lists of letter sequences replaced with 'u'
        for item in l_item:
            #item is string of characters with 'u' already present
            temp = permutate(item)
            for item in temp:
                l_perms.append(item)
    return l_perms 

def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]

            for m in permutate(part):
                x=seq[k:k+1] + m
                temp.append(x)
        return temp

def split_word(f, word):
	"""split 7 letter word into two, 1 char+6 char, 2char+5char, etc - return 2 elem tuple"""
        for i in range(1, len(word)):
            word1 = word[:i]
            word2 = word[i:]
            if word1 in d_dict:
                if word2 in d_dict:
                    output = '%s %s /n' % (word1, word2)
                    f.write( output )

def split_words(f, l_words):
    for item in l_words:
        words = split_word(f, item)

def dict_lookup_words(t_words):
	"""look up word pair in dictionary, if they are both in dictionary, output to file"""
        return 
    
def dict_load():
    fin = open(f_dict)
    d=dict()
    for line in fin:
        d[ line.strip().lower() ] = ''
    return d

def main():
    #create 7 alphabetical string sequences, return list of seqs
    l_seqs = create_seven_letter_seq()

    #create string sequences with one letter replaced by 'u', return dict of key=seq, items=list of new seqs with 'u'
    l_seq = replace_letter(l_seqs)

    #order 7 char seqs into all arrangements
    l_seqs = perm_seqs(l_seq)

    #load cross-word dictionary into dictionary
    d_dict = dict_load()

    #open output file
    fout = open(f, 'w')

    #split all 7 letter sequences into 2 words, min word length = 1, see if they're in dict, add to output file if yes
    split_words(fout,  l_seqs)    

    #close output file
    fout.close()
    

if __name__ == '__main__':
    main()
