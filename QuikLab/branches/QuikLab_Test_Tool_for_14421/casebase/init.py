#! /usr/bin/env python
#coding=GB18030
import os
from checkName import check
import case_wrapper
import getpass
import time
def _init():
#检查日志文件是否存在
    path='../report'
    if not os.path.exists(path):
        os.chdir('report')
    files=os.listdir(path)
    for i in files:
        d_path=os.path.join(path,i)
#         print d_path
        log='../report/log.txt'
        if os.path.exists(log):
            os.remove(log)
    username = getpass.getuser()
    filePath='C:\Users\%s\QuiKLab3\\runtime\\'%username
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'
    fileRes=filePath+fileName
    if os.path.exists(fileRes):
        os.remove(fileRes)
 
#检查用户名和工程名是否存在
    tpList=case_wrapper.readIniConfig('QuikLab3.0')
    ck=check(tpList[3],tpList[5])
    if ck.ckUname() == 1:
        pass
    else:
        print 'No User'
        exit()
    if ck.ckProName() == 1:
        pass
    else:
        print "Pro had exist!"
        exit()
    print "Init finish!"
if __name__=='__main__':
    _init()


