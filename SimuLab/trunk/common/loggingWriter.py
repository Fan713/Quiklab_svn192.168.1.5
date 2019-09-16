#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年3月19日

@author: KLJS276

功能：生成日志文件
'''
import os
import sys

import logging

from trunk.common import searchFile


class Logger(object):
    
    def __init__(self):
        self.terminal = sys.stdout
        
    def write(self,message):
        #将print的信息重定向至文件       
        fileDir = searchFile.searchFile(r"\report")
        fileUrl = fileDir + r'\out.txt'
        self.log = open(fileUrl,"a")
        self.log.write(message)
        self.log.close()
    
    def logWriter(self,pyfilename,message):
        #生成log文件
        LOG_FORMAT = "%(asctime)s " + str(pyfilename) + " %(message)s"         #定义log文件内容格式（异常发生的时间/py文件/信息）
        DATE_FORMAT = "%Y-%m-%d %H:%M:%S"                                      #异常发生时间的格式
        fileDir = searchFile.searchFile(r"\report") 
        fileUrl = fileDir + r'\test.log'
        logging.basicConfig(format = LOG_FORMAT,datefmt= DATE_FORMAT,filename=fileUrl,level = logging.DEBUG,filemode='a')  #指定要记录日志的级别，日志格式，日期格式，输出位置
        logging.debug(message)
        logging.shutdown()             #输出的信息
        
if __name__ == "__main__":
    sys.stdout = Logger()
    print (4,45)
    
    
    
    

