#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年4月8日

@author: KLJS276

功能：获取电脑相关信息
'''
import os
import socket  # 导入socket模块


class getHostInfo(object):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     #创建socket对象(IPv4,无连接UDP)
        
    def getHostIp(self):
        #获取主机IP地址
        try:
            self.s.connect(('192.168.1.64',80))     #建立连接
            ip = self.s.getsockname()[0]
        finally:
            self.s.close()
        return ip
    
    def getSys32Or64bit(self):
        #获取系统为32/64位
        return "PROGRAMFILES(X86)" in os.environ     #如果是64位系统返回True
        

if __name__ == '__main__':
    hostInfo = getHostInfo()
    print (hostInfo.getHostIp())
#     print (hostInfo.getSys32Or64bit())
