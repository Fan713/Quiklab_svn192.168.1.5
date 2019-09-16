#! /usr/bin/env python
#coding=utf-8
import sys
import json
import re

import pymysql

reload(sys)
sys.setdefaultencoding('utf8')

def unicToList(Name,patt):
    i=json.dumps(Name,encoding='utf-8',ensure_ascii=False).strip('"').encode('utf8')  #unicode转为字符串
    Name=re.findall(patt,i)
    return(Name)
    
class check(object):
    def __init__(self):
        self.db = pymysql.connect(host = '192.168.1.226',port = 3306,user = 'root',passwd = 'root',db = 'mydb',charset = 'utf8')
    
    def search(self,cmmd):
        cur = self.db.cursor()
        cur.execute(cmmd)
        data = cur.fetchall()
        cur.close()
        return(data)
    
    #查询工程名且按照工程名称升序排序
    def getProName(self):
        cur = self.db.cursor()
        proSql = 'select Name from mydb.tbl_project order by Name;'
        cur.execute(proSql)
        proName = cur.fetchall()
        proName = list(proName)
        for i in range(len(proName)):
            proName[i] = proName[i][0]        
        proName = repr(proName).decode('unicode_escape')
        cur.close()
        patt=r"\'(.*?)\'"
        proName=unicToList(proName,patt)
        return(proName)
    
    '''
             查询工程下的用例分类名称
            条件：1、根据tbl_project中的工程ID
        2、tbl_resourcearchive表中‘测试用例集’的ID作为父ID
    '''
    def getTestCaseClassName(self,proName):
        cur = self.db.cursor()
        testCaseClassSql = '''select Name  FROM  mydb.tbl_resourcearchive 
                              where ProjectId = (select id from mydb.tbl_project where Name = "''' + proName + '''") 
                              and parentId = (select id FROM mydb.tbl_resourcearchive where ProjectId =(select id from mydb.tbl_project where Name = "''' + proName + '''") and Name = '测试用例集' order by id limit 1);'''
        cur.execute(testCaseClassSql)
        testCaseClass = cur.fetchall()
        testCaseClass = list(testCaseClass)
        for i in range(len(testCaseClass)):
            testCaseClass[i] = testCaseClass[i][0]
        testCaseClass = repr(testCaseClass).decode('unicode_escape')
        cur.close()

        patt=r"\'(.*?)\'"
        testCaseClass=unicToList(testCaseClass,patt)
        return(testCaseClass)
    '''
            查询工程用例分类下用例名称
           条件：1、tbl_project中工程ID
        2、tbl_resourcearchive父ID在工程下用例分类的ID中
        3、tbl_resourcearchive中父ID在测试用例分类名字的ID中
    '''
    def getTestCaseName(self,proName,testCaseClassName):
        cur = self.db.cursor()
        testCaseSql = '''SELECT Name FROM mydb.tbl_resourcearchive where parentId in (select id from mydb.tbl_resourcearchive where Name =  "'''+ testCaseClassName + '''") 
                        and ProjectId = (SELECT id FROM mydb.tbl_project where Name = "''' + proName + '''")
                        and parentId in (select id  FROM  mydb.tbl_resourcearchive where ProjectId = (select id from mydb.tbl_project where Name = "''' + proName + '''") and parentId = (select id FROM mydb.tbl_resourcearchive where ProjectId =(select id from mydb.tbl_project where Name = "''' + proName + '''") and Name = "测试用例集" order by id limit 1));'''
        cur.execute(testCaseSql)
        testCase = cur.fetchall()
        testCase = list(testCase)
        for i in range(len(testCase)):
            testCase[i] = testCase[i][0]
        testCase = repr(testCase).decode('unicode_escape')    
        cur.close()

        patt=r"\'(.*?)\'"
        testCase=unicToList(testCase,patt)
#         print testCase
        return(testCase)
    '''
            查询工程下任务分类名称
            条件：1、根据tbl_project中的工程ID
        2、tbl_resourcearchive表中‘测试任务集’的ID作为父ID
    '''
    def getTestTaskClassName(self,proName):
        cur = self.db.cursor()
        testTaskClassSql = '''select Name  FROM  mydb.tbl_resourcearchive 
                              where ProjectId = (select id from mydb.tbl_project where Name = "''' + proName + '''") 
                              and parentId = (select id FROM mydb.tbl_resourcearchive where ProjectId =(select id from mydb.tbl_project where Name = "''' + proName + '''") and Name = '测试任务集' order by id limit 1);'''
        cur.execute(testTaskClassSql)
        testTaskClass = cur.fetchall()
        testTaskClass = list(testTaskClass)
        for i in range(len(testTaskClass)):
            testTaskClass[i] = testTaskClass[i][0]
        testTaskClass = repr(testTaskClass).decode('unicode_escape')  
        cur.close()

        patt=r"\'(.*?)\'"
        testTaskClass=unicToList(testTaskClass,patt)

        return(testTaskClass)
    '''
            查询工程下任务分类下的任务名称
            条件：1、tbl_project中工程ID
        2、tbl_resourcearchive父ID在工程下任务分类的ID中
        3、tbl_resourcearchive中父ID在测试任务分类名字的ID中
    '''
    def getTestTaskName(self,proName,testTaskClassName):
        cur = self.db.cursor()
        testTaskSql = '''SELECT Name FROM mydb.tbl_resourcearchive where parentId in (select id from mydb.tbl_resourcearchive where Name =  "'''+ testTaskClassName + '''") 
                        and ProjectId = (SELECT id FROM mydb.tbl_project where Name = "''' + proName + '''")
                        and parentId in (select id  FROM  mydb.tbl_resourcearchive where ProjectId = (select id from mydb.tbl_project where Name = "''' + proName + '''") and parentId = (select id FROM mydb.tbl_resourcearchive where ProjectId =(select id from mydb.tbl_project where Name = "''' + proName + '''") and Name = "测试任务集" order by id limit 1));'''
        cur.execute(testTaskSql)
        testTask = cur.fetchall()
        testTask = list(testTask)
        for i in range(len(testTask)):
            testTask[i] = testTask[i][0]
        testTask = repr(testTask).decode('unicode_escape')   
        cur.close()

        patt=r"\'(.*?)\'"
        testTask = unicToList(testTask,patt)
        return(testTask)
    
    '''
            查询工程测试任务下的测试用例
            条件：1、tbl_project中工程ID
        2、tbl_resourcearchive父ID在工程下任务分类的ID中
        3、tbl_resourcearchive中父ID在测试任务分类名字的ID中
        4、tbl_archiveattributeindex中的archiveId与tbl_resourcearchive中的任务ID相等
        5、tbl_archiveattribute中的Id与tbl_archiveattributeindex中的AttributeId相等
    '''
    def getTestTaskTestCaseName(self,proName,testTaskClassName,testTaskName):
        cur = self.db.cursor()
        testTaskTestCaseSql =  '''select AttributeValue  from 
                         (SELECT id,Name FROM mydb.tbl_resourcearchive 
                          where parentId in (select id from mydb.tbl_resourcearchive where Name =  "''' + testTaskClassName + '''") 
                          and ProjectId = (SELECT id FROM mydb.tbl_project where Name = "''' + proName + '''")
                          and parentId in (select id  FROM  mydb.tbl_resourcearchive where ProjectId = (select id from mydb.tbl_project where Name = "''' + proName + '''") and parentId = (select id FROM mydb.tbl_resourcearchive where ProjectId =(select id from mydb.tbl_project where Name = "''' + proName + '''") and Name = "测试任务集" order by id limit 1))) a  
                          left join  mydb.tbl_archiveattributeindex b on a.id = b.archiveId 
                          left join mydb.tbl_archiveattribute c on b.AttributeId = c.Id 
                          where Name = "''' + testTaskName + '''" and AttributeValue like '%TestTask%';'''                       
#         print testTaskTestCaseSql
        cur.execute(testTaskTestCaseSql)
        testTaskTestCase = cur.fetchall()
        testTaskTestCase = list(testTaskTestCase)
        for i in range(len(testTaskTestCase)):
            testTaskTestCase[i] = testTaskTestCase[i][0]
        testTaskTestCase = repr(testTaskTestCase).decode('unicode_escape')   
        cur.close()

        patt=r'testCaseName\=\\"(.*?)\\'
        testTaskTestCase=unicToList(testTaskTestCase,patt)
        return(testTaskTestCase)
    
if __name__=='__main__':
    p=check()
# #     print p.search('SELECT Name FROM mydb.tbl_user;')
#     proNum='SELECT Name FROM mydb.tbl_resources where type=6;'
# #     print len(p.search(proNum))
#     _list=p.search(proNum)
#     _data=[]
#     print _list
#     print len(set(_list))
#     for i in range(len(_list)):
#         _data.append(str(json.dumps(_list[i][0],encoding='utf-8',ensure_ascii=False).strip('"').encode('GB18030'))) #工程数量
#     print repr(_data).encode('string_escape')
# #     for index,value in enumerate(p.search(proNum)):
# #         print(index,value)
    print p.getProName()
    print p.getTestCaseClassName('1111')    
    print p.getTestCaseName('1111', "用例分类")

    print p.getTestTaskClassName("1111")
    print p.getTestTaskName("1111", "测试任务集")
    print p.getTestTaskTestCaseName("1111","45","55")                         #工程列表添加索引