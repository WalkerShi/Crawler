import HTMLParser
import urllib2
import urllib
import sys
import cookielib
from bs4 import BeautifulSoup

user_len = 300000;
url = 'http://csn.cancer.org/user/';

def Brower(idx, url, fp):
    login_page = "http://csn.cancer.org/user/login"
    try:
        cj = cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        data = urllib.urlencode({"name":'ilve',"pass":'102938',
        'form_build_id':'form-Zjp8IwDxddX39TCoTkM4ipJ01yePsBvcWK1UX22SNL8',            
        'form_id':'user_login',
        'op':'Log+in'
        })
        opener.open(login_page,data)
        op=opener.open(url)
        data= op.read()
        
        nPos = data.index('<title>') + 7
        nPosr = data.index(' |')
        username = data[nPos: nPosr]
        if (username == 'Access Denied'): return;

        nPos = data.index('<dt>Joined on</dt>') + len('<dt>Joined on</dt>') + 5;
        Join = "";
        for i in range(nPos, 1000000, 1):
            if (data[i] == '<'): break
            Join += data[i]

        nPos = data.index('<dt>Last online</dt>') + len('<dt>Last online</dt>') + 5;
        Last = "";
        for i in range(nPos, 100000, 1):
            if (data[i] == '<'): break
            Last += data[i]
            
        Age = 'Not Record'
        try:
            nPos = data.index('<dt>Age Range</dt>')
            nPos += len('<dt>Age Range</dt>') + 5
            Age = ""
            for i in range(nPos, 100000, 1):
                if (data[i] == '<'): break
                Age += data[i]
        except Exception,e:
            a = 1

        fp.write(username + '\t' + Join + '\t' + Last + '\t' + Age + '\n')
        print idx

        fpp = open('D:\\cornell\\user\\' + username + '.txt', 'w');
        fpp.write(data)
        
    except Exception,e:
        print str(e)
    
def user(fp, name):
    print name;
    for l in range(100):
        try:
            urlText = urllib2.urlopen(name, timeout = 30)
            content = urlText.read()
        except :
            continue
        break
    fp.write(content)
    
def main():
    fp = open("userlist00.txt", "w");
    for i in range(0, 5000, 1):
        Brower(i, url + str(i), fp);
    #for i in range(1): #
    #    user(fp, "http://csn.cancer.org/member/search/pg%253A1%252C2?page=" + str(i));
        
main()
