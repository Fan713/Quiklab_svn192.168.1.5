#! /usr/bin/env python
#coding=GB18030
import re,time,os,sys
from pywinauto import application
app=application.Application(backend='uia')

#将application.py打印的控件属性导入./identify文件中
def setenv():
    for line in sys.path:
        t='site-packages$'
        if re.findall(t, line):
            old=line+'\\pywinauto\\application.py'
            new=line+'\\pywinauto\\application.bak'
    with open(old,'r') as f:
        patt='def\ print_control_identifiers'
        f2=open(new,'w')
        for line in f:
            if re.findall(patt, line):
                line=r"    def print_control_identifiers(self, depth=None, filename='./identif'):"
                f2.write(line)
                f2.write('\n')
            else:
                f2.write(line)
        f2.close()
    os.remove(old)
    os.rename(new, old)
class attr_Control(object):
    def __init__(self,con_Name):
        self.con_Name=con_Name      
        
#打印指定窗口下所有控件属性
    @staticmethod      
    def get_Allattr(window_name):
        time.sleep(1)
        app.connect(title = window_name)
        app[window_name].print_control_identifiers()

#根据正则表达式获得指定控件属性
    def get_attrName(self):
        path='./identif'
        _file=open(path)
        flag=0
        for line in _file:
#             t="'"+self.con_Name+"'"
            Name="\'%s\D?\d*\'"%self.con_Name
            if re.findall(Name, line):
                flag=1
#                 print line
                continue
            if flag == 1:
                break
        _file.close()
        if flag == 0:
            print('No this Element')
            return (0)
        else:
            attr_list=line.split(',')
            pattern=r'\'\w+\d+\''
            attrs=[]
            for i in attr_list:
                s=re.findall(pattern,i)
                if s:
                    attrs.append(s)
            if attrs:
                attr_Name=attrs[0][0].replace('\'','').strip(' ')
                return attr_Name
            else:
                print('No this Element')
                return (0)
if __name__=='__main__':
    setenv()
    con_Name=raw_input("Please input Search Name:")
    con_list=con_Name.split(',')
    for Name in con_list:
        window_name=r'QuiKLab V3.0'
        print "Seraching all attr..."
        attr_Control.get_Allattr(window_name)
        print Name
        attr=attr_Control(Name)
        print attr.get_attrName()
        try:
            app[window_name][u'需求管理'].wait('ready', 10, 2)
            print "1"
        except:
            print "2"
#         app[window_name][attr.get_attrName()].click_input()

    