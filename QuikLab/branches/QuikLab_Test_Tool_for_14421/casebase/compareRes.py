#! /usr/bin/env python
#coding=GB18030
import os
import time
import getpass
def isNotIn(expectResult,actualResult,logFile,Msg):
    with open(logFile,'r') as f:
        actualResult=f.read()
    if expectResult in actualResult:
        print Msg
username = getpass.getuser()
filePath='C:\Users\%s\QuiKLab3\\runtime\\'%username
#     os.chdir(filePath)
fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'
logFile=filePath+fileName
print logFile
despath=os.getcwd()
os.chdir('../report')
despath=os.getcwd()
os.system('copy %s %s'%(logFile,despath))