import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getNewsList(html):
    soup = BeautifulSoup(html,'html.parser')
    tag_div = soup.find('div', attrs={'class': 'art_list'})
    for a in tag_div.find_all('a'):
        news_title = a.get_text()
        news_url = a.get('href')
        news_url = "http://st.whut.edu.cn/tzgg"+ news_url[1:]
        print (news_title,'\n',news_url,'\n')

def printNewsList():
        pass


def main():
    url = 'http://st.whut.edu.cn/tzgg/'
    html = getHTMLText(url)
    getNewsList(html)

main()
