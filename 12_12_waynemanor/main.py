import simplejson as json
import string

def remove_string(s, old = '(disambiguation)', new = ''):
    """takes string 's' and replaces any occurences of 'old' in string with 'new'"""
    return s.replace(old, new)    

def load_json_from_file(p):
    """Takes relative file path of json file and returns dictionary of parsed json"""
    f = open(p, 'r')
    l = json.load(f)
    return l

def load_from_text(p):
    f = open(p, 'r')
    l = list()
    for line in f:
        s = remove_string(line)
        l.append(s)
    return l

def normalize_word(s):
    """removes extra characters, ex:'disambiguation', spaces, and non ascii letters"""
    sorted_word = sort_word(s.lower() )
    return ''.join( [char for char in sorted_word if char in string.ascii_letters] )

def sort_word(word):
    """sorts word and removes white spaces"""
    l = [letter for letter in word]
    l.sort(reverse=False)
    sort_word = ''.join([letter for letter in l])
    return sort_word

def build_dict(l):
    """takes list of string entries and sorts each string by char value and strips out anything but string.ascii_letters.
    Builds a dictionary from list with key=sorted, cleansed string and value(s) a list of all original strings that map to the cleansed string"""
    d = dict()
    for item in l:
        normal_word = normalize_word(item)
        if normal_word not in d:
            d[normal_word] = [item]
        else:
            d[normal_word].append(item)
    return d


if __name__ == '__main__':
    #p_json = 'titles.json'
    #p_json = 'test.json'
    #d = normalize_list( load_json_from_file(p_json) )  
    #p_text = 'text.txt'

    #TO DO: Store created dictionary in dictionary file
    #so I don't have to keep creating it each time
    p_text = 'wiki_title_dl.txt'
    l = load_from_text(p_text)
    d = build_dict(l)
    orig = "iconic hop"
    s = normalize_word( orig )
    if s in d:
        print "String '%s' has anagrams: %s" % (orig, d[s])
        print d[s]
    else:
        print "String '%s' not found" % orig
    




