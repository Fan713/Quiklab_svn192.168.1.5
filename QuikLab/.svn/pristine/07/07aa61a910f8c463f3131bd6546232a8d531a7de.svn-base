#! /usr/bin/env python
#coding=GB18030
import pymysql
class check(object):
    def __init__(self,uName,proName):
        self.uName=uName
        self.proName=proName
        self.db = pymysql.connect(host = '192.168.1.226',port = 3306,user = 'root',passwd = 'root',db = 'mydb',charset = 'utf8')
    def ckUname(self):
        cur = self.db.cursor()
        cur.execute('SELECT Name FROM mydb.tbl_user;')
        data = cur.fetchall()
        for i in range(0,len(data)):
            if self.uName == data[i][0]:
                print "find user"
                cur.close()
                return(1)
        cur.close()
        return (0)        
    def ckProName(self):        
        cur = self.db.cursor()
        cur.execute('SELECT Name FROM mydb.tbl_project;')
        data = cur.fetchall()
        for i in range(0,len(data)):
            if self.proName == data[i][0]:
                print "find proName"
                cur.close()
                return(0)
        cur.close()
        return (1)
if __name__=='__main__':
    pass