#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年3月19日

@author: KLJS276
'''
'''
功能:判断预期结果和实际结果是否相等
'''

import sys

from logging import Logger

import loggingWriter


logFile = loggingWriter.Logger()

def isEqual(expectResult,actualResult,pyFileName,trueMessage,falseMessage):
    if expectResult != actualResult:
        logFile.logWriter(pyFileName,falseMessage)
        assert expectResult == actualResult
    else:
        logFile.logWriter(pyFileName,trueMessage)
