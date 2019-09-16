#! /usr/bin/env python
#coding=GB18030
import getpass
import os
import re
import shutil
import threading
import time

from pywinauto import application 

from casebase import getProcessID
import locFun as location

#-------------从服务器下载最新测试版本到e盘-------------
def cpFile():
    path='\\\\192.168.1.226\\测试版本\\PC14421'
    filelist=os.listdir(path)
    _list=[]
    for t in filelist:
        p=r'\d\.0\.0\.\d*'
        m=re.findall(p,t)
        if m:
            ver=m[0].split('.')[-1]
            _list.append(ver)
    for t in filelist:
        if max(_list) in t:
            if t.split('.')[-1] == 'exe':
                srcFile=path+'\\'+t
                print "Test rev is:",t
                print "Copying Installer..."
                os.system('copy %s %s'%(srcFile,despath))
                with open('temp','w') as f:
                    f.write('1')
                return t
username = getpass.getuser()
despath='C:\\Users\\%s\\temp\\'%username   
if not os.path.exists(despath):             #建立临时安装文件夹
    os.mkdir(despath)
fileName=cpFile()           #执行copy，并返回安装程序名称
appFile=despath+'appFile.txt'   
with open(appFile,'w') as f:
    f.write(fileName)

#-------------静默安装-------------
def _install():
    filePath=despath+fileName
#     print filePath
    os.system('%s /silent'%filePath)

#-------------静默卸载-------------
def _uninstall():
    os.system('D:\QuiKLab3.0\unins000.exe /silent')
    path='D:\QuiKLab3.0\MainApp.exe'
    if os.path.exists(path):
        print "unInstall fail!!!"
    else:
        print "unInstall successful！！！"
        
        
#-------------检查安装是否成功-------------
def _check(window_name):
    app=application.Application()
    i=1
    while i<20:
        if os.path.isfile('temp'):
            os.remove('temp')
            break
        time.sleep(1)
        i+=1
    time.sleep(5)
    try:
        app.connect(title = window_name)        #获取安装窗口连接
    except:
        print "connect failed!"
        exit()
    app[window_name].wait('exists', 10, 2)      #判断安装窗口是否存在
    flag=despath+'tag.txt'
    with open(flag,'w') as f:
        f.write('1')   
    try:
        app[window_name].wait_not('exists', 60, 2)   #判断是否安装完成
        path='D:\QuiKLab3.0\MainApp.exe'
        if os.path.exists(path):                    #安装的执行文件是否存在
            print 'Install Successfully!'

        else:
            print 'Install fail'
            with open(flag,'w') as f:
                f.write('0')   
            exit()
    except:
        print "Install Fail"
        with open(flag,'w') as f:
            f.write('0') 
        killName=fileName.replace('exe','tmp')      
        print "kill process:",killName
        os.system('taskkill /IM %s /F'%killName)        #安装失败关闭安装进程
        exit()

        
@location._getName 
def _checkInstall():
    threads=[]
    t1 = threading.Thread(target=_install)
    threads.append(t1)
    t2 = threading.Thread(target=_check,args=(u'安装 - QuiKLab',))
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
#     print threading.enumerate()
    for i in threads:
        i.join() 
if __name__=='__main__':
    pass
    _checkInstall()
