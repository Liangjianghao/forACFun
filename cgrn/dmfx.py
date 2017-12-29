# -*- coding: utf-8 -*-

import os
import sys
import re
import json
import requests
from lxml import html
import  xml.dom.minidom
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
reload(sys)
sys.setdefaultencoding('utf8')

mylist=[]
path='/Users/l/Desktop/cgrn'
nameList=os.listdir(path)
for filename in nameList:
    filepath=path+'/'+filename
    if filepath==path+'/.DS_Store':
        continue
    
    print filepath
    jsonPath='%s/danmu.json'%filepath
    print jsonPath
    data=[]
    with open(jsonPath,'r') as json_file:
        data = json.load(json_file)

    print len(data)
    damuArr=data[2]
    print damuArr
    listTime=[]
    hahalistTime=[]
    for href in damuArr:
        if  href is None:
            continue
        else:
            KeyList=['6','高能','鬼鬼','秀']
            if any(keyWord in href['m'] for keyWord in KeyList):
                time=href['c']
                timeStr=str(time.split(',')[0])
                if '.' in timeStr:
                    flist=timeStr.split('.')
                    hahalistTime.append(flist[0])

            time=href['c']
            timeStr=str(time.split(',')[0])
            if '.' in timeStr:
                flist=timeStr.split('.')
                listTime.append(flist[0])
    hahaumbers = map(int, hahalistTime)
    hahaumbers.sort()
    print hahaumbers

    numbers = map(int, listTime)
    numbers.sort()
    print numbers
    setNumbers=set(numbers)

    alist=[i for i in setNumbers]
    alist.sort()

    timeR=[i for i in range(0,max(alist))]
    blist=[]
    halist=[]
    for time in timeR:
        itermCount=numbers.count(time)
        haitermCount=hahaumbers.count(time)
        blist.append(itermCount)
        halist.append(-haitermCount)
    print(timeR)
    print(blist)
    print(halist)
    newtimeR=[]
    newblist=[]
    newhalist=[]

    for numbers in timeR:
        m,s=divmod(numbers,60)
        h,m=divmod(m,60)
        timeStr="%02d:%02d:%02d" % (h, m, s)
        # print(timeStr)
        newtimeR.append(timeStr)
    print newtimeR

    import webbrowser

    GEN_HTML = "danmu.html"

    f = open('%s/%s'%(filepath,GEN_HTML),'w')
    list=[1,2,3,4,5,6]
    message = '''<!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>ECharts</title>
    </head>
    <body>
        <div id="main" style="height:400px"></div>
        <script src="http://echarts.baidu.com/build/dist/echarts-all.js"></script>
        <script type="text/javascript">
            var myChart = echarts.init(document.getElementById('main'));
            var option = {
                title : {
                    text: '弹幕变化',
                },
                tooltip : {
                    trigger: 'axis'
                },
                legend: {
                    data:['弹幕数','高能数']
                },
                toolbox: {
                    show : true,
                    feature : {
                        mark : {show: true},
                        dataView : {show: true, readOnly: false},
                        magicType : {show: true, type: ['line', 'bar']},
                        restore : {show: true},
                        saveAsImage : {show: true}
                    }
                },
                calculable : true,
                xAxis : [
                    {
                        type : 'category',
                        boundaryGap : false,
                        data : %s
                    }
                ],
                yAxis : [
                    {
                        type : 'value',
                        axisLabel : {
                            formatter: '{value}'
                        }
                    }
                ],
                series : [
                    {
                        name:'弹幕最大值',
                        type:'line',
                        data:%s,

                    },
                    {
                        name:'高能最大值',
                        type:'line',
                        data:%s,
                    }
                ]
            };
            // 为echarts对象加载数据
            myChart.setOption(option);
        </script>
    </body>'''%(newtimeR,blist,halist)

    f.write(message)
    f.close()
    # webbrowser.open(GEN_HTML,new = 1)



