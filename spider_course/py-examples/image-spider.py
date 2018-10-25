# image-spider

# author = cheng

import requests
import os

url = "http://image.nationalgeographic.com.cn/2017/1113/20171113035359678.jpg"

root = "D://pics//"

path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('success')
    else:
        print('already exist')
except:
    print('error')

# import requests
# import os
# url = "https://pic1.zhimg.com/v2-a97a2f2855511a61b5abdec3131c6f7c_b.jpg"
# root = "E://pics//"
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path,'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")
    
