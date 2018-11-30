import requests
from bs4 import BeautifulSoup
import re
import csv
import xlsxwriter


def getHTMLText(url):
    try:
        kv = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0/ROY TOOL'
        }
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getNewsList(html, n_list):
    soup = BeautifulSoup(html, 'lxml')
    ul = soup.find('ul', attrs={'class': 'col_con_list'})
    for li in ul.find_all('li'):
        for span in li.find_all('span'):
            news_date = re.match(r'[【](.*?)[】]', span.get_text())
            news_date = news_date.group(1)
        for a in li.find_all('a'):
            news_subject = re.match(r'[【](.*?)[】]', a.get_text())
            news_subject = news_subject.group(1)
            news_company = re.match(r'[【].*[】](.*)', a.get_text())
            news_company = news_company.group(1)
            news_url = "http://scc.whut.edu.cn/" + a.get('href')
        n_list.append([news_date, news_subject, news_company, news_url])


def printNewsList(n_list):
    n_list = n_list[::-1]
    tplt = "{0:^4}\t{1:{4}^10}\t{2:^30}\t{3:^35}"
    for g in n_list:
        print(tplt.format(g[0], g[1], g[2], g[3], chr(12288)))


def writeCSV(n_list):
    with open('学校就业新闻.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["日期", "行业", "公司", "链接"])
        writer.writerows(n_list)


def writeXLS(n_list):
    wb = xlsxwriter.Workbook('学校就业新闻.xlsx')
    sh = wb.add_worksheet('A Test Sheet')
    sh.set_column('A:B', 20)
    sh.set_column('C:D', 80)
    row = 0
    col = 0
    for date, subject, company, url in n_list:
        if row == 0:
            sh.write(0, 0, "日期")
            sh.write(0, 1, "行业")
            sh.write(0, 2, "公司")
            sh.write(0, 0, "链接")
        sh.write(row, col, date)
        sh.write(row, col + 1, subject)
        sh.write(row, col + 2, company)
        sh.write(row, col + 3, url)
        row += 1
    wb.close()


def main():
    depth = 2
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
