import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getNewsList(html, n_list):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('ul', attrs={'class': 'col_con_list'})
    for li in ul.find_all('li'):
        for span in li.find_all('span'):
            news_date = re.sub(r'\s','',span.get_text())
        for a in li.find_all('a'):
            news_title = re.sub(r'\s','',a.get_text())
            news_url = "http://scc.whut.edu.cn/" + a.get('href')
        n_list.append([news_date, news_title, news_url])


def printNewsList(n_list):
    n_list = n_list[::-1]
    tplt = "{0:^5}\t{1:{3}^25}\t{2:^10}"
    for g in n_list:
        print(tplt.format(g[0], g[1], g[2],chr(12288)))


def main():
    depth = 2
    for i in range(depth, 0, -1):
        news = []
        url='http://scc.whut.edu.cn/infoList.shtml?tid=1001&searchForm=&pageNow={}'.format(i)
        try:
            html = getHTMLText(url)
            getNewsList(html, news)
            printNewsList(news)
            print("--------------------------------------------------------")
        except:
            continue


main()
