#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年4月26日

@author: KLJS276

功能：查找data/report文件夹
'''
import os

def searchFile(packageName):
    fileDir = os.getcwd() + packageName
    fileDirBool = True
    while fileDirBool:
        if not os.path.exists(fileDir):
            os.chdir('../')
            fileDir=os.getcwd() + packageName
        else:
            fileDirBool = False
    return fileDir
