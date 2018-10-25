# baidu-spider

# author = cheng

import requests

keyword = 'python'
url = "http://www.baidu.com/s"

try:
    kv = {'wd':keyword}
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('error')

# import requests as rq
# keyword = "python"
# url = "http://www.baidu.com/s"
# try:
#     kv = {'wd':keyword,'userageent':'Mozilla/5.0'}
#     r = rq.get(url,params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")

# keyword = "python"
# url = "http://www.so.com/s"
# try:
#     kv = {'wd':keyword}
#     r = rq.get(url,params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")
