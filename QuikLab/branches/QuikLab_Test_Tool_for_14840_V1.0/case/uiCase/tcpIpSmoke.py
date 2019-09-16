#! /usr/bin/env python
#coding=GB18030
import getpass
import os
import socket
import time
import unittest
import casebase.TCP_Component as tcp
import casebase.case_wrapper as case
from casebase.checkName import check
# import casebase.init as init


configList = case.readIniConfig('QuikLab3.0')
ip=[]
host=socket.gethostname()
ip=socket.gethostbyname(host).split('.')   #获得本机IP并存入数组ip
print "Current ip is:",ip
window_name =configList[0]
getName=check()
proName=getName.getProName(configList[5])

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print 'start'
#         import casebase.QuikLab_Install as install
#         install._checkInstall()
#         username = getpass.getuser()
#         despath='C:\\Users\\%s\\temp\\'%username    
#         flag=despath+'tag.txt'
#         with open(flag,'r') as f:
#             for i in f:
#                 if i == '0':
#                     exit()
        case.confDataBase(configList[1],configList[2],configList[6])
        

    @classmethod
    def tearDownClass(self):
        os.system('taskkill /IM MainApp.exe /F')
    def test1_Login(self):
        case.login(configList[1],configList[2],configList[3],configList[4])

    def test2_CreatPro(self):
        case.creat_pro(window_name,proName)
        
    def test3_LoadPro(self):
        case.unload_pro(window_name)
        case.load_pro(window_name, proName)
        
    def test4_ConfigEnviro(self):
        case.add_Bus(window_name)
        case.add_dev(window_name)
        case.add_tar(window_name,ip)
        tcp.add_TCP_Client_Interface(window_name,ip)
        tcp.add_TCP_Service_Interface(window_name)
        tcp.add_TCP_Signal(window_name)
        tcp.add_TCP_Case(window_name)
    def test5_RunCase(self):
        tcp.run_case(window_name)
        tcp.compareRes()
    
if __name__ == "__main__":
    unittest.main()