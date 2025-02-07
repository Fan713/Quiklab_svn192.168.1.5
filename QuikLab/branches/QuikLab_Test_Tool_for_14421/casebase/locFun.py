#! /usr/bin/env python
#coding=GB18030
import time
import os

#-------------获取当前执行函数名称并判断执行是否正常-------------
def _getName(func):
    def wrapper(*args,**kwargs):
        path='../report'
        if not os.path.exists(path):
            os.chdir('report')
        _file='../report/log.txt'
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