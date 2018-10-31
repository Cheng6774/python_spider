import requests
from bs4 import BeautifulSoup
import re
import csv
import xlsxwriter


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
            news_date = re.sub(r'\s', '', span.get_text())
        for a in li.find_all('a'):
            news_title = re.sub(r'\s', '', a.get_text())
            news_url = "http://scc.whut.edu.cn/" + a.get('href')
        n_list.append([news_date, news_title, news_url])


def printNewsList(n_list):
    n_list = n_list[::-1]
    tplt = "{0:^4}\t{1:{3}^35}\t{2:^20}"
    for g in n_list:
        print(tplt.format(g[0], g[1], g[2], chr(12288)))


def writeCSV(n_list):
    with open('学校就业新闻.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["日期", "标题", "链接"])
        writer.writerows(n_list)


def writeXLS(n_list):
    wb = xlsxwriter.Workbook('学校就业新闻.xlsx')
    sh = wb.add_worksheet('A Test Sheet')
    sh.set_column('A:A', 20)
    sh.set_column('B:C', 80)
    row = 0
    col = 0
    for date, title, url in n_list:
        sh.write(row, col, date)
        sh.write(row, col + 1, title)
        sh.write(row, col + 2, url)
        row += 1
    wb.close()


def main():
    depth = 3
    total_news = []
    for i in range(depth, 0, -1):
        page_news = []
        url = 'http://scc.whut.edu.cn/infoList.shtml?tid=1001&searchForm=&pageNow={}'.format(
            i)
        try:
            html = getHTMLText(url)
            getNewsList(html, page_news)
            total_news = page_news + total_news
            printNewsList(page_news)
            print("--------------------------------------------------------第"\
            ,i,"页输出完毕-------------------------------------------------")
        except:
            continue
    writeCSV(total_news)
    writeXLS(total_news)

main()
