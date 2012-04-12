# Computer aided solution to Will Short NPR puzzle originally aired on 
# 12/19/2010 at http://www.npr.org/2010/12/19/132170541/a-cut-above-average
#-------------------------------------------------------------------------------------
# Name a city in the United States that ends in the letter S. The city is one of the largest cities in its state. 
# Change the S to a different letter and rearrange the result to get the state the city is in. What are the city and state?
#-------------------------------------------------------------------------------------

import os
import string
from lxml import etree

"""
url = "http://en.wikipedia.org/wiki/List_of_U.S._states'_largest_cities_by_population"
fp = os.popen("wget %s" % (url,))
"""

#HTML Parser
p = etree.HTMLParser()

#open saved wikipedia page
f = open('city.html', 'r')

#Create Element Tree Object from webpage
tree = etree.parse(f, parser=p)

#XPath selectors
xps1 = '//table[@class="wikitable"]//tr'
xps2 = './/td//a/text()'

d_states = dict()

rows = tree.xpath(xps1)

for row in rows:
    cols = row.xpath(xps2)
    if len(cols):
        state = cols[0]
        cities = cols[1:6]
        d_states[state] = cities

def rem_spaces(word):
    """takes 'word' and returns all non-ascii_letters from 'word'"""
    return ''.join( [ char for char in word if char in string.ascii_letters] )

def test_words(word1, word2):
    """tests if word1 and word2 are the same length"""
    word1 = rem_spaces( word1 )
    word2 = rem_spaces( word2 ) 
 
    return len(word1)==len(word2) and len(word1) == 7

for state in d_states:
    cities = d_states[state]
    for city in cities:
        if test_words(city, state):
            print city, state


