#! /usr/bin/env python
#coding=GB18030
from pywinauto import mouse as ms
import auto_lib as pywin 
import time
import locFun as location
app=pywin.Pywin()

#添加客户端接口
@location._getName
def add_TCP_Client_Interface(window_name):
    app.connect(window_name)
    app._wait_child(window_name, u'添加接口', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER', 1)
#添加IP
    app.click(window_name, 'Edit11')
    app.Sendk('RIGHT', 1)
    time.sleep(1)
    app.input(window_name, 'Edit11', '19')
    app.Sendk('2', 1)
    app.input(window_name, 'Edit12', '16')
    app.Sendk('8', 1)
    app.input(window_name, 'Edit13', '1')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit14', '5')

#设置端口
    app.click(window_name, 'Edit9')
    app.input(window_name, 'Edit9', '^a')
    app.input(window_name, 'Edit9', '6060')
    app.click(window_name, u'确定')   #确定
    app._wait_not_child(window_name, u'添加接口', 'ready', 10, 2)
    
#添加服务端接口
@location._getName
def add_TCP_Service_Interface(window_name):
    ms.right_click(coords=(923,510))
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app._wait_child(window_name, u'添加接口', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER', 1)
    app.click(window_name, u'确定')   #确定
    app._wait_not_child(window_name, u'添加接口', 'ready', 10, 2)
    
#添加信号
@location._getName
def add_TCP_Signal(window_name):
    ms.press(button='left', coords=(902, 456))
    ms.move(coords=(940, 456))
    ms.release(button='left', coords=(940, 456))
    app._wait_child(window_name, u'编辑__信号__signal', 'ready', 10, 2)
    app.click(window_name, 'ComboBox5')
    time.sleep(1)
    app.input(window_name, 'ComboBox5', 'i_block')  #添加数据结构
    app.click(window_name, u'确定')   #确定
    app._wait_not_child(window_name, u'编辑__信号__signal', 'ready', 10, 2)

#新建测试用例
@location._getName
def add_TCP_Case(window_name):
    app.click(window_name, 'TreeItem11')
    app._wait_child(window_name, u'测试用例集', 'ready', 10, 2)
    app.right_click(window_name, 'TreeView2')
    app.Sendk('DOWN', 2)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'新建用例分类', 'ready', 10, 2)
    app.click(window_name, u'确定')
#     app._wait_not_child(window_name, u'新建用例分类', 'ready', 10, 2)
    app._wait_child(window_name, u'用例分类', 'ready', 10, 2)
    app.right_click(window_name,u'用例分类')    #测试用例root
    time.sleep(1)
    app.Sendk('DOWN',4)
    app.Sendk('ENTER',1)
    app._wait_child(window_name, u'新建测试用例', 'ready', 10, 2)
#     app.Sendk('TAB',2)
    app.input(window_name, 'Edit1', 'content2')     #输入用例名
    app.click(window_name,u'确定')
    app.click(window_name,u'用例分类')
    app.Sendk('RIGHT',1)
    app.Sendk('DOWN',1)
    app._wait_child(window_name, 'content2', 'ready', 10, 2)
    

#添加信号
    app.click(window_name, u'测试用例变量')
    app.click(window_name, u'添加信号变量')
    app._wait_child(window_name, u'选择信号对话框', 'ready', 10, 2)
    ms.click(coords=(602,450))      #选中信号
    app.click(window_name, u'确定')
    app._wait_child(window_name, 'signal', 'ready', 10, 2)


#测试用例编辑    
    app.click(window_name, u'测试用例编辑')
    app.right_click(window_name, 'TreeItem18')      #右键"主流程"
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)   #快速生成
    app._wait_child(window_name, u'删除', 'ready', 10, 2)
    ms.press(button='left',coords=(600,229))
    ms.move(coords=(661, 646))
    ms.release(button='left', coords=(661, 646))
    app.click(window_name, u'确定')
    app._wait_child(window_name, u'发送[signal]', 'ready', 10, 2)

@location._getName
def run_case(window_name):
    app.click(window_name,u'开始')
    app._wait_child(window_name, u'开始新测试', 'ready', 10, 2)
    app.click(window_name, 'content2')
    app.click(window_name, 'ComboBox4')
    time.sleep(1)
    app.Sendk('UP', 2)
    app.Sendk('ENTER', 1)    
    app.click(window_name, u'开始')
    time.sleep(2)
    app.click(window_name, u'是')
#     app._wait_child(window_name, u'继续', 'ready', 10, 2)
    time.sleep(10)
    app._wait_not_child(window_name, u'继续', 'ready', 10, 2)
    time.sleep(2)
    app.click(window_name,u'运行')
    time.sleep(2)
    app.click(window_name, u'停  止')
if __name__=='__main__':
    pass
    app=pywin.Pywin()
    window_name =u'QuiKLab V3.0'
#     time.sleep(2)
    app.connect(window_name)
    add_TCP_Client_Interface(window_name)
#     add_TCP_Service_Interface(window_name)
#     add_TCP_Signal(window_name)
#     add_TCP_Case(window_name)
#     run_case(window_name)