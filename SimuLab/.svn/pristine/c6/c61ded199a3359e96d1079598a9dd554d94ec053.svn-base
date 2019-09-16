#! /usr/bin/env python
#coding=utf-8

import linecache
import os
import sys
import time
import unittest

from trunk.caseBase.interfaceCase import apiResultTest, getExpectTest
from trunk.common import compare, readConfig, getHostInfo, searchFile


dir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
sys.path.append(dir)

pyfilename = os.path.basename(__file__)
readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]

hostInfo = getHostInfo.getHostInfo()
hostIp = hostInfo.getHostIp()

class testrecordGroupInfo(unittest.TestCase):
    u"""测试信号/参数录制相关接口"""
    @classmethod
    def setUpClass(self):
        apiResultTest.creatConnect(hostIp)
        apiResultTest.loadProject(mainFileDir)
        apiResultTest.execProject()
    
    @classmethod
    def tearDownClass(self):
        apiResultTest.stopProject()
        apiResultTest.disConnect()
    
    def testrecordInfo(self):
        u"""测试注册录制/获取录制状态"""
        groupName = "record"
        fileDir = searchFile.searchFile(r"\report")
#         fileDir = r"E:\0603_20190603_155430"
        fileName = "group1.txt"
        regRecordGroupReturn = apiResultTest.regRecordGroup(groupName, 1, fileDir, fileName)           #注册录制组
        compare.isEqual(0,regRecordGroupReturn,pyfilename,'调用注册录制组接口返回值为:{}'.format(regRecordGroupReturn),'调用注册录制组接口返回值为:{}'.format(regRecordGroupReturn))   #判断调用注册录制组接口的返回值是否为0
        
        fileStatus = apiResultTest.getRecordStatus(groupName)                   #获取录制组状态
        print fileStatus,type(fileStatus)
        if  fileStatus[1] == 0:
            compare.isEqual(2,fileStatus[0],pyfilename,'录制组状态为:{}'.format(fileStatus[0]),'录制组状态为:{}'.format(fileStatus[0]))     #判断录制组状态是否为2(录制中)
        else:
            compare.isEqual(0,fileStatus[1],pyfilename,'调用获取录制组状态接口返回值为:{}'.format(fileStatus[1]),'调用获取录制组状态接口返回值为:{}'.format(fileStatus[1]))    #判断调用录制组状态接口返回值是否为0
                
#         while fileStatus[0] != 4:
#             fileStatus = apiResultTest.getRecordStatus(groupName)
#             print fileStatus,type(fileStatus)
        time.sleep(15)
        fileStatus = apiResultTest.getRecordStatus(groupName)
        compare.isEqual(4,fileStatus[0],pyfilename,'录制组状态为:{}'.format(fileStatus[0]),'录制组状态为:{}'.format(fileStatus[0]))      #判断录制组状态是否为4(录制完成)
                            
        fileNameDir = os.path.join(fileDir,fileName)
        if os.path.exists(fileNameDir):
            secondText = linecache.getline(fileNameDir,2)      #获取录制文件中第2行的内容
            startTime = float(secondText.split(',')[0])         #获取录制文件中第2行第1列的内容，即录制的起始时间
            thirdText = linecache.getline(fileNameDir,3)      #获取录制文件中第3行的内容
            thirdTime = float(thirdText.split(',')[0])        #获取录制文件中第3行第1列的内容
            countNum = len(open(fileNameDir,'rU').readlines())   #获取录制的文件中的行数
            lastText = linecache.getline(fileNameDir,countNum)   #获取最后一行的内容
            lastTime = float(lastText.split(',')[0])             #获取最后一行第一列的内容，即录制的结束时间
            difTime = int(round(lastTime - startTime))      #获得录制的时间
            compare.isEqual(10, difTime, pyfilename, "录制时长{}s与设置的时长10s一致".format(difTime), "录制时长{}s与设置的时长10s不一致".format(difTime))
            sampleRate = int((thirdTime - startTime)*(10**6))       #将录制的时间差由s换算成us
            compare.isEqual(1000, sampleRate, pyfilename, "录制的采样率{}us与设置的采样率1000us一致".format(sampleRate), "录制的采样率{}us与设置的采样率1000us不一致".format(sampleRate))
        else:
            compare.isEqual(0,1,pyfilename,'','{}路径下没有生成录制的文件'.format(fileNameDir))   #当调用注册录制组接口成功但是没有生成录制文件时抛出异常且日志中打印的信息
    
    def testUnRecordInfo(self):
        u"""测试注册录制/注销录制接口"""
        groupName = "record1"
        fileDir = searchFile.searchFile(r"\report")
        fileName = "group2.txt"
        regRecordGroupReturn = apiResultTest.regRecordGroup(groupName, 1, fileDir, fileName)           #注册录制组
        compare.isEqual(0,regRecordGroupReturn,pyfilename,'调用注册录制组接口返回值为:{}'.format(regRecordGroupReturn),'调用注册录制组接口返回值为:{}'.format(regRecordGroupReturn))   #判断调用注册录制组接口的返回值是否为0
        unregReturn = apiResultTest.unRegRecordGroup(groupName)                               # 强制注销录制组
        compare.isEqual(0,unregReturn,pyfilename,'调用注销接口状态返回值为:{}'.format(unregReturn),'调用注销接口状态返回值为:{}'.format(unregReturn))

if __name__ == "__main__":
    unittest.main()
            
    
        