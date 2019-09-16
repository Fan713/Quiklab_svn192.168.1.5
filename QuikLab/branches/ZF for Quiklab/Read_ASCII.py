#! /usr/bin/env python
#coding=GB18030

#将xml文件内容转换成十六进制
def str_to_hex(s):
    return''.join([hex(ord(c)).replace('0x','') for c in s])    #字符串转换成十六进制
path0=r'D:\QuiKLab3.0\configures\Default\viewconfig.xml'
a=''
with open(path0,'r') as file0:
    for line in file0:
        line=line.strip('\r\n')     #去掉空格、换行
        a=a+str_to_hex(line)        #将每行内容连接起来     
    a=a.upper()   #将字母由小写转为大写
    print a
                               
#读取Quiklab解析出来的内容
path='D:\QuiKLab3.0\configures\Default\original.txt'  
with open(path,'r') as file:
    for line in file:
        b=line.replace('0D 0A ','').replace(' ','') #去掉0D 0A 空格
        print b  

if b in a:
    print True
else:
    print False