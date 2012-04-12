import string

p = '../wiki/wiki_title_dl.txt'
#p = '../wiki/wiki_test.txt'
f = open(p, 'r')

d = dict()

for line in f.readlines():
    d[line.strip().lower()] = None
f.close()

def has_underscore_middle(s):
    """returns true if string 's' has underscore not including end or beginning"""
    s = s[1:-1]
    return s.find('_') > -1

def has_right_length(s, l = 7):
    """return True if string 's' is correct length 'l'=7"""
    return len(s) == l

def has_ascii_letters_only(s):
    """return True if string 's' is made up only of ascii letters"""
    for char in s:
        if char not in string.ascii_letters:
            return False
    return True

def get_from_underscore(s):
    """accepts string 's' that is expected to have "_"
    return from "_" on, exclusive"""
    reverse = s[::-1]
    loc_ = reverse.find('_')

    return s[-loc_:]

def load_word_dictionary():
    p = '/home/idris/word_lists/CROSSWD.TXT'
    f = open(p, 'r')
    d= dict()
    for line in f.readlines():
        d[line.strip().lower()] = None
    return d

def mix_last_name(s):
    """Takes a seven letter string 's' and creates new 6 letter string
    with last 2 letters of 's' + first four letters of 's'
    Ex: "abcdefg" --> "fgabcd" """
    return s[-2:] + s[:4]


l = list()

#Step 1 of Solution - grab Wikipedia entries that are possibly in form firstname_lastname with len(last_name)==7
for name in d:
    if has_underscore_middle(name):
        last_name = get_from_underscore(name)
        if has_right_length(last_name):
            if has_ascii_letters_only(last_name):
                l.append( (name, last_name) ) 

d_word_list = load_word_dictionary()

pout = 'output.txt'
fout = open(pout, 'w')

#Step 2 of Solution - move around letters in last name and see if result is in crossword dictionary
for name in l:
    prof = mix_last_name(name[1])
    if prof in d_word_list:
        write = "%s \t %s \t %s \n" % (prof, name[0], name[1])
        fout.write( write ) 


