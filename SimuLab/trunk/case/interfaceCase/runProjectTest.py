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


class testRunProject(unittest.TestCase):
    u"""注册/注销/获取参数/信号值"""
    @classmethod
    def setUpClass(self):
        apiResultTest.creatConnect(hostIp)
        apiResultTest.loadProject(mainFileDir)
        apiResultTest.execProject()
        
    @classmethod
    def tearDownClass(self):
        apiResultTest.stopProject()
        apiResultTest.disConnect()


    def testParamLatest(self):
        u"""测试注册/注销/获取参数值(瞬态)接口"""
        paramLatestReturn = apiResultTest.paramLatest()
        regParamLatestReturnList = list(set(paramLatestReturn[0]))     #接口获取注册参数(瞬态)列表去重 
        regParamLatestReturnLen = len(regParamLatestReturnList)         #去重之后返回值列表的长度
        regParamLatestReturn =  regParamLatestReturnList[0]       #接口获取注册参数(瞬态)返回值         
        if  regParamLatestReturnLen == 1:
            compare.isEqual(0, regParamLatestReturn , pyfilename, "调用获取注册参数(瞬态)接口返回值为:{}".format(regParamLatestReturn), "调用获取注册参数(瞬态)接口返回值为:{}".format(regParamLatestReturn))
        else:
            compare.isEqual(1, regParamLatestReturnLen , pyfilename, "调用获取注册参数(瞬态)接口返回值列表长度为:{}".format(regParamLatestReturnLen), "调用获取注册参数(瞬态)接口返回值列表长度为:{}".format(regParamLatestReturnLen))
        
        getParamLatestValueReturnList = list(set(paramLatestReturn[1]))     #接口获取注册参数(瞬态)列表去重 
        getParamLatestValueReturnLen = len(getParamLatestValueReturnList)         #去重之后返回值列表的长度
        getParamLatestValueReturn =  getParamLatestValueReturnList[0]       #接口获取参数值(瞬态)返回值         
        if  getParamLatestValueReturnLen == 1:
            compare.isEqual(0, getParamLatestValueReturn , pyfilename, "调用获取参数值（瞬态）接口返回值为:{}".format(getParamLatestValueReturn), "调用获取参数值（瞬态）接口返回值为:{}".format(getParamLatestValueReturn))
        else:
            compare.isEqual(1, getParamLatestValueReturnLen , pyfilename, "调用获取参数值（瞬态）接口返回值列表长度为:{}".format(getParamLatestValueReturnLen), "调用获取参数值（瞬态）接口返回值列表长度为:{}".format(getParamLatestValueReturnLen))    
    
        unParamLatestValueReturnList = list(set(paramLatestReturn[2]))     #接口获取注册参数(瞬态)列表去重 
        unParamLatestValueReturnLen = len(unParamLatestValueReturnList)         #去重之后返回值列表的长度
        unParamLatestValueReturn =  unParamLatestValueReturnList[0]       #接口获取注销参数(瞬态)返回值         
        if  unParamLatestValueReturnLen == 1:
            compare.isEqual(0, unParamLatestValueReturn , pyfilename, "调用注销参数值（瞬态）接口返回值为:{}".format(unParamLatestValueReturn), "调用注销参数值（瞬态）接口返回值为:{}".format(unParamLatestValueReturn))
        else:
            compare.isEqual(1, unParamLatestValueReturnLen , pyfilename, "调用注销参数值（瞬态）接口返回值列表长度为:{}".format(unParamLatestValueReturnLen), "调用注销参数值（瞬态）接口返回值列表长度为:{}".format(unParamLatestValueReturnLen)) 
            
    def testParamPeriod(self):
        u"""测试注册/注销/获取参数值(连续)接口"""
        paramPeriodReturn = apiResultTest.paramPeriod()
        regParamPeriodReturnList = list(set(paramPeriodReturn[0]))     #接口获取注册参数(连续)列表去重 
        regParamPeriodReturnLen = len(regParamPeriodReturnList)         #去重之后返回值列表的长度
        regParamPeriodReturn =  regParamPeriodReturnList[0]       #接口获取注册参数(连续)返回值         
        if  regParamPeriodReturnLen == 1:
            compare.isEqual(0, regParamPeriodReturn , pyfilename, "调用获取注册参数(连续)接口返回值为:{}".format(regParamPeriodReturn), "调用获取注册参数(连续)接口返回值为:{}".format(regParamPeriodReturn))
        else:
            compare.isEqual(1, regParamPeriodReturnLen , pyfilename, "调用获取注册参数(连续)接口返回值列表长度为:{}".format(regParamPeriodReturnLen), "调用获取注册参数(连续)接口返回值列表长度为:{}".format(regParamPeriodReturnLen))
        
        getParamPeriodValueReturnList = list(set(paramPeriodReturn[1]))     #接口获取注册参数(连续)列表去重 
        getParamPeriodValueReturnLen = len(getParamPeriodValueReturnList)         #去重之后返回值列表的长度
        getParamPeriodValueReturn =  getParamPeriodValueReturnList[0]       #接口获取参数值(连续)返回值         
        if  getParamPeriodValueReturnLen == 1:
            compare.isEqual(0, getParamPeriodValueReturn , pyfilename, "调用获取参数值（连续）接口返回值为:{}".format(getParamPeriodValueReturn), "调用获取参数值（瞬态）接口返回值为:{}".format(getParamPeriodValueReturn))
        else:
            compare.isEqual(1, getParamPeriodValueReturnLen , pyfilename, "调用获取参数值（连续）接口返回值列表长度为:{}".format(getParamPeriodValueReturnLen), "调用获取参数值（瞬态）接口返回值列表长度为:{}".format(getParamPeriodValueReturnLen))    
    
        unParamPeriodValueReturnList = list(set(paramPeriodReturn[2]))     #接口获取注销参数(连续)列表去重 
        unParamPeriodValueReturnLen = len(unParamPeriodValueReturnList)         #去重之后返回值列表的长度
        unParamPeriodValueReturn =  unParamPeriodValueReturnList[0]       #接口获取注销参数(连续)返回值         
        if  unParamPeriodValueReturnLen == 1:
            compare.isEqual(0, unParamPeriodValueReturn , pyfilename, "调用注销参数值（连续）接口返回值为:{}".format(unParamPeriodValueReturn), "调用注销参数值（连续）接口返回值为:{}".format(unParamPeriodValueReturn))
        else:
            compare.isEqual(1, unParamPeriodValueReturnLen , pyfilename, "调用注销参数值（连续）接口返回值列表长度为:{}".format(unParamPeriodValueReturnLen), "调用注销参数值（连续）接口返回值列表长度为:{}".format(unParamPeriodValueReturnLen))    
   
    def testoutSigLatest(self):
        u"""测试注册/注销/获取信号值(瞬态)接口"""
        outSigLatestReturn = apiResultTest.outSigLatest()
        regOutSigLatestReturnList = list(set(outSigLatestReturn[0]))     #接口获取注册信号(瞬态)列表去重 
        regOutSigLatestReturnLen = len(regOutSigLatestReturnList)         #去重之后返回值列表的长度
        regOutSigLatestReturn =  regOutSigLatestReturnList[0]       #接口获取注册信号(瞬态)返回值         
        if  regOutSigLatestReturnLen == 1:
            compare.isEqual(0, regOutSigLatestReturn , pyfilename, "调用获取注册信号(瞬态)接口返回值为:{}".format(regOutSigLatestReturn), "调用获取注册信号(瞬态)接口返回值为:{}".format(regOutSigLatestReturn))
        else:
            compare.isEqual(1, regOutSigLatestReturnLen , pyfilename, "调用获取注册信号(瞬态)接口返回值列表长度为:{}".format(regOutSigLatestReturnLen), "调用获取注册信号(瞬态)接口返回值列表长度为:{}".format(regOutSigLatestReturnLen))
        
        getOutSigLatestValueReturnList = list(set(outSigLatestReturn[1]))     #接口获取注册信号(瞬态)列表去重 
        getOutSigLatestValueReturnLen = len(getOutSigLatestValueReturnList)         #去重之后返回值列表的长度
        getOutSigLatestValueReturn =  getOutSigLatestValueReturnList[0]       #接口获取信号值(瞬态)返回值         
        if  getOutSigLatestValueReturnLen == 1:
            compare.isEqual(0, getOutSigLatestValueReturn , pyfilename, "调用获取信号值（瞬态）接口返回值为:{}".format(getOutSigLatestValueReturn), "调用获取信号值（瞬态）接口返回值为:{}".format(getOutSigLatestValueReturn))
        else:
            compare.isEqual(1, getOutSigLatestValueReturnLen , pyfilename, "调用获取信号值（瞬态）接口返回值列表长度为:{}".format(getOutSigLatestValueReturnLen), "调用获取信号值（瞬态）接口返回值列表长度为:{}".format(getOutSigLatestValueReturnLen))    
    
        unParamLatestValueReturnList = list(set(outSigLatestReturn[2]))     #接口获取注册信号(瞬态)列表去重 
        unParamLatestValueReturnLen = len(unParamLatestValueReturnList)         #去重之后返回值列表的长度
        unParamLatestValueReturn =  unParamLatestValueReturnList[0]       #接口获取注销信号(瞬态)返回值         
        if  unParamLatestValueReturnLen == 1:
            compare.isEqual(0, unParamLatestValueReturn , pyfilename, "调用注销信号值（瞬态）接口返回值为:{}".format(unParamLatestValueReturn), "调用注销信号值（瞬态）接口返回值为:{}".format(unParamLatestValueReturn))
        else:
            compare.isEqual(1, unParamLatestValueReturnLen , pyfilename, "调用注销信号值（瞬态）接口返回值列表长度为:{}".format(unParamLatestValueReturnLen), "调用注销信号值（瞬态）接口返回值列表长度为:{}".format(unParamLatestValueReturnLen))
            
    def testOutSigPeriod(self):
        u"""测试注册/注销/获取信号值(连续)接口"""
        outSigPeriodReturn = apiResultTest.outSigPeriod()
        regOutSigPeriodReturnList = list(set(outSigPeriodReturn[0]))     #接口获取注册信号(连续)列表去重 
        regOutSigPeriodReturnLen = len(regOutSigPeriodReturnList)         #去重之后返回值列表的长度
        regOutSigPeriodReturn =  regOutSigPeriodReturnList[0]       #接口获取注册信号(连续)返回值         
        if  regOutSigPeriodReturnLen == 1:
            compare.isEqual(0, regOutSigPeriodReturn , pyfilename, "调用获取注册信号(连续)接口返回值为:{}".format(regOutSigPeriodReturn), "调用获取注册信号(连续)接口返回值为:{}".format(regOutSigPeriodReturn))
        else:
            compare.isEqual(1, regOutSigPeriodReturnLen , pyfilename, "调用获取注册信号(连续)接口返回值列表长度为:{}".format(regOutSigPeriodReturnLen), "调用获取注册信号(连续)接口返回值列表长度为:{}".format(regOutSigPeriodReturnLen))
        
        getOutSigPeriodValueReturnList = list(set(outSigPeriodReturn[1]))     #接口获取注册信号(连续)列表去重 
        getOutSigPeriodValueReturnLen = len(getOutSigPeriodValueReturnList)         #去重之后返回值列表的长度
        getOutSigPeriodValueReturn =  getOutSigPeriodValueReturnList[0]       #接口获取信号值(连续)返回值         
        if  getOutSigPeriodValueReturnLen == 1:
            compare.isEqual(0, getOutSigPeriodValueReturn , pyfilename, "调用获取信号值（连续）接口返回值为:{}".format(getOutSigPeriodValueReturn), "调用获取信号值（瞬态）接口返回值为:{}".format(getOutSigPeriodValueReturn))
        else:
            compare.isEqual(1, getOutSigPeriodValueReturnLen , pyfilename, "调用获取信号值（连续）接口返回值列表长度为:{}".format(getOutSigPeriodValueReturnLen), "调用获取信号值（瞬态）接口返回值列表长度为:{}".format(getOutSigPeriodValueReturnLen))    
    
        unOutSigPeriodValueReturnList = list(set(outSigPeriodReturn[2]))     #接口获取注销信号(连续)列表去重 
        unOutSigPeriodValueReturnLen = len(unOutSigPeriodValueReturnList)         #去重之后返回值列表的长度
        unOutSigPeriodValueReturn =  unOutSigPeriodValueReturnList[0]       #接口获取注销信号(连续)返回值         
        if  unOutSigPeriodValueReturnLen == 1:
            compare.isEqual(0, unOutSigPeriodValueReturn , pyfilename, "调用注销信号值（连续）接口返回值为:{}".format(unOutSigPeriodValueReturn), "调用注销信号值（连续）接口返回值为:{}".format(unOutSigPeriodValueReturn))
        else:
            compare.isEqual(1, unOutSigPeriodValueReturnLen , pyfilename, "调用注销信号值（连续）接口返回值列表长度为:{}".format(unOutSigPeriodValueReturnLen), "调用注销信号值（连续）接口返回值列表长度为:{}".format(unOutSigPeriodValueReturnLen))     

    def testGetOutSigValue(self):
        u"""测试获取信号值"""
        getOutSigValueReturn = apiResultTest.getOutSigValue()[1]
        getOutSigValueReturnList = list(set(getOutSigValueReturn))     #接口获取信号值列表去重 
        getOutSigValueReturnLen = len(getOutSigValueReturnList)         #去重之后返回值列表的长度
        getOutSigValueReturn =  getOutSigValueReturnList[0]       #接口获取注册值返回值         
        if  getOutSigValueReturnLen == 1:
            compare.isEqual(0, getOutSigValueReturn , pyfilename, "调用获取信号值接口返回值为:{}".format(getOutSigValueReturn), "调用获取信号值接口返回值为:{}".format(getOutSigValueReturn))
        else:
            compare.isEqual(1, getOutSigValueReturnLen , pyfilename, "调用获取信号值接口返回值列表长度为:{}".format(getOutSigValueReturnLen), "调用获取信号值接口返回值列表长度为:{}".format(getOutSigValueReturnLen))

    def testGetModelStatus(self):
        u"""获取模型仿真状态"""
        getModelStatusReturn = apiResultTest.getModelStatus()   #获取模型状态接口返回值
        getModelStatusReturnList = list(set(getModelStatusReturn))    #列表去重
        getModelStatusReturnLen = len(getModelStatusReturnList)       #去重之后返回值列表长度
        getModelStatusReturn = getModelStatusReturnList[0]            #获取返回值
        if getModelStatusReturnLen == 1:
            compare.isEqual(0, getModelStatusReturn , pyfilename, "调用获取模型仿真状态返回值为:{}".format(getModelStatusReturn), "调用获取模型仿真状态返回值为:{}".format(getModelStatusReturn))
        else:
            compare.isEqual(0, getModelStatusReturnLen , pyfilename, "调用获取模型仿真状态返回值列表长度为:{}".format(getModelStatusReturnLen), "调用获取模型仿真状态返回值列表长度为:{}".format(getModelStatusReturnLen))
        
if __name__ == "__main__":
    unittest.main()