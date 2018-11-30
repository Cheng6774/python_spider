import urllib2
import urllib
import cookielib
import sys
import os
import json
import time

PostUrl ="http://jxgl.gdufs.edu.cn/jsxsd/xsxkkc/xsxkGgxxkxk?kcxx=&skls=&skxq=&skjc=&sfym=true&sfct=true&szjylb=06&szkclb=13"

headers = {
"Accept":"*/*",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
"X-Requested-With": "XMLHttpRequest",
"Content-Length":"254",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://jxgl.gdufs.edu.cn/jsxsd/xsxkkc/comeInGgxxkxk",
"Origin": "http://jxgl.gdufs.edu.cn",
"Connection":"keep-alive",
"Host": "jxgl.gdufs.edu.cn",
}

cookie_jar = cookielib.MozillaCookieJar()
cookies = open('I:\cookie.txt').read()

for cookie in json.loads(cookies):
    cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))

	
post_data = {}
post_data['sEcho'] = '1'
post_data['iColumns'] = '11'
post_data['sColumns'] = ''
post_data['iDisplayStart'] = '0'
post_data['iDisplayLength'] = '15'
post_data['mDataProp_0'] = 'kch'
post_data['mDataProp_1'] = 'kcmc'
post_data['mDataProp_2'] = 'xf'
post_data['mDataProp_3'] = 'skls'
post_data['mDataProp_4'] = 'sksj'
post_data['mDataProp_5'] = 'skdd'
post_data['mDataProp_6'] = 'xkrs'
post_data['mDataProp_7'] = 'syrs'
post_data['mDataProp_8'] = 'ctsm'
post_data['mDataProp_9'] = 'szkcflmc'
post_data['mDataProp_10 '] = 'czOper'

post_data = urllib.urlencode(post_data)

handler = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(handler)

record = 0
count = 0

while (record == 0) : 
	time.sleep(0.5)
	count = count + 1
	print "#" , count
	request = urllib2.Request(PostUrl, post_data, headers)
	response = opener.open(request)
	json_data = json.load(response)
	record = json_data['iTotalDisplayRecords']
	print "Result:", json_data['iTotalDisplayRecords']
	if (record != 0) :
		print "Course:", json_data['aaData'][0]['kcmc']
		print "ID:", json_data['aaData'][0]['jx0404id']


URL1 = "http://jxgl.gdufs.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id="
URL2 = json_data['aaData'][0]['jx0404id']
URL3 = "&xkzy=&trjf="
ChooseURL = URL1 + URL2 + URL3

ChooseHeader={
"Host": "jxgl.gdufs.edu.cn",
"Connection": "keep-alive",
"Accept": "*/*",
"X-Requested-With": "XMLHttpRequest",}

request2 = urllib2.Request(ChooseURL,'', ChooseHeader)
response2 = opener.open(request2)
json_data2 = json.load(response2)
print "Result:",json_data2['success']
print "Message:",json_data2['message']