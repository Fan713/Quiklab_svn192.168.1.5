#! /usr/bin/env python
#coding=GB18030
import ConfigParser
import logging
import os
import time
import xml.dom.minidom

from pywinauto import mouse as ms

import auto_lib as pywin 
import locFun as location
import exception as exp


app=pywin.Pywin()

@location._getName
def login(tl_dir,tl_name,uName,key):
    app.start(tl_dir,tl_name)
    window_name =u'登录--试验自动测试管理系统'
    app._wait_child(window_name, u'登 陆', 'exists', 10, 2)
    app.connect(window_name)
#输入用户名和密码
    app.input(window_name, 'Combox', uName)
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1', key)
    app.click(window_name, u'登 陆')
#判断QuikLab3.0是否弹出    
    window_name =u'QuiKLab V3.0'
    app._wait_child(window_name,u'新建项目','exists',10, 2)
    time.sleep(2)
    app.connect(window_name)
#新建项目
@location._getName 
def creat_pro(window_name,pro_name):
    app.click(window_name,u'新建项目')
    app._wait_child(window_name, u'新增', 'active', 10, 2)
    app.click(window_name, 'Edit2')
    app.input(window_name, 'Edit2', '^a')
    app.input(window_name,'Edit2',pro_name)
    app.click(window_name,u'确定') #确定

#加载项目
@location._getName 
def load_pro(window_name,pro_name):
    app.click(window_name,u'加载项目')
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    app.click(window_name, u'单机测试')
    app.click(window_name,u'确定')
    time.sleep(2)
    
#判断项目是否加载成功
    if 'name' in app.texts(window_name, 'statics2'):
        pass
    else:
        print "pro failed to load!!!"
        exit()
        
#--------------------删除项目--------------------------
def  delete_pro(window_name,pro_name):
    app.click(window_name,u'加载项目')
    app.click(window_name, 'Edit1')
    app.input(window_name,'Edit1',pro_name)
    ownerInfo = app.texts(window_name, "DataItem3")
    if ownerInfo != '':
        app.right_click(window_name, u'单机测试')
        app.Sendk("UP", 1)
        app.Sendk("ENTER", 1)
        app.click(window_name, u"确定")
    app.right_click(window_name, u'单机测试')
    app.Sendk("DOWN", 2)
    app.Sendk("ENTER", 1)
    app.click(window_name, u"确定")
    app.click(window_name, u"确定")

#卸载项目
@location._getName         
def unload_pro(window_name):
    app.click(window_name,u'卸载项目')
    time.sleep(1)
    app.click(window_name,u'是')
    if len(app.texts(window_name, 'statics2')) != 0:
        print 'unload failed!!!'
        exit()

#添加总线
@location._getName
def add_Bus(window_name):
    app.click(window_name,u'环境配置') #进入环境配置 
    ms.right_click(coords=(1577, 492))
    app.Sendk('DOWN', 1)
    app.Sendk('ENTER',1)
#判断弹出"添加总线"窗口 
    app._wait_child(window_name, u'添加总线', 'ready', 10, 2)
    app.click(window_name, 'ComboBox1')
    app.input(window_name, 'ComboBox1', 'tcp')#添加 TCP/IP协议
    app.Sendk('ENTER',1)
    app.click(window_name, u'确定') #确定

#添加设备  
@location._getName
def add_dev(window_name):
    app.right_click(window_name,'Pane2')
    app.Sendk('DOWN', 3)
    app.Sendk('ENTER',1) #选择添加设备
    app._wait_child(window_name, u'添加设备', 'ready', 10, 2)

#添加目标机
@location._getName
def add_tar(window_name):
    app.click(window_name, 'ComboBox1')
    time.sleep(1)
    app.Sendk('UP', 1)
    app.Sendk('ENTER', 1)

#添加IP
    app.click(window_name, 'Edit2')
    app.Sendk('RIGHT', 1)
    time.sleep(1)
    app.input(window_name, 'Edit2', '19')
    app.Sendk('2', 1)
    app.input(window_name, 'Edit3', '16')
    app.Sendk('8', 1)
    app.input(window_name, 'Edit4', '1')
    app.Sendk('.', 1)
    app.input(window_name, 'Edit5', '5')
    app.click(window_name, u'确定')#确定
    

@location._getName
def close(window_name,contorl):
    app.click(window_name,contorl)
    app.click(window_name,u"确定")
    
def closeLogin(window_name,contorl):
    app.click(window_name,contorl)
    
#界面配置数据库相关信息
@location._getName
def confDataBase(tl_dir,tl_name):
    app.start(tl_dir,tl_name)
    time.sleep(3)
    window_name =u'登录--试验自动测试管理系统'
    app._wait_child(window_name, u'登 陆', 'exists', 10, 2)
    app.connect(window_name)
    app.click(window_name, u"配置")     #点击配置按钮
    app.click(window_name, u"数据库")    #点击数据库
#     time.sleep(2)
    app.click(window_name, 'Edit3')        #选择IP地址输入框的第一位数字
    app.input(window_name, 'Edit3', '^a')  #全选输入框的第一位数字
    app.input(window_name, 'Edit3', '19')  #输入IP地址中的第一位数字
    app.Sendk('2', 1)
    app.click(window_name, 'Edit4')
    app.input(window_name, 'Edit4', '^a')
    app.input(window_name, 'Edit4', '16')
    app.Sendk('8', 1)
    app.click(window_name, 'Edit5')
    app.input(window_name, 'Edit5', '^a')
    app.input(window_name, 'Edit5', '1')
    app.click(window_name, 'Edit6')
    app.input(window_name, 'Edit6', '^a')
    app.input(window_name, 'Edit6', '22')
    app.Sendk('6', 1)
    app.click(window_name, u"应用")    #点击应用按钮
    app.click(window_name, u"确定")    #点击确定按钮
    app.click(window_name, u"确定")
    app.click(window_name, u'退出')    #点击退出
    
#----------------------------------------断言公共方法---------------------------------------------------
# 判断预期结果和实际结果是否相等
@exp._exception 
def isNotEqual(expectResult,acutalResult,pyfilename,message):
    if expectResult != acutalResult:
        assert expectResult == acutalResult

# 判断预期结果是否包含在实际结果中
# @exp._exception 
def isNotIN(expectResult,acutalResult,pyfilename,message):
    if expectResult not in  acutalResult:
        logWriter(pyfilename,message);
        assert expectResult in acutalResult
        
#-------------实际结果与预期结果比较，flag为True则预期为通过，反之则预期不通过-------------
#Example: isNotIn('假',logFile, True,'测试成功') logFile不含'假'，True条件为真，测试成功
# @exp._exception        
def isNotIn(expectResult,logFile,flag,Msg):
    with open(logFile,'r') as f:
        actualResult=f.read()
    if expectResult not in actualResult:
        if flag is True:
            pass
        else:
            assert expectResult in actualResult
    
#----------------------------------------文件/数据库操作-------------------------------------------------
#读取配置文件
def readIniConfig(softName):
#     print softName
    readini = ConfigParser.ConfigParser()
    _file = '../data/mainConfig.ini'
    if os.path.exists(_file):
        pass
    else:
        os.chdir('data')     
    readini.read(_file)
    section = readini.sections()
#     print section
    _list=[]
    for sectionInfo in section:
        if sectionInfo in softName:
            for key in readini.options(sectionInfo):
                _list.append(readini.get(sectionInfo,key))
#             softWindowName = readini.get(sectionInfo,"softWindowName")
#             softSetupdir = readini.get(sectionInfo,"softSetupDir")
#             softLabname = readini.get(sectionInfo,"softLabName")
#             softUserName = readini.get(sectionInfo,"softUserName")
#             softPwd = readini.get(sectionInfo,"softPwd")
#             softProjectName = readini.get(sectionInfo,"softProjectName")
#         _list=[softWindowName,softSetupdir,softLabname,softUserName,softPwd,softProjectName]
    return _list

#解析xml文件
def readXml(xmlFileUrl,elementName):
    elementData = []
    dom = xml.dom.minidom.parse(xmlFileUrl)  #打开xml文档
    root = dom.documentElement   #获取所有节点对象
    print root
    itemlist = root.getElementsByTagName(elementName)   #在集合中获取节点名称为elementName的节点对象
    for item in itemlist:
        un = item.firstChild.data
        elementData.append(un)    #获取对标签之间的数据
    return elementData

#记录log文件
def logWriter(pyfilename,message):
    LOG_FORMAT = "%(asctime)s " + str(pyfilename) + " %(message)s"         #定义log文件内容格式（异常发生的时间/py文件/信息）
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"                                      #异常发生时间的格式
    fileUrl = os.getcwd() + r'\report\test.log'
    if not os.path.exists(fileUrl):
        os.chdir('../')
        fileUrl=os.getcwd() + r'\report\test.log'
    logging.basicConfig(format = LOG_FORMAT,datefmt= DATE_FORMAT,filename=fileUrl,level = logging.DEBUG)  #指定要记录日志的级别，日志格式，日期格式，输出位置
    logging.debug(message)
    logging.shutdown()             #输出的信息 

if __name__=='__main__':
    pass
    app=pywin.Pywin()
    tl_dir = r'D:\QuiKLab3.0'
    tl_name = r'D:\QuiKLab3.0\MainApp.exe'   
    login(tl_dir,tl_name,'default','1')
# # #     time.sleep(5)
#     window_name =u'QuiKLab V3.0'
#     app.connect(window_name)
# #     time.sleep(5)
# #     creat_pro(window_name,'test_name120')
# #     unload_pro(window_name)
#     load_pro(window_name, 'test_name120')
# #     add_Bus(window_name)
# #     add_dev(window_name)
# #     add_tar(window_name)
# #     result=ckname.checkName('cl123')
# #     print result
# #     if result == 0:
# #         print "ProName had exist！！！"
# #         exit()
    readIniConfig('QuikLab3.0')
#     logWriter()
