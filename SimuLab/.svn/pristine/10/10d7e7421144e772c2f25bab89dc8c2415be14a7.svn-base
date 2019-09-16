#! /usr/bin/env python
#coding=utf-8
import os,sys
dir = os.getcwd().split('\\')[-1]
if dir == 'interfaceCase' or dir == 'uiCase':
    envDir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
elif dir == 'trunk':
    envDir = os.path.abspath(os.path.join(os.getcwd(),".."))   
else:
    envDir = os.path.abspath(os.path.join(os.getcwd(),"../.."))
sys.path.append(envDir)