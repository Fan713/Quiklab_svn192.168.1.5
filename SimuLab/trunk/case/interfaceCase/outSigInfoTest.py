#! /usr/bin/env python
#coding=utf-8
import os
import sys
import unittest

from caseBase.interfaceCase import apiResultTest, getExpectTest
from common import compare, readConfig, getHostInfo

dir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
sys.path.append(dir)

pyfilename = os.path.basename(__file__)
readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]

hostInfo = getHostInfo.getHostInfo()
hostIp = hostInfo.getHostIp()

class testOutSigInfo(unittest.TestCase):
    u"""测试模型信号相关信息"""
    @classmethod
    def setUpClass(self):
        apiResultTest.creatConnect(hostIp)
        apiResultTest.loadProject(mainFileDir)

    @classmethod
    def tearDownClass(self):
        apiResultTest.stopProject()
        apiResultTest.disConnect()


    def testOutSigCount(self):
        u"""测试模型中信号个数"""
        apiOutSigCount = apiResultTest.getOutSigInfo()[0]
        expectOutSigCount = getExpectTest.getOutSigCount()
        compare.isEqual(expectOutSigCount, apiOutSigCount, pyfilename, "接口获取的信号个数：{}与预期结果：{}一致".format(apiOutSigCount, expectOutSigCount), "接口获取的信号个数：{}与预期结果：{}不一致".format(apiOutSigCount, expectOutSigCount))
        
    def testOutSigNameId(self):
        u"""测试输出信号名称与ID对应关系"""
        apiOutSigNameId = apiResultTest.getOutSigInfo()[2]
        expectOutSigNameId = getExpectTest.getOutSigInfo()[0]
        compare.isEqual(expectOutSigNameId, apiOutSigNameId, pyfilename, "接口信号名称与ID对应关系：{}与预期结果：{}一致".format(apiOutSigNameId, expectOutSigNameId), "接口信号名称与ID对应关系：{}与预期结果：{}不一致".format(apiOutSigNameId, expectOutSigNameId))
        
    def testOutSigModelName(self):
        u"""测试输出信号名称与模型名称对应关系"""
        apiOutSigModelName = apiResultTest.getOutSigInfo()[3]
        expectOutSigModelName = getExpectTest.getOutSigInfo()[1]
        compare.isEqual(expectOutSigModelName, apiOutSigModelName, pyfilename, "接口信号名称与模型名称对应关系：{}与预期结果：{}一致".format(apiOutSigModelName, expectOutSigModelName), "接口信号名称与模型名称对应关系：{}与预期结果：{}不一致".format(apiOutSigModelName, expectOutSigModelName))
        

if __name__ == "__main__":
    unittest.main()