# -*- coding: utf-8 -*-
import string
import requests
import re
import time
import smtplib

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def GetNews(html,JList): 
    p = re.compile(
        r'<li><span>(.*?)</span><a href="(.*?)">(.*?)</a></li>'
        )
    items = p.findall(html)
    for item in items:
        # if(item[2] == time.strftime('%Y-%m-%d',time.localtime(time.time()))):  #查询当天的新闻则开启if语句
        JList.append([item[0], item[1], item[2]])
    return JList


def main():
    jobUrl = 'http://scc.whut.edu.cn/infoList.shtml?tid=1001'
    jobHtml = getHTMLText(jobUrl)
    jobList = []
    GetNews(jobHtml,jobList)
    print(jobList)

main()

# if news:
#     sub = 'WHUT教务处最新通知推送（Anotherhome提供）' + time.strftime(
#         '%Y-%m-%d', time.localtime(time.time()))
#     content = 'WHUT最新通知:<br><br>'
#     for item in news:
#         content += item[2]
#         print(item[2], '\n')
#         content += '  '
#         content += item[1]
#         content += '  '
#         print(item[1], '\n')
#         content += item[0]
#         print(item[0], '\n')
#         content += '<br>'
#         content += ' （校内资源，请用校园网或VPN访问）  <br><br> 推送服务由<a href="http://www.anotherhome.net/" target="_blank">Anotherhome</a>提供. 代码托管在<a href="https://github.com/DIYgod/WHUTNews" target="_blank">Github</a>上.'
#     # if send_mail(mailto_list, sub, content):
#     #     print('Succeed')
#     # else:
#     #     print('Fail')
# else:
#     print('None')