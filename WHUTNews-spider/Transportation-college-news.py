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
    div = soup.find('div', attrs={'class': 'art_list'})
    for li in div.find_all('li'):
        for i in li.find_all('i'):
            news_date = i.get_text()
        for a in li.find_all('a'):
            news_title = a.get_text()
            news_url = "http://st.whut.edu.cn/tzgg" + a.get('href')[1:]
        n_list.append([news_date, news_title, news_url])


def printNewsList(n_list):
    n_list = n_list[::-1]
    tplt = "{0:^4}\t{1:{3}^20}\t{2:^10}"
    for g in n_list:
        print(tplt.format(g[0], g[1], g[2], chr(12288)))


def main():
    depth = 20
    for i in range(depth, -1, -1):
        news = []
        if i == 0:
            url = 'http://st.whut.edu.cn/tzgg/index.shtml'
        else:
            url = 'http://st.whut.edu.cn/tzgg/index_{}.shtml'.format(str(i))
        try:
            html = getHTMLText(url)
            getNewsList(html, news)
            printNewsList(news)
            print("--------------------------------------------------------")
        except:
            continue


main()
