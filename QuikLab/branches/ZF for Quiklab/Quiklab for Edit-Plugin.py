#! /usr/bin/env python
#coding=GB18030
from pywinauto import application
from pywinauto import mouse as ms 
import pyautogui as py
#import pywinauto #调用pywinauto
import auto_lib as pywin
import SendKeys
import time
import os
import try2
from pywinauto.mouse import right_click

#QuiKLab登录
# tl_dir = r'D:\Program Files\QuiKLab3.0'
# tl_name = r'D:\Program Files\QuiKLab3.0\MainApp.exe'
# try2.login(tl_dir,tl_name,'1')              
# time.sleep(2)  
#    
# #加载项目    
window_name =u'QuiKLab V3.0'  
app=pywin.Pywin()   #实例化
# try2.load_pro(window_name,'ZF-ICD-TEST')
# time.sleep(2)

#新建用例分类
app.connect(window_name)
# app.click(window_name,u'用例分类') #点击已创建好的用例分类
# app.Sendk('RIGHT')
# app.click(window_name,u'TEST') #点击TEST测试用例
# #添加用例变量
# app.click(window_name,u'测试用例变量')
# app.click(window_name,u'添加信号变量') 

#勾选信号
# app.click(window_name,'TCP/IP')
# print py.position()
# x=py.position()[0]
# y=py.position()[1]
# checkbox_x=x-92
# checkbox_y=y
# py.moveTo(checkbox_x, checkbox_y)
# ms.click(coords=(checkbox_x,checkbox_y))
# app.click(window_name,u'确 定')

# #编辑测试用例
# app.click(window_name,'TabItem0') #点击测试用例编辑
# right_click(coords=(774,318)) #鼠标右击

#编辑测试用例--快速生成
# app.Sendk('DOWN')
# app.Sendk('UP')
# app.Sendk('ENTER') #选择快速生成
# app.click(window_name,'ComboBox1')
# app.Sendk('DOWN')
# app.Sendk('ENTER')
# app.click(window_name,'ComboBox1')
# app.Sendk('UP')
# app.Sendk('ENTER')  #快速生成类型选择循环发送/接收信号
# 
# app.click(window_name,'Edit1')
# app.input(window_name,'Edit1','^A')
# app.input(window_name,'Edit1','50')  #设置循环次数

app.click(window_name,'TCP/IP')
print py.position()
x1=py.position()[0]
y1=py.position()[1]
checkbox_x=x1
checkbox_y=y1+388
ms.press(button='left', coords=(x1, y1))
py.moveTo(checkbox_x, checkbox_y)
ms.release(button='left', coords=(checkbox_x, checkbox_y)) 
app.click(window_name,u'确 定')


# #编辑测试用例—-新建动作
# app.Sendk('DOWN')
# app.Sendk('RIGHT')
# for i in range(8):
#     app.Sendk('DOWN')
# app.Sendk('ENTER')
# app.click(window_name,u'确 定') #新建动作—循环
# app.Sendk('DOWN')






    
 