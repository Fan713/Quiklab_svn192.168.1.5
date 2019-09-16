#! /usr/bin/env python
#coding=GB18030
import ctypes
import json
import os
import re
import sys
import time

import logging

import data

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(Levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w'
                    )
class Logger(object):
    def __init__(self,fileN='Default.log'):
        self.terminal=sys.stdout
        self.log=open(fileN,'w')
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
sys.stdout=Logger('1.txt')
data=data.check()
os.chdir(r"D:\QuiKLab3.0")
lib = ctypes.cdll.LoadLibrary(r"D:\QuiKLab3.0\QuiKLabAPI.dll")
# temp='s'*128
# lib.getAppPath(temp)
# print '-------------------------',temp
# time.sleep(5)
print "初始化QuiKLab平台类:\n",lib.initQuiKLabPlatform()
time.sleep(5)
print("获取下位机数量:\n"),lib.getTargetCount()
print("根据索引获取下位机IP:")
IP="iP"*64
lib.getTargetIP(0,IP,len(IP))
print(IP)
a='\x00' #C语言中的空格
print"根据索引获取下位机状态:\n",lib.getTargetState(0)
print "更新硬件资源信息:\n",lib.updateInterfInfos()
num=lib.getInterfNumFromIp(IP)
print '根据ip获取板卡类型个数:\n',num
interName="s"*128
info="s"*128
print "*"*20
for i in range(num):
    lib.getInterfInfo(IP,i,interName,len(interName),info,len(info))
    print '板卡名称:',interName.strip(a)
    print '板卡信息:',info.strip(a)
    print "*"*20

print "获取当前平台的工程数量:\n",lib.getProjectCount()
p_Num=lib.getProjectCount()
cmd='SELECT Name FROM mydb.tbl_project order by Name; '
_list=data.search(cmd)
# print json.dumps(_list[142][0],encoding='utf-8',ensure_ascii=False)
print (len(_list))
if int(p_Num) == int(len(_list)):
    print('获取当前平台的总工程数量测试结果：Pass')
else:
    print('获取当前平台的总工程数量测试结果：Fail')
pN="s"*128
p=[]
# lib.getProjectName(1,pN,len(pN))

for i in range(p_Num):      #查询所有工程名称
    lib.getProjectName(i,pN,len(pN))
    print pN
    p.append(pN.split(a)[0])    #过去输出字符串中的a(空格)
#     print(json.dumps(_list[i][0],encoding='utf-8',ensure_ascii=False).strip('"').encode('GB18030'))
    if pN.split(a)[0] == json.dumps(_list[i][0],encoding='utf-8',ensure_ascii=False).strip('"').encode('GB18030'):
        flag=0
    else:
        print type(pN.split(a)[0]),type(json.dumps(_list[i][0],encoding='utf-8',ensure_ascii=False).strip('"'))
        flag=1
        break
if flag==0:
    print('工程名称获取测试结果:Pass')
else:
    print('工程名称获取测试结果:Fail')
# print repr(p).decode('string_escape')  #能够输出中文
time.sleep(5)

print "加载工程:\n",lib.loadProject('1111')

#测试用例
print "获取当前工程的测试用例分类数量:\n",lib.getTestCaseClassCount()

classN='s'*128
lib.getTestCaseClassName(0, classN, len(classN))
print "根据索引，获取分类下的测试用例类名称:\n",classN.strip(a)

pn = "s"*128;
lib.getProjectName(1,pn,len(pn))
print "索引为'1'的工程名称:\n", pn.strip(a)

cpn="s"*128
lib.getCurrentProjectName(cpn,len(pn))
print "当前工程的名称:\n",cpn.strip(a)

print "获取测试用例集的测试用例数量:\n",lib.getTestCaseCount(classN)
 
caseName='s'*128
lib.getTestCaseName(classN,0,caseName,len(caseName))
print "获取分类下的测试用例名称:\n",caseName.strip(a)
print "设置使用中的测试用例:\n",lib.useTestCase(classN,caseName)
# print"设置使用中的下位机IP:\n",lib.useTargetIp("192.168.1.212") 
print "订阅输入信号的参数:\n",lib.regInputSignalParam("signal","P3")
print("设置发送信号的参数值:\n"),lib.setOutputSignalParamValue("signal","P3",55)
print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P3")
time.sleep(5)
print "为当前工程启动测试用(%s):\n"%caseName.split(a)[0],lib.startTestCase('caseName')
time.sleep(10)
print "下位机状态:",lib.getTargetState(0)
# 
print "获取测试用例运行时的参数数量:",lib.getTestCaseRuntimeParamCount()
# # print "停止工程测试用例:\n",lib.stopTestCase()
# 
print("获取工程输入信号的数量:")
num=lib.getInputSignalCount()
print(num)
 
print("获取输入信号的名称:")
sN="insingnalName"
print "*"*20
for i in range(num):
    lib.getInputSignalName(i,sN,13)
    print sN
print "*"*20
print("获取工程输出信号的数量:")
num=lib.getOutputSignalCount()
print(num)
 
print "*"*20
for i in range(num):
    print "获取输出信号的名称:"
    sN="outsignalName"
    lib.getOutputSignalName(i,sN,13)
    print sN
    spNum=lib.getSignalParamCount(sN)
    print("获取信号的参数数量:"),spNum
    print("获取信号参数名称:")
    for i in range(spNum):
        spN="SignalParamName"
        lib.getSignalParamName(sN,i,spN,15)
        print spN
#         time.sleep(1)
    print "*"*20

# print(lib.setAutoWhenGetParamValue(true))

# print("取消订阅:\n"),lib.unRegInputSignalParam("signal","P3")

# print("设置发送信号的参数值:\n"),lib.setOutputSignalParamValue("signal","P3",55)
print("获取订阅的信号参数值:\n"),lib.getInputSignalParamValue("signal","P3")
time.sleep(5)
print "停止工程测试用例:\n",lib.stopTestCase()

print "下位机状态:",lib.getTargetState(0)

print '获取当前工程的测试任务分类数量:\n',lib.getTestTaskClassCount()

print "获取当前工程的所有测试任务分类名称:"
for i in range(0,lib.getTestTaskClassCount()):
    tcN='projectTaskClassName'
    lib.getTestTaskClassName(i,tcN,20)
    print str(i+1)+'.'+tcN
    print "   获取测试任务集的测试任务数量",lib.getTestTaskCount(tcN)  
    for i in range(0,lib.getTestTaskCount(tcN)):
        tN='projectTackName'
        lib.getTestTaskName(tcN,i,tN,15)
        print "        根据任务分类名，获取测试任务名称:",tN
 
print "设置使用中的测试任务"
print(lib.useTestTask("45", "ww"))
 
print "根据当前测试任务，获取测试用例个数:\n", lib.getTestTaskTestCaseCount()
# print"设置使用中的下位机IP:\n",lib.useTargetIp("192.168.1.5") 
print '启动测试任务',lib.startTestTask(tN)  
  
print "获取测试任务下的测试用例数量:\n",lib.getTestTaskTestCaseCount()
print "停止工程测试用例:\n",lib.stopTestTask()
# time.sleep(5)
print "释放平台类:\n" ,lib.releaseQuiKLabPlatform()

