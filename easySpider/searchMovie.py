# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
import shutil
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')

def analyUrl(name):
	url='http://www.btrabbit.cc/search/%s.html'%name
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//div[@class="search-item detail-width"]')
	sourcelist=[]
	if len(hrefs)>0:
		href=hrefs[0]
		for x in hrefs:
			name=x.xpath('div[@class="item-title"]/h3/a/@title')
			nameStr=''
			nameStr=nameStr+name[0]
			detail=href.xpath('div[@class="item-bar"]/a/text()')
			if detail:
				nameStr=nameStr+detail[0]
			sourcelist.append(nameStr)
			downUrl=x.xpath('div[@class="item-bar"]/a/@href')
			sourcelist.append(downUrl[0])
			# print len(sourcelist)
			if len(sourcelist)==2:
				break

	return sourcelist
def searchFH(name):
	seedstr = '\n'.join(analyUrl(name))
	return	seedstr
if __name__ == '__main__':
	print searchFH('守法公民')
