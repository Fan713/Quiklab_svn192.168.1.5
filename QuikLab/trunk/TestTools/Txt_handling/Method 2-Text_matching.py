#!/user/bin/env python
#coding=utf-8
'''
Created on 2019年5月15日
@author: ZF
*********************************************************************************
此脚本用于检测Quiklab已接收的（以txt文件形式存储）数据的正确性；
原理：根据发送文本text的长度，若txt文件某行内容长度不等于text发送文本长度，自动添加下一行内容，并进行匹配；
           若txt文件行内容长度等于text发送文本长度，自动匹配;
优点：
          比Text_mathcing.py考虑异常情况更全面，内存占用更少;
*********************************************************************************    
'''
import re

text=raw_input('请输入发送信号内容(需与测试用例中实际发送信号数据一致):')
b = len(text)
path0 =raw_input('请输入接收数据txt存放路径:')
a=''
w=True 
i=0

##############获取txt文本行数##########################################################
# count=0
# thefile=open(path0,'rb')
# while True:
#     buffer=thefile.read()
#     if not buffer:
#         break
#     count+=buffer.count('\n')
# thefile.close()
# print count
####################################################################################

###########将text内容与txt文本每行内容进行匹配###############################################
row=0
with open(path0,'r') as file0:
    for line in file0:
        i=i+1
        line=line.strip('\r\n')
        if len(line) == b :
            if line.strip(' ')==text.strip(' '):
                w=True
                row=row+1
            else:
                w=False
                print '第%s行内容"%s"与text不匹配'%(i,line)
                break

        else:
            a=a+line
            if len(a) < b:                                #每行内容长度小于text内容长度，添加w=0标志位
                w = False
            elif len(a) > b:                              #每行内容长度大于text内容长度，添加w=0标志位
                w = False
                print '第%s行内容"%s"与text不匹配'%(i,a)
                break
            else:
                if a.strip(' ') == text.strip(' '):         #每行内容长度等于text内容长度，进行内容匹配
                    row=row+1
                    a=''                                    #将a置为空
                else:
                    w = False
                    print '第%s行内容"%s"与text不匹配'%(i,a)
                    break   
                                                       
if w == True:
    print '接收数据与发送数据匹配且一共接收到%d条数据'%row
else:
   print '第%s行内容"%s"与text不匹配'%(i,a)        
         




