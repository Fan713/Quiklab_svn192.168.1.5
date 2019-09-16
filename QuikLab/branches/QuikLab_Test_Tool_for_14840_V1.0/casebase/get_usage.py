#! /usr/bin/env python
#coding=GB18030
import getpass
import os, sys
import shutil
import threading
import time

import psutil
from pywinauto import application
import win32com.client

from casebase import getProcessID
import pandas as pd


#-----------------�жϽ����Ƿ����-------------------------
def check_exist(pro_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process where Name="%s"'%pro_name)
    if len(processCodeCov) > 0:
#         print "exist"
        return 1
    else:
        print "%s is not exist"%pro_name
        return 0
    
#-----------------��ý���ID-------------------------
def get_PID():
    _list=getProcessID.process_get_modules()
    for i in range(len(_list)):
        if "MainApp" in _list[i][1]:
            PID=_list[i][0]
            return PID
        
#----------------���report·��----------------------
def get_path():
    path = sys.path[0] + r"\report"
    if not os.path.exists(path):
        path = os.path.abspath("..") + r"\report"
        print path

    if not os.path.exists(path):
        path = os.path.abspath("..\..") + r"\report"
        print path
    return(path)

#-----------------���CPU��MEMռ����-----------------------
def get_usage():
    app=application.Application(backend='uia')
    flag=0
# #     print os.getcwd()
#     time.sleep(20)
#     username = getpass.getuser()
#     despath='C:\\Users\\%s\\temp\\'%username
#     appFile=despath+'appFile.txt'
# #     print "read appfile"
#     with open(appFile,'r') as f:
#         for line in f:
#             fileName=line.replace('exe','tmp')
# #     os.remove('appFile.txt')
#     while check_exist(fileName):
#         time.sleep(2)
#     time.sleep(8) 
#     print os.getcwd()
#     tag=despath+'tag.txt'
#     with open(tag,'r') as f:
#         for i in f:
#             if i == '0':
#                 print i
# #                 os._exit(0)
#                 exit()
# #     os.remove('tag.txt')
    window_name = r'QuiKLab V3.0'
    
#-------------�ж�QuikLab3.0�Ƿ񵯳�������ִ��case���߳��Ƿ���ִ��------------------
    while flag == 0:
        mark=0
        try:
            for i in threading.enumerate():
                if 'Thread-1' in str(i):
                    mark=1
            if mark == 0:
                print "Quiklab exception!"
                username = getpass.getuser()
                despath='C:\\Users\\%s\\temp\\'%username
                if os.path.exists(despath):
                    shutil.rmtree(despath)
                os._exit(0)  #��tcpSmoke�쳣�˳�����cpu�߳��˳���ɾ����ʱ��װ�ļ�
            app.connect(title = window_name) 
            flag=1  #QuikLab�����������flag��Ϊ1����ʼ��ȡcpu usage
        except:
            time.sleep(2)
            flag=0
#             print "error"
    _path=get_path()+'\Usage.txt'       #�趨����usage.txt��·��
#     print _path
    if os.path.exists(_path):
        os.remove(_path)
    PID=get_PID()
#     if PID is None:
#         print "QuikLab didn't start!"
#         exit()
    c=[]
    m=[]
    t=[]
    try:
        def get_cpu_info():
            i = 0
            print "getting Usage... "
            while True:
                if check_exist('MainApp.exe')==0:
                    break
                i = i + 1
                text = open(_path, 'a')
                cpucount = psutil.cpu_count(logical=True)   #CPU�˵ĸ���
                process = psutil.Process(int(PID))  #����PID���ӽ���
                cpupercent = process.cpu_percent(interval=1)    #�趨��ȡCPU�ļ��ʱ��Ϊ1s
                cpu = int(cpupercent / cpucount)                
                mem = process.memory_percent()
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                c.append(cpu)
                m.append(mem)
                t.append(now)
                if cpu <= 50:
                    print >> text, now+'         ' +str(cpu) + '                    ' + str(mem)  
                    text.close()
                else:
                    print >> text, now+'         ' +str(cpu) + '                    ' + str(mem)
                    text.close()
                    #cpuռ���ʳ���50ʱ����ȡ��ǰִ�е�ģ�����ƣ�д��overusage.txt
                    Log_file=get_path()+'log.txt'
                    with open(Log_file,'r') as tf:
                        lines=tf.readlines()
                        fun_name=lines[-1].split(' ')[1]
                    over_file=get_path()+'\overusage.txt'
                    over=open(over_file,'a')
                    over.write(fun_name)
                    over.write('\n')
                    over.close()
        print '����%s��' % PID + 'CPU����Ѿ����У��������result.txt����'
        print "-------------------------------------------------"
        text = open(_path, 'a')
        print >> text,'����ʱ��'+'                                                       '+'CPUʹ����(%)'+ '                 '+'MEMռ����(%)'+'                                                       '+'����ʱ��'
        text.close()
        get_cpu_info()
    except:
        pass
    finally:
#         if max(c) > 50:
#             with open(_path,'a') as f:
#                 print "CPUռ�ù��ߣ�Performance Test Fail"
#                 f.write("CPUռ�ù��ߣ�Performance Test Fail")
#         else:
#             with open(_path,'a') as f:
#                 print "Performance Test Pass"
#                 f.write('Performance Test Pass')
        username = getpass.getuser()
        despath='C:\\Users\\%s\\temp\\'%username
        shutil.rmtree(despath)   #ɾ����ʱ��װ�ļ�
        print  u'����%s' % PID + u'�Ѿ�����'
        info={u'��¼ʱ��':t,
              u'CPUʹ����':c,
              u'MEMʹ����':m}
        df=pd.DataFrame(info)
        ex=get_path()+'\usage.xls'
        df.to_excel(ex)
        
if __name__=='__main__':
    get_usage()