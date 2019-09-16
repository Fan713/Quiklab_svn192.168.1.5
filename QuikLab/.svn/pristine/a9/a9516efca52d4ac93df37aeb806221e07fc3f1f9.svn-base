#!/user/bin/env python
#coding=GB18030

'''
Created on 2019年5月15日
@author: ZF
*************************************************************************************************************************************
此脚本用于检测Quiklab已接收的（以txt文件形式存储）数据的正确性；
原理：根据发送文本text的长度，重新均分接收数据txt文件每行内容长度，并将均分后的内容进行匹配；
此方法存在瓶颈：
    1.若text内容完全一致，如："11 11 11 11",若中间行存在缺失内容时，匹配每行内容时，自动均分行内容长度，导致错误行匹配结果正确；
    2.若text内容不一致，如："AA BB CC DD ",若中间某一行内容缺失，如："AA BB "，匹配每行内容时，会自动将缺失行的下一行的部分内容自动补至缺失行，导致从缺失行开始之后的行内容匹配失败。
*************************************************************************************************************************************
'''
import re
import linecache

text=raw_input('请输入发送信号内容(需与测试用例中实际发送信号数据一致):')
len1 = len(text)
path0 =raw_input('请输入接收数据txt存放路径:')
a=''

with open(path0,'r') as file0:              #读文件
    for line in file0:
        line=line.strip('\r\n')
        a = a+line
    a = re.sub(r'(.{%d})'%len1,'\\1\n',a)    #按照多少个字符换行
    print a
with open(path0,'w') as file0:              #将a覆盖至file0
    file0.write(a)
print linecache.getlines(path0)             #获取覆盖后所有行内容


t=len(a)/len1
print '总共发送数据行数:',t
for i in range(1,t+1):  
    count1 = linecache.getline(path0,i)       #获取每行内容
    if count1.strip('\n') == text:
        pass
    else:
        print '第%d行不匹配'%i,count1




