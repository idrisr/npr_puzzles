"""
From Michael Arkelian, of Sacramento, Calif.: Name a creature in six letters.
Move the first three letters to the end and read the result backward to name another creature.

Clue: If you break either six-letter word in half, each pair of three letters will themselves spell a word.

http://www.npr.org/templates/story/story.php?storyId=130943907
"""

f_wordlist = '/home/idris/word_lists/CROSSWD.TXT'

def load_dict():
    """load word_list into dictionary
    I should make a dictionary saved on disk instead of always re-loading
    """
    fin = open (f_wordlist)
    d = dict()
    for line in fin:
        word = line.strip().lower()
        if len(word) in (3, 6):
            d[ word ] = None
    return d

def move_letters(word):
    """move first 3 letters of word to end"""
    new_word = word[3:] + word [:3]
    #reverse word
    new_word = new_word[::-1]
    return new_word

def half_words(word):
    """tests to see if each split word is a real word"""

def check_word(word):
    """returns boolean of whether word is in dictionary"""
    return (word in d_dict)

def test_condition(word):
    """test if all conditions for puzzle are true"""
    l = list()
    word2 = move_letters(word)
    l.append( word2 )
    l.append( word[:3] )
    l.append( word[3:])
    l.append( word2[:3])
    l.append( word2[3:])
    for word in l:
        if not check_word(word):
            return False
    return True
    #check if word after moving letter
    #if check_worddd


def main():
    for word in d_dict:
        if test_condition(word):
            print word

if __name__ == '__main__':
    #load only 3 or 6 letter words
    d_dict = load_dict()
    main()
