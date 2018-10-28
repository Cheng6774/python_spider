import requests
from bs4 import BeautifulSoup
import re
import csv


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
            news_date = re.sub(r'\s','',i.get_text())
        for a in li.find_all('a'):
            news_title = re.sub(r'\s','',a.get_text())
            news_url = "http://st.whut.edu.cn/tzgg" + a.get('href')[1:]
        n_list.append([news_date, news_title, news_url])

def printNewsList(n_list):
    tplt = "{0:^4}\t{1:{3}^35}\t{2:^20}"
    for g in n_list:
        print(tplt.format(g[0], g[1], g[2], chr(12288)))


def writeCSV(n_list):
    with open ('交通学院新闻.csv','w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["日期","标题","链接"])
        writer.writerows(n_list)


def main():
    depth = 3
    total_news = []
    for i in range(depth, -1, -1):
        page_news = []
        if i == 0:
            url = 'http://st.whut.edu.cn/tzgg/index.shtml'
        else:
            url = 'http://st.whut.edu.cn/tzgg/index_{}.shtml'.format(str(i))
        try:
            html = getHTMLText(url)
            getNewsList(html, page_news)
            total_news =  page_news + total_news
            print("--------------------第",i+1,"页输出完毕------------------------------------")
        except:
            continue
    printNewsList(total_news)
    writeCSV(total_news)
    
main()
