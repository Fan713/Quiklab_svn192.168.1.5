#! /usr/bin/env python
#coding=GB18030
import os
import sys
import time

from PIL import ImageGrab


def _exception(func):
    def wrapper(*args):
        try:
            func(*args)
        except:
            path = sys.path[0] + r"\report"
            if not os.path.exists(path):
                path = os.path.abspath("..") + r"\report"
                print path
    
            if not os.path.exists(path):
                path = os.path.abspath("..\..") + r"\report"
                print path
            _file= path + '\log.txt'
            with open(_file,'a') as f:
                f.write('fail')
                f.write('\n')
            now=time.strftime('%Y%m%d_%H%M%S',time.localtime((time.time())))
            im = ImageGrab.grab()
            lists =[]
            fileNames = os.listdir(path)
            for fileName in fileNames:
                if os.path.isdir(os.path.join(path,fileName)):
                    lists.append(fileName)
                     
            lists.sort(key=lambda fn:os.path.getmtime(path +r"/" + fn))
            file_new = os.path.join(path,lists[-1])
            picFile= file_new + '/' + now+'.png'
            print "screenshot:" + picFile,len("screenshot:" + picFile)    #用于测试报告中增加截图
            im.save(picFile)
            exit()

    return wrapper

if __name__=='__main__':
    pass