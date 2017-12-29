# -- coding: UTF-8 -- 
import requests
import json
import os
import sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf8')

f=open('cgrn.json')
data = json.load(f)
for pro in data:
	for k in pro:
		print k
		print pro[k]
		path='/Users/l/Desktop/cgrn/%s'%k
		isExists=os.path.exists(path)
		if not isExists:
			os.makedirs(path)
			print path+'创建成功'
		else:
			print '目录已存在'
		danmuUrl='http://danmu.aixifan.com/V4/%s/0/500'%pro[k]
		print danmuUrl
		response=requests.get(danmuUrl).content
		danmuArr=json.loads(response)
		danmuNum= len(danmuArr[2])
		# print response
		# with open("%s/%s条弹幕.json"%(path,danmuNum),"w") as f:
		with open("%s/danmu.json"%(path),"w") as f:
			f.write(json.dumps(danmuArr,ensure_ascii=False))


  