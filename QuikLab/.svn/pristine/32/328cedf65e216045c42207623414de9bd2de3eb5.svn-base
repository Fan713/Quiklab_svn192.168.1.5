#! /usr/bin/env python
#coding=GB18030
import os
import unittest

import casebase.case_wrapper as case
import logging
import getpass


configList = case.readIniConfig('QuikLab3.0')
pyfilename = os.path.basename(__file__)


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def testConfDataBase(self):
        case.confDataBase(configList[1],configList[2])
        username = getpass.getuser()
        xmlList = case.readXml('C:\Users\%s\QuiKLab3\config.xml'%username, 'hostname')
        case.isNotIN('192.168.1.227', xmlList, pyfilename,"192.168.1.227不在xml文件中")
            
    def tearDown(self):
        pass
#         case.closeLogin(u'登录--试验自动测试管理系统', u"退出")        
        
        
if __name__ == "__main__":
#     pass
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
