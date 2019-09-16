#! /usr/bin/env python
#coding=GB18030
import psutil
import os
import sys
import time
import process 
import win32com.client
import pandas as pd

def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)
    if len(processCodeCov) > 0:
        pass
    else:
        print "%s is not exist"%pro_name
        return 0
    
def get_PID():
    _list=process.process_get_modules()
    for i in range(len(_list)):
        if "MainApp" in _list[i][1]:
            PID=_list[i][0]
            return PID
try:
    os.remove('./CPUresult.txt')
except:
    print "No result"
PID=get_PID()
c=[]
m=[]
try:
    def get_cpu_info():
        reload(sys)
        i = 0
        while True:
            if check_exist('MainApp.exe')==0:
                break
            text = open('./CPUresult.txt', 'a')
            i = i + 1
            cpucount = psutil.cpu_count(logical=True)
#             print cpucount

            process = psutil.Process(int(PID))
            cpupercent = process.cpu_percent(interval=1)
#             print cpupercent
            cpu = int(cpupercent / cpucount)
            mem = process.memory_percent()
            c.append(cpu)
            m.append(mem)
            if cpu <= 50:
                print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'         ' +str(cpu) + '                    ' + str(mem)  
#                 print>> text, u'CPU使用率%s' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                text.close()
            else:
                print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'         ' +str(cpu) + '                    ' + str(mem)
#                 print>> text, u'CPU使用率%s' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                text.close()
                with open('./log.txt','r') as tf:
                    lines=tf.readlines()
                    fun_name=lines[-1].split(' ')[1]
                over=open('overuage.txt','a')
                over.write(fun_name)
                over.write('\n')
                over.close()
    print '进程%s的' % PID + 'CPU监控已经运行，结果将在result.txt生成'
    time.sleep(1)
    print "--------------------------------------------------------------------"
    print '测试时间'+'                                                       '+'CPU使用率(%)'+ '                 '+'MEM占用率(%)'+'                                                       '+'测试时间'
    print get_cpu_info()
    print c
finally:
    print  u'进程%s的' % PID + u'已经结果'
    info={u'CPU使用率':c,
          u'MEM使用率':m}
#     info = repr(info).decode('string_escape')
    df=pd.DataFrame(info)
    print df
    df.to_excel(r'./usage.xls')
