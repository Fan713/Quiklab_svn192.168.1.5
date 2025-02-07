#! /usr/bin/env python
#coding=utf-8
import os
import sys
import unittest

dir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
sys.path.append(dir)
from caseBase.interfaceCase import apiResultTest,getExpectTest
from common import compare,readConfig,getHostInfo



pyfilename = os.path.basename(__file__)
readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]

hostInfo = getHostInfo.getHostInfo()
hostIp = hostInfo.getHostIp()

class testmodelInfo(unittest.TestCase):
    u"""测试模型相关信息"""
    @classmethod
    def setUpClass(self):
        apiResultTest.creatConnect(hostIp)
        apiResultTest.loadProject(mainFileDir)

    @classmethod
    def tearDownClass(self):
        apiResultTest.stopProject()
        apiResultTest.disConnect()
        
    def testModelCount(self):
        u"""测试模型个数"""
        apiModelCount = apiResultTest.getModelCount()
        expectModelCount = getExpectTest.getModelCount()
        compare.isEqual(expectModelCount, apiModelCount, pyfilename, "接口获取的模型个数：{}与预期的模型个数：{}一致".format(apiModelCount, expectModelCount), "接口获取的模型个数：{}与预期的模型个数：{}不一致".format(apiModelCount, expectModelCount))
           
    def testModelName(self):
        u"""测试模型名称"""
        apiModelInfo = apiResultTest.getModelInfo()[0]
        expectModelInfo = getExpectTest.getModelInfo()[0]
        compare.isEqual(expectModelInfo, apiModelInfo, pyfilename, "接口获取的模型名称：{}与预期的模型名称:{}一致".format(apiModelInfo, expectModelInfo),"接口获取的模型名称：{}与预期的模型名称:{}不一致".format(apiModelInfo, expectModelInfo))
        
    def testModelTarget(self):
        u"""模型运行的下位机信息"""
        apiModelTargetInfo = apiResultTest.getModelInfo()[1]
        expectModelTargetInfo = getExpectTest.getModelInfo()[1]
        compare.isEqual(apiModelTargetInfo, expectModelTargetInfo, pyfilename, "接口获取的模型运行下位机信息：{}与预期的模型运行下位机信息:{}一致".format(apiModelTargetInfo, expectModelTargetInfo),"接口获取的模型运行下位机信息：{}与预期的模型运行下位机信息:{}不一致".format(apiModelTargetInfo, expectModelTargetInfo))
        
    def testModelNameId(self):
        u"""测试模型名称与ID对应关系"""
        apiModelNameId = apiResultTest.getModelInfo()[2]
        expectModelNameId = getExpectTest.getModelInfo()[2]
        compare.isEqual(apiModelNameId,expectModelNameId,pyfilename,"接口获取的模型名称与ID对应关系：{}与预期结果：{}一致".format(apiModelNameId, expectModelNameId),"接口获取的模型名称与ID对应关系：{}与预期结果：{}不一致".format(apiModelNameId, expectModelNameId))
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
