#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年3月25日

@author: KLJS276

功能：读取ini格式的配置文件
'''
import ConfigParser
import os
import sys

from trunk.common import searchFile


class readIniConfig(object):
    def __init__(self, testType):
        self.testType = testType
       
    def readConfig(self):
        readini = ConfigParser.ConfigParser()
        fileDir = searchFile.searchFile(r"\data")
        _file = fileDir + r'\mainConfig.ini' 
        readini.read(_file)       #读取配置文件
        section = readini.sections()            #获取ini文件内的所有section,以列表形式返回
        _list=[]
        for sectionInfo in section:
            if sectionInfo in self.testType:
                for key in readini.options(sectionInfo):      #获取section的所有option
                    if readini.get(sectionInfo,key):          #获取section中option的值，返回类型是string类型
                        _list.append(readini.get(sectionInfo,key))
                    else:
                        print "Configure file wrong!Please check it."
                        exit()
        return _list
    
if __name__ == "__main__":
    pass

        