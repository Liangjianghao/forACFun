# -- coding: UTF-8 -- 
import time
import sys
import os
from lxml import html
import json
import requests
from selenium import webdriver

import sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf8')

def login():
	driver = webdriver.Chrome()
	driver.get("http://www.acfun.cn/login/")
	elemZH = driver.find_element_by_id("ipt-account-login")
	elemZH.send_keys('18621121232')

	elemMM = driver.find_element_by_id("ipt-pwd-login")
	elemMM.send_keys("l31415926")

	loginBtn = driver.find_element_by_class_name("btn-login")
	loginBtn.click()
	time.sleep(3)

	return driver
def idChange(strID):
	newID=strID.split('/')[2]
	newID=newID.replace('ac','')
	# print newID
	header_dict = {'deviceType':'0','market':'appstore','appVersion':'4.7.6'}
	url='https://apipc.app.acfun.cn/v2/videos/%s'%newID
	res = requests.get(url,headers=header_dict).content
	result=json.loads(res)
	print result
	if result:
		return result['vdata']['videos'][0]['videoId']
	# return newID

def fillPage(driver):
	driver.get('http://www.acfun.cn/search/#page=1;query=快速看完一局韩服王者斗殴局;type=video')
	time.sleep(3)
	pageNum=driver.find_element_by_class_name('hint')
	numberPage= pageNum.text.split('/')[1].replace('页','')
	numberPage=int(numberPage)
	print '共有'+str(numberPage)+'页视频'
	proList=[]
	for x in xrange(1,numberPage):
		driver.get('http://www.acfun.cn/search/#page=%s;query=快速看完一局韩服王者斗殴局;type=video'%x)
		time.sleep(2)
		pageNum=driver.find_element_by_class_name('hint')
		print '当前为'+pageNum.text
		selector = html.fromstring(driver.page_source)
		hrefs=selector.xpath('//div[@class="video-cell clearfix"]')

		for href in hrefs:
			proDic={}
			name=href.xpath('div/div[1]/a')
			info = name[0].xpath('string(.)')
			acID=href.xpath('div/div[1]/a/@href')
			newacID=idChange(acID[0])
			print info+'\n'+'番号'+acID[0]+'  '+'弹幕番号：'+str(newacID)
			proDic[info]=newacID
			proList.append(proDic)

		with open("cgrn.json","w") as f:
			f.write(json.dumps(proList,ensure_ascii=False))

driver=login()
fillPage(driver)