#! /usr/bin/env python
#coding=GB18030
import psutil
import os
import time
from casebase import getProcessID
import win32com.client
from pywinauto import application
import threading
#-----------------判断进程是否存在-------------------------
def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)
    if len(processCodeCov) > 0:
        return 1
    else:
        print "%s is not exist"%pro_name
        return 0
    
#-----------------获得进程ID-------------------------
def get_PID():
    _list=getProcessID.process_get_modules()
    for i in range(len(_list)):
        if "MainApp" in _list[i][1]:
            PID=_list[i][0]
            return PID

#-----------------获得CPU和MEM占用率-----------------------
def get_usage():
    app=application.Application(backend='uia')
    flag=0
#     print os.getcwd()
    time.sleep(15)
    with open('../appFile.txt','r') as f:
        for line in f:
            fileName=line.replace('exe','tmp')
#             print fileName
    while check_exist(fileName):
        time.sleep(2)
    time.sleep(8) 
    with open('tag.txt','r') as f:
        for i in f:
            if i == '0':
                print i
#                 os._exit(0)
                exit()
    window_name = r'QuiKLab V3.0'
#-------------判断QuikLab3.0是否弹出，并且执行case的线程是否在执行------------------
    while flag == 0:
        mark=0
        try:
            for i in threading.enumerate():
                if 'Thread-1' in str(i):
                    mark=1
            if mark == 0:
                print "Quiklab exception!"
                os._exit(0)
            app.connect(title = window_name) 
            flag=1
        except:
            time.sleep(2)
            flag=0
    if os.path.exists('./CPUresult.txt'):
        os.remove('./CPUresult.txt')
        os.remove('./MEMresult.txt')
    PID=get_PID()
    if PID is None:
        print "QuikLab didn't start!"
        exit()
    c=[]
    m=[]
    try:
        def get_cpu_info():
            i = 0
            print "getting Usage... "
            while True:
                if check_exist('MainApp.exe')==0:
                    break
                i = i + 1
                cpucount = psutil.cpu_count(logical=True)   #CPU核的个数
                process = psutil.Process(int(PID))  #根据PID监视进程
                cpupercent = process.cpu_percent(interval=1)
                cpu = int(cpupercent / cpucount)
                mem = process.memory_percent()
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                c.append(cpu)
                m.append(mem)
                Cpu_text = open('./CPUresult.txt', 'a')
                Mem_text = open('./MEMresult.txt', 'a')
                if cpu <= 50:
#                     print u'CPU usage is %s' % cpu + '         ' + now
#                     print u'MEM usage is %s' % mem + '         ' + now
                    print>> Cpu_text, 'CPU使用率:%s%%' % cpu + '    ' + now
                    print>> Mem_text, 'MEM使用率:%s%%' % mem + '    ' + now
                    Cpu_text.close()
                    Mem_text.close()
                else:
                    print 'CPU使用率:%s%%,占用率过高' % cpu + '    ' + now
                    print 'MEM使用率:%s%%' % mem + '    ' + now
                    print>> Cpu_text, 'CPU使用率%s%%,占用率过高' % cpu + '    ' + now
                    print>> Mem_text, 'MEM使用率:%s%%,占用率过高' % mem + '   ' + now
                    Cpu_text.close()
                    Mem_text.close()
#         print 'Result will be in result.txt'
        time.sleep(1)
        print "-------------------------------------------------"
        get_cpu_info()
    except:
        pass
    finally:
        if max(c) > 50:
            with open('./CPUresult.txt','a') as f:
                print "CPU占用过高，Performance Test Fail"
                f.write("CPU占用过高，Performance Test Fail")
        else:
            with open('./CPUresult.txt','a') as f:
                print "Performance Test Pass"
                f.write('Performance Test Pass')
        print  u'进程%s' % PID + u'已经结束'
if __name__=='__main__':
    get_usage()