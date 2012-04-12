import lxml.html
import re
import urllib2

def get_url(url):
    '''get_url accepts a URL string and return the server response code, response headers, and contents of the file'''

    ''' spoofs a firefox browswer'''
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

if __name__ == '__main__':
    url_base = 'http://en.wikipedia.org/wiki/List_of_national_capitals'
    contents = get_url(url_base)



