#! /usr/bin/env python
#coding=GB18030
import os
import re
import time
import threading
import locFun as location
from pywinauto import application 

#-------------从服务器下载最新测试版本到e盘-------------
def cpFile():
    path='\\\\192.168.1.226\\测试版本\\PC14421'
    despath='e:\\'
    filelist=os.listdir(path)
    _list=[]
    for t in filelist:
        p=r'\d\.0\.0\.\d*'
        m=re.findall(p,t)
        ver=m[0].split('.')[-1]
        _list.append(ver)
    print _list
    print max(_list)
    for t in filelist:
        if max(_list) in t:
            if t.split('.')[-1] == 'exe':
                srcFile=path+'\\'+t
                print srcFile
                print "Copying Installer..."
                os.system('copy %s %s'%(srcFile,despath))
                return t
            
fileName=cpFile()
with open('appFile.txt','w') as f:
    f.write(fileName)

#-------------静默安装-------------
def _install():
    os.system('E:\%s /silent'%fileName)

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
    time.sleep(5)
    try:
        app.connect(title = window_name)
    except:
        print "connect failed!"
        exit()
    app[window_name].wait('exists', 10, 2)
    flag='tag.txt'
    with open(flag,'w') as f:
        f.write('1')   
    try:
        app[window_name].wait_not('exists', 60, 2)
        path='D:\QuiKLab3.0\MainApp.exe'
        if os.path.exists(path):
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
        print killName
        os.system('taskkill /IM %s /F'%killName)
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
