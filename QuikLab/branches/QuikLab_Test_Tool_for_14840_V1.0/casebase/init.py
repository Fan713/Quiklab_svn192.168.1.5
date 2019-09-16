#! /usr/bin/env python
#coding=GB18030
import getpass
import os
import shutil
import sys
import time
import case_wrapper
from checkName import check


def _init():
#检查日志文件是否存在
#     path='../report'
    path = sys.path[0] + r"\report"
    if not os.path.exists(path):
        path = os.path.abspath("..") + r"\report"

    if not os.path.exists(path):
        path = os.path.abspath("..\..") + r"\report"
    files=os.listdir(path)
    for i in files:                     #删除report下所有文件
        d_path=os.path.join(path,i)
        if os.path.isfile(d_path):
            os.remove(d_path)
    username = getpass.getuser()
    filePath='C:\Users\%s\QuiKLab3\\runtime\\'%username
    despath='C:\\Users\\%s\\temp\\'%username
    fileName=time.strftime('%Y_%m_%d',time.localtime((time.time()))) +'.log'   
    fileRes=filePath+fileName
    if os.path.exists(fileRes):             #删除执行QuikLab时产生的日志
        os.remove(fileRes)
    if os.path.exists(despath):             #删除临时安装文件下载文件夹
        shutil.rmtree(despath)

#检查用户名和工程名是否存在
    tpList=case_wrapper.readIniConfig('QuikLab3.0')
    ck=check()
    if ck.ckUname(tpList[3]) == 1 and ck.ckProName(tpList[5]) == 1:
        pass
    else:
        exit()
    print "Init finish!"
if __name__=='__main__':
    _init()


