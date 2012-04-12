from BeautifulSoup import BeautifulSoup
import re

fin = '/home/idris/work/npr_puzzle/11_14_nt/aa.txt'
f = open(fin, 'r')
text =''
for line in f:
    text += line

soup = BeautifulSoup(text)

titles= soup.findAll('a', title=re.compile('Aa'))

for item in titles:
    print item['title']
            


