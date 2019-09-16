#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年4月26日

@author: KLJS276

功能：从注册表获取SimuLab安装路径
'''
import _winreg

import getHostInfo


hostInfo = getHostInfo.getHostInfo()
sysDigit = hostInfo.getSys32Or64bit()

def getInstallDir(para):
    if sysDigit == True:                  #系统为64位系统获取key值
        key=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"Software\Wow6432Node\SimuLab\v3.0")
    else:
        pass
    value,type = _winreg.QueryValueEx(key,para)       #根据键获取值
    return value

if __name__ == "__main__":
    print getInstallDir("RootPath")
    
    
