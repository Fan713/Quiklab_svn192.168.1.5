#! /usr/bin/env python
#coding=GB18030
import os
import casebase.case_wrapper as case
import unittest
import casebase.TCP_Component as tcp
import casebase.init as init
import casebase.QuikLab_Install as install
configList = case.readIniConfig('QuikLab3.0')
class Test(unittest.TestCase):
    def setUp(self):
        init._init()
        install._checkInstall()
        flag='tag.txt'
        with open(flag,'r') as f:
            for i in f:
                if i == '0':
                    exit()
        case.confDataBase(configList[1],configList[2])
        case.login(configList[1],configList[2],configList[3],configList[4])


    def tearDown(self):
        os.system('taskkill /IM MainApp.exe /F')

    def testName(self):
        window_name =configList[0]
        case.creat_pro(window_name,configList[5])
        case.unload_pro(window_name)
        case.load_pro(window_name, configList[5])
        case.add_Bus(window_name)
        case.add_dev(window_name)
        case.add_tar(window_name)
        tcp.add_TCP_Client_Interface(window_name)
        tcp.add_TCP_Service_Interface(window_name)
        tcp.add_TCP_Signal(window_name)
        tcp.add_TCP_Case(window_name)
        tcp.run_case(window_name)
        tcp.compareRes()
    
if __name__ == "__main__":
    unittest.main()