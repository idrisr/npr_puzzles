from lxml import etree
"""
Name a nationality. The third, fourth, fifth, sixth and 10th letters in order name a country.
Also the fourth, fifth, seventh, ninth and 12th letters in order also name a country.
Neither country is related to the nationality. What nationality is this?
"""

import string
def get_chars(l_index, word):
    """returns l_indexth characters of string 'word'
    contents of 'l_index' are expected to be 1 indexed for ease"""
    new_word = ''
    try:
        for i in l_index:
            new_word+= word[i-1]
        return new_word
    except:
        return None

def no_space_lower(s):
    s = ''.join([char for char in s.lower() if char not in string.whitespace])
    return s

p_nat = 'List_of_nationalities'
f_nat = open(p_nat, 'r') 

p = etree.HTMLParser()
tree = etree.parse(f_nat, parser=p)

"""Why doesn't this xpath return anything???"""
#xp_countrys= '//table[@id="sortable_table_id_0"]//tr'

"""Take opp to learn more about xpaths
1) like why do they return lists and can this be controlled
2) how to specify not certain tags
"""

xp_countrys= '//table[@class="wikitable sortable"]//tr'
xp_country = './td[1]//text()'
xp_adj     = './td[2]//text()'
countrys = tree.xpath(xp_countrys)

d_adj = dict()
d_name = dict()

l_country1 = [ 3, 4, 5, 6, 10]
l_country2 = [ 4, 5, 7, 9 ,12]

for country in countrys:
    names = country.xpath(xp_country)
    adjs  = country.xpath(xp_adj)
    if names and adjs:
        for adj in adjs:
            d_adj[no_space_lower(adj)] = None
        for name in names:
            d_name[no_space_lower(name)] = None

for adj in d_adj:
    if len(adj)>=12:
        splice1 = get_chars(l_country1, adj) 
        splice2 = get_chars(l_country2, adj)
        #print '%s\t %s\t %s\t' % (splice1, splice2,adj )

def country_combo(c1, c2):
    pass    

l=list()
for name in d_name:
    if len(name)==5:
        l.append(name)
