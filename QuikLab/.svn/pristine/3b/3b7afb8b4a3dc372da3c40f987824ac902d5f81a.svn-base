#! /usr/bin/env python
#coding=GB18030
from datetime import datetime
import os
import shutil
import threading
import time
import unittest
import allcase


import casebase.HTMLTestRunner as HTMLTestRunner
import casebase.get_usage as cpuUsage
import casebase.init as init


def start():
    testunit = unittest.TestSuite()
    alltestnames = allcase.caseData()
    print "All test case name are:",alltestnames
    for test in alltestnames:
        testunit.addTest(unittest.makeSuite(test))
    
    now = time.strftime("%Y%m%d%H%M%S",time.localtime())
    filedir =  os.getcwd() + r'\report'
    if not os.path.exists(filedir):
        os.chdir('../')
        filedir=os.getcwd() + r'\report'
#     print filedir
    file_dir = filedir + r'\result' + now 
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)      #时间作为文件夹名创建文件夹
      
    fileUrl = filedir + r'\result' + now +".html" 
    fp = file(fileUrl ,'wb')
#     print fileUrl
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'QuikLab3.0自动化测试报告',description=u'QuikLab3.0自动化测试报告')
    runner.run(testunit)
    fp.close()
    time.sleep(5)
    fileNames = os.listdir(filedir)
    for fileName in fileNames:
        if os.path.isfile(os.path.join(filedir,fileName)):          #如果是文件移动至最新的目录下
            if os.path.splitext(fileName)[1] != ".py":
                fp = os.path.join(filedir,fileName)
                shutil.move(fp, file_dir)
        elif os.path.isdir(os.path.join(filedir,fileName)):         #如果是目录删除一周之前的记录
            filedate = os.path.getmtime(os.path.join(filedir,fileName))        #获取到目录的修改时间戳单位为秒
            data = time.time()          #获取当前的时间戳
            num = (data - filedate)/60/60/24      #60s,60m,2h时间戳转换为天
            if num >= 7:
                try:
                    shutil.rmtree(os.path.join(filedir,fileName))  #删除一周之前的目录                 
                except Exception as e:
                    print(e) 
init._init()                    
threads=[]
t1 = threading.Thread(target=start)
threads.append(t1)
t2 = threading.Thread(target=cpuUsage.get_usage)
threads.append(t2)
for t in threads:
#     print t.getName()
    t.setDaemon(True)
    t.start()
for n in threads:
    n.join()
    
