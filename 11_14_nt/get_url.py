import urllib2
from BeautifulSoup import BeautifulSoup
import re

def get_url(url):
    '''get_url accepts a URL string and return the server response code, response headers, and contents of the file'''
    req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13',
    'Referer': 'http://python.org'}

    request = urllib2.Request(url, headers=req_headers) # create a request object for the URL
    opener = urllib2.build_opener() # create an opener object
    response = opener.open(request) # open a connection and receive the http response headers + contents

    code = response.code
    headers = response.headers # headers object
    contents = response.read() # contents of the URL (HTML, javascript, css, img, etc.)
    
    return code, headers, contents

def get_url_list(f):
    fout = open(f, 'r')
    l = list()
    for line in fout:
        l.append(line.strip())
    return l
    
def make_url(base, s):
    """takes base wikipedia string and appends two chars"""
    return base+s

def save_files(base_url, l):
    """takes list of chars to append to wikipedia url and saves all files""" 
    
    #create list of urls to fetch
    l_urls = list()
    for item in l:
        l_urls.append( ( make_url(base_url, item), item ) )

    #save url to file
    #for item in l_urls:
    for item in l_urls:

        #for testing only
        #if l_urls.index(item) > 5: break

        #file path to dump html
        f = '/home/idris/work/npr_puzzle/11_14_nt/dumps/'+item[1]+'.txt'

        #get contents of web page
        text = get_url( item[0] )[2]

        #prettify and save html of web page
        soup = BeautifulSoup(text)

        titles= soup.findAll('a', title=re.compile(item[1]) )

        fout = open(f, 'w')

        for title in titles:
            try:
                fout.write( title.string + '\n')
            except:
                fout.write('error' + '\n')

if __name__ == '__main__':
    base_url = 'http://en.wikipedia.org/wiki/Special:AllPages/'
               'http://en.wikipedia.org/w/index.php?title=Special:AllPages&from=ASCII+ART'    
    f = '/home/idris/work/npr_puzzle/11_14_nt/urls.txt'
    l_urls = get_url_list(f)
    save_files(base_url, l_urls)
