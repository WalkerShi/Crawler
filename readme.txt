As we all know, building a good dataset is the key issue for our research.
We need an efficient and robust crawler for our project when suitable dataset 
doesn't exist. I share my crawler here and briefly talk about how to write a
crawler. Generally speaking, this issue depends on the website's structure.

'crawler_cancer.py' is written for crawling user's information from 
'csn.cancer.org'. This website requires an account to see the contents. So we 
have to mimic user's action to log in. In this case, we use cookie 
corresponding to line14 - line24 in the program.
'opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]'
means our program is disguised as a browser called 'Mozilla'. It is designed 
to misguide the website. And later in 'data = urllib.urlencode(...)', we should 
fill in username, password and other things. We can find what is needed through
the real browser when we open the url. Till now, we've gotten a page. There are two
ways to preprocess this page. One way is to use a python lib called 
'beautiful soup'(https://www.crummy.com/software/BeautifulSoup/bs4/doc/), the other
way is to write code by ourselves. Personally speaking, I prefer the second way
because of its flexibility and simplicity. Website is well-structured usually containing
fixed signal before the information we want to crawl. 'index' function in python is
enough in this case. By mentioning flexibility, I believe you will understand me if you
used 'beautiful soup' before.
 
Meanwhile, maybe you have noticed that a parameter called 'timeout' in
'urlText = urllib2.urlopen(name, timeout = 30)'. The reason to introduce this one is 
to avoid the error from Internet. For the same purpose, we have to repeat this line 
for several times if we don't want to lose anything. 

The next problem is that some websites have automatic recognition system which protect 
themselves from attacking. If you directly execute a crawler, maybe your ip will be 
blocked. A generally strategy is waiting for a random time period(in second level)
after each crawling operation. And remember to change you ip frequently if possible.
It will greatly decrease the probability to be blocked.

By the way, please save what you have crawled if you don't want to restart everything
from the beginning when emergency occurs.

'crawlplus_archive.py' is about how to crawl archives from wiki. It is very similar to
'crawler_cancer.py'. The unique technique used in this program is that it splits the
whole tasks into several parts. Therefore, we can run them simultaneously. The solution
I use here is very simple. I use a variable, which is added by one in each round, to
record the index of the url we want to crawl. If this index is out of our concerning
boundary, just skip this operation and it will be done by another program.

If you have any questions, please be free to contact with me. :D

Walker Shi(Hanyuan Shi)
email: shihanyuan@sjtu.edu.cn
  