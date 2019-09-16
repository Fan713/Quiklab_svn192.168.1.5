#! /usr/bin/env python
#coding=utf-8
import os
import sys
import time
import unittest

from trunk.caseBase.interfaceCase import apiResultTest, getExpectTest
from trunk.common import compare, readConfig, getHostInfo


dir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
sys.path.append(dir)



pyfilename = os.path.basename(__file__)
readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]

hostInfo = getHostInfo.getHostInfo()
hostIp = hostInfo.getHostIp()


class testProStatus(unittest.TestCase):
    u"""测试工程状态"""
    @classmethod
    def setUpClass(self):
        apiResultTest.creatConnect(hostIp)
        apiResultTest.loadProject(mainFileDir)
        

    @classmethod
    def tearDownClass(self):
        apiResultTest.disConnect()


    def testProStatus(self):
        proStatus = apiResultTest.getProStatus()   #获取工程状态
        compare.isEqual(2, proStatus, pyfilename, "工程状态为：{}与预期的工程状态：暂停：2一致".format(proStatus), "工程状态为：{}与预期的工程状态：暂停：2不一致".format(proStatus))
        apiResultTest.execProject()                #运行工程
        time.sleep(10)
        proStatus = apiResultTest.getProStatus()   #获取工程状态
        compare.isEqual(3, proStatus, pyfilename, "工程状态为：{}与预期的工程状态：运行：3一致".format(proStatus), "工程状态为：{}与预期的工程状态：运行：3不一致".format(proStatus))
        apiResultTest.pauseProject()               #暂停工程
        time.sleep(10)
        proStatus = apiResultTest.getProStatus()   #获取工程状态
        compare.isEqual(2, proStatus, pyfilename, "工程状态为：{}与预期的工程状态：暂停：2一致".format(proStatus), "工程状态为：{}与预期的工程状态：运行：3不一致".format(proStatus))
        apiResultTest.stopProject()                #停止工程
        time.sleep(10)
        proStatus = apiResultTest.getProStatus()   #获取工程状态
        compare.isEqual(1, proStatus, pyfilename, "工程状态为：{}与预期的工程状态：未加载：1一致".format(proStatus), "工程状态为：{}与预期的工程状态：未加载：1不一致".format(proStatus))

if __name__ == "__main__":
    unittest.main()