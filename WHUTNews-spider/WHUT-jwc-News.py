# -*- coding: utf-8 -*-
import string
import urllib.request, urllib.error, urllib.parse
import re
import time
import smtplib
from email.mime.text import MIMEText
import chardet   #需要导入这个模块，检测编码格式


# mailto_list = ['306578968@qq.com']	# 收件人，多个收件人用逗号隔开
# mail_host = 'smtp.gmail.com'
# mail_user = ''				# 发件人
# mail_pass = ''				# 发件人密码

# def send_mail(to_list, sub, content):
#     msg = MIMEText(content, _subtype = 'html', _charset = 'utf-8')
#     msg['Subject'] = sub
#     msg['From'] = mail_user
#     msg['To'] = ';'.join(to_list)
#     try:
#         s = smtplib.SMTP()
#         s.connect(mail_host)
#         s.ehlo()
#         s.starttls()
#         s.login(mail_user, mail_pass)
#         s.sendmail(mail_user, to_list, msg.as_string())
#         s.close()
#         return True
#     except Exception as e:
#         print(str(e))
#         return False

def GetNews():
    url = 'http://jwc.whut.edu.cn/'
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req).read()
    p = re.compile(r'<a class="pad_left" href="(.*?)" title=".*?">(.*?)</a><span class="pad_right" >(.*?)</span>')
    encode_type = chardet.detect(page)  
    page = page.decode(encode_type['encoding']) #进行相应解码，赋给原标识符（变量）
    items = p.findall(page)
    news = []
    for item in items:
        # if(item[2] == time.strftime('%Y-%m-%d',time.localtime(time.time()))):  #查询当天的新闻则开启if语句
            news.append([item[0], item[1], item[2]])
    return news

news = GetNews()
if news:
    sub = 'WHUT教务处最新通知推送（Anotherhome提供）' + time.strftime('%Y-%m-%d',time.localtime(time.time()))
    content = 'WHUT最新通知:<br><br>'
    for item in news:
        content += item[2]
        print(item[2],'\n')
        content += '  '
        content += item[1]
        content += '  '
        print(item[1],'\n')
        content += item[0]
        print(item[0],'\n')
        content += '<br>'
        content += ' （校内资源，请用校园网或VPN访问）  <br><br> 推送服务由<a href="http://www.anotherhome.net/" target="_blank">Anotherhome</a>提供. 代码托管在<a href="https://github.com/DIYgod/WHUTNews" target="_blank">Github</a>上.'
    # if send_mail(mailto_list, sub, content):
    #     print('Succeed')
    # else:
    #     print('Fail')
else:
    print('None')


