# -- coding: UTF-8 -- 
import requests
import json
import sys
from selenium import webdriver
reload(sys)
# with open('1.json') as json_file:
def returnId(idStr):
	header_dict = {'deviceType':'0','market':'appstore','appVersion':'4.7.6'}
	res = requests.get("https://apipc.app.acfun.cn/v2/videos/%s"%idStr,headers=header_dict).content
	result=json.loads(res)
	print result
	print result['vdata']['videos'][0]['videoId']
	return result['vdata']['videos'][0]['videoId']

strN='1809298'
danmuID=returnId(strN)
danmuUrl='http://danmu.aixifan.com/V4/%s/0/500'%danmuID
print danmuUrl
response=requests.get(danmuUrl).content
print response