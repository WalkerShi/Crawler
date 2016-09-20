import HTMLParser
import urllib2
import urllib
import sys
import cookielib
import os

user_len = 1;
url = 'https://en.wikipedia.org/wiki/Talk:';
cnt = 0
total = 0
urls = 'data//'

def Brower(url):
    where = ''
    print url
    try:
        for l in range(5):
            try:
                urlText1 = urllib2.urlopen(url, timeout = 30)
                content1 = urlText1.read()
            except :
                continue
        fp = open('1.html', 'w')
        data = content1
        fp.write(data)
    except :
        return 0

dhh = 0

def number(url):
    n = len(url)
    for i in range(n):
        if (url[i] >= '0' and url[i] <= '9'):
            return 1
    return 0

def go(url, idx):
    print url
    pos = url.index('Archive') + len('Archive')
    if (number(url[pos : len(url)]) == 0): return 0
    url = 'https://en.wikipedia.org' + url
    print url
    global dhh
    dhh += 1
    add = 'archives//' + str(idx) + '@' + str(dhh) + '.html'
    print add
    try:
        for l in range(5):
            try:
                urlText1 = urllib2.urlopen(url, timeout = 30)
                content1 = urlText1.read()
            except e:
                continue
        fp = open(add, 'w')
        data = content1
        fp.write(data)
    except :
        return 0
        
def through(lll):
        fp = open('list' + str(lll + 1) + '.txt', 'r')
        alines = fp.readlines()
        #print len(lines)
        xxx = 0
        #print lines[0]
        for i in range(lll * 300000, (lll + 1) * 300000):
            if (i % 1000 == 0): print i
            add = 'new//' + str(i) + '@0.html'
            fp = open(add, 'r')
            data = ''
            lines = fp.readlines()
            for line in lines:
                data += line
            #print data
            #print xxx
            aline = alines[xxx]
            #print aline
            xxx += 1
            interest = url + aline[6:len(aline)-1] + '/Archive'
            #print interest
            interest = interest.replace('https://en.wikipedia.org/wiki/Talk:', '/wiki/Talk:')
            #print interest
            global dhh
            dhh = 0
            for j in range(1000):
                try:
                    pos = data.index(interest)
                    print pos
                    data = data[pos : len(data)]
                    shy = data[0 : len(interest)]
                    for k in range(len(interest), 1000000, 1):
                        if (data[k] == '"'): break
                        shy += data[k]
                    data = data[1 : len(data)]
                    go(shy, i)
                    
                except:
                    aaa = 1
                
def main():
    #new = Brower(url)
    fp = open('shy.txt', 'r')
    lines = fp.readlines()
    l = int(lines[0])
    fp.close()
    l += 1
    fp = open('shy.txt', 'w')
    fp.write(str(l))
    fp.close()
    
    through(l - 1)
    
main()
