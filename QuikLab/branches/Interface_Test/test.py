#! /usr/bin/env python
#coding=GB18030
import re
import ctypes
import os
import sys
import time
import logging
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
    
os.chdir(r"D:\QuiKLab3.0")
lib = ctypes.cdll.LoadLibrary(r"QuiKLabAPI.dll")
# temp='s'*128
# lib.getAppPath(temp)
# print '-------------------------',temp
time.sleep(5)
print "��ʼ��QuiKLabƽ̨��:\n",lib.initQuiKLabPlatform()
time.sleep(5)
print("��ȡ��λ������:\n"),lib.getTargetCount()
print("����������ȡ��λ��IP:")
IP="iP"*64
lib.getTargetIP(0,IP,len(IP))
print(IP)

print"����������ȡ��λ��״̬:\n",lib.getTargetState(0)

# print"����ʹ���е���λ��IP:\n",lib.useTargetIp("192.168.1.5") 
print "��ȡ��ǰƽ̨�Ĺ�������:\n",lib.getProjectCount()
p_Num=lib.getProjectCount()
pN="s"*128
p=[]
lib.getProjectName(1,pN,len(pN))
a='\x00' #C�����еĿո�
for i in range(p_Num):      #��ѯ���й�������
    lib.getProjectName(i,pN,len(pN))
    p.append(pN.split(a)[0])    #��ȥ����ַ����е�a(�ո�)
print repr(p).decode('string_escape')  #�ܹ��������
time.sleep(5)

print "���ع���:\n",lib.loadProject('1111')

#��������
print "��ȡ��ǰ���̵Ĳ���������������:\n",lib.getTestCaseClassCount()

classN='s'*128
lib.getTestCaseClassName(1, classN, len(classN))
print "������������ȡ�����µĲ�������������:\n",classN.strip(a)

pn = "s"*128;
lib.getProjectName(1,pn,len(pn))
print "����Ϊ'1'�Ĺ�������:\n", pn.strip(a)

cpn="s"*128
lib.getCurrentProjectName(cpn,len(pn))
print "��ǰ���̵�����:\n",cpn.strip(a)


 
print "��ȡ�����������Ĳ�����������:\n",lib.getTestCaseCount(classN)
 
caseName='s'*128
lib.getTestCaseName(classN,0,caseName,len(caseName))
print "��ȡ�����µĲ�����������:\n",caseName.strip(a)
print "����ʹ���еĲ�������:\n",lib.useTestCase(classN,caseName)
# print"����ʹ���е���λ��IP:\n",lib.useTargetIp("192.168.1.212") 
print "���������źŵĲ���:\n",lib.regInputSignalParam("signal","P3")
print("���÷����źŵĲ���ֵ:\n"),lib.setOutputSignalParamValue("signal","P3",55)
print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P3")
time.sleep(5)
print "Ϊ��ǰ��������������(%s):\n"%caseName.split(a)[0],lib.startTestCase(caseName)
time.sleep(10)
print "��λ��״̬:",lib.getTargetState(0)
# 
print "��ȡ������������ʱ�Ĳ�������:",lib.getTestCaseRuntimeParamCount()
# # print "ֹͣ���̲�������:\n",lib.stopTestCase()
# 
print("��ȡ���������źŵ�����:")
num=lib.getInputSignalCount()
print(num)
 
print("��ȡ�����źŵ�����:")
sN="insingnalName"
for i in range(num):
    lib.getInputSignalName(i,sN,13)
    print sN
     
print("��ȡ��������źŵ�����:")
num=lib.getOutputSignalCount()
print(num)
 
for i in range(num):
    print "*"*20
    print "��ȡ����źŵ�����:"
    sN="outsignalName"
    lib.getOutputSignalName(i,sN,13)
    print sN
    spNum=lib.getSignalParamCount(sN)
    print("��ȡ�źŵĲ�������:"),spNum
    print("��ȡ�źŲ�������:")
    for i in range(spNum):
        spN="SignalParamName"
        lib.getSignalParamName(sN,i,spN,15)
#         time.sleep(1)
    print "*"*20

# print(lib.setAutoWhenGetParamValue(true))

# print("ȡ������:\n"),lib.unRegInputSignalParam("signal","P3")

# print("���÷����źŵĲ���ֵ:\n"),lib.setOutputSignalParamValue("signal","P3",55)
print("��ȡ���ĵ��źŲ���ֵ:\n"),lib.getInputSignalParamValue("signal","P3")
time.sleep(5)
print "ֹͣ���̲�������:\n",lib.stopTestCase()

print "��λ��״̬:",lib.getTargetState(0)

print '��ȡ��ǰ���̵Ĳ��������������:\n',lib.getTestTaskClassCount()

print "��ȡ��ǰ���̵����в��������������:"
for i in range(0,lib.getTestTaskClassCount()):
    tcN='projectTaskClassName'
    lib.getTestTaskClassName(i,tcN,20)
    print str(i+1)+'.'+tcN
    print "   ��ȡ�������񼯵Ĳ�����������",lib.getTestTaskCount(tcN)  
    for i in range(0,lib.getTestTaskCount(tcN)):
        tN='projectTackName'
        lib.getTestTaskName(tcN,i,tN,15)
        print "        �����������������ȡ������������:",tN
 
print "����ʹ���еĲ�������"
print(lib.useTestTask("45", "ww"))
 
print "���ݵ�ǰ�������񣬻�ȡ������������:\n", lib.getTestTaskTestCaseCount()
# print"����ʹ���е���λ��IP:\n",lib.useTargetIp("192.168.1.5") 
# print '������������',lib.startTestTask(tN)  
  
print "��ȡ���������µĲ�����������:\n",lib.getTestTaskTestCaseCount()
 
# time.sleep(5)
print "�ͷ�ƽ̨��:\n" ,lib.releaseQuiKLabPlatform()

