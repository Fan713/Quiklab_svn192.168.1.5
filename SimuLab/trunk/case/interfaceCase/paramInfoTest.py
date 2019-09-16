#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年4月12日

@author: KLJS276
'''
import os
import sys
import unittest

dir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
sys.path.append(dir)
from trunk.caseBase.interfaceCase import apiResultTest,getExpectTest
from trunk.common import compare,readConfig,getHostInfo

pyfilename = os.path.basename(__file__)
readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]

hostInfo = getHostInfo.getHostInfo()
hostIp = hostInfo.getHostIp()

class testParamInfo(unittest.TestCase):
    u"""测试模型参数相关信息"""
    @classmethod
    def setUpClass(self):
        apiResultTest.creatConnect(hostIp)
        apiResultTest.loadProject(mainFileDir)

    @classmethod
    def tearDownClass(self):
        apiResultTest.stopProject()
        apiResultTest.disConnect()
     
    def testParamNameID(self):
        u"""测试参数名称与ID的对应关系"""
        apiParamNameIdInfo = apiResultTest.getParamInfo()[2]
        expectParamNameIdInfo = getExpectTest.getParamInfo()[0]
        compare.isEqual(expectParamNameIdInfo, apiParamNameIdInfo, pyfilename, "接口获取的参数名称与ID对应关系：{}与预期的结果:{}一致".format(apiParamNameIdInfo, expectParamNameIdInfo),"接口获取的参数名称与ID的对应关系：{}与预期结果:{}不一致".format(apiParamNameIdInfo, expectParamNameIdInfo))
        
    def testParamModelName(self):
        u"""测试参数名称与模型名称对应关系"""
        apiParaModelNameInfo = apiResultTest.getParamInfo()[3]
        expectParaModelNameInfo = getExpectTest.getParamInfo()[1]
        compare.isEqual(apiParaModelNameInfo, expectParaModelNameInfo, pyfilename, "接口获取的参数与模型名称对应关系：{}与预期结果:{}一致".format(apiParaModelNameInfo, expectParaModelNameInfo),"接口获取的参数名称与模型名称的对应关系：{}与预期结果:{}不一致".format(apiParaModelNameInfo, expectParaModelNameInfo))
        
    def testParamValue(self):
        u"""测试获取修改模型中参数的值"""
        apiParamValue = apiResultTest.getParamValue()[1]
        expectParamValue = getExpectTest.getParamValue()
        compare.isEqual(expectParamValue, apiParamValue, pyfilename, "接口获取的参数与参数值对应关系为：{}与预期结果:{}一致".format(apiParamValue, expectParamValue), "接口获取的参数与参数值对应关系为：{}与预期结果:{}不一致".format(apiParamValue, expectParamValue))
        apiSetParamValue = apiResultTest.setParamValue()
        for key in apiParamValue.keys():
            getApiParamValue = apiParamValue[key]                #获取参数未修改之前的值
            getApiSetParamValue = apiSetParamValue[key]          #获取参数修改之后的值
            for i in range (0,len(getApiParamValue)):
                if getApiSetParamValue[i] != (getApiParamValue[i] + 1):
                    compare.isEqual(0, 1, pyfilename, "", "修改之后的参数值：{}比修改之前的参数值:{}不是大1".format(apiSetParamValue, apiParamValue))           
        compare.isEqual(0,0,pyfilename,"修改之后的参数值：{}比修改之前的参数值:{}大1".format(apiSetParamValue, apiParamValue),'')       

if __name__ == "__main__":
    unittest.main()