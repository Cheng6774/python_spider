# ip-address

# author = cheng

import requests

url = "http://m.ip138.com/ip.asp?ip="

try:
    r = requests.get(url + '202.120.2.119')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('error')

