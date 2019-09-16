#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time


#-------------获取当前执行函数名称并判断执行是否正常-------------
def _getName(func):
    def wrapper(*args,**kwargs):
        path = sys.path[0] + r"\report"
        if not os.path.exists(path):
            path = os.path.abspath("..") + r"\report"
     
        if not os.path.exists(path):
            path = os.path.abspath("..\..") + r"\report"
            
        _file=path+'/log.txt'
        with open(_file,'a') as f:
            t=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
            f.write('%s '%t)
            f.write(func.__name__)
            f.write(' ')
            print func.__name__
        func(*args,**kwargs)
        with open(_file,'a') as f:
            f.write('pass')
            f.write('\n')
    return wrapper

if __name__=='__main__':
    pass