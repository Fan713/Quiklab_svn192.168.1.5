#! /usr/bin/env python
#coding=GB18030
import paramiko
import uuid

class SSHConnection(object):
    def __init__(self, host, port, username, pwd):
        
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self._k = None
        
    def connect(self):
        transport = paramiko.Transport(self.host,self.port)
        transport.connect(username = self.username, password = self.pwd)
        self._transport = transport
        
    def close(self):
        self._transport.close()
    
    #上传    
    def upload(self,local_path,target_path):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.put(local_path,target_path)
    
    #下载   
    def download(self,remote_path,local_path):
        sftp = paramiko.SFTPClient.from_transport(self._transport)
        sftp.get(remote_path,local_path)
        
    #执行命令并将结果打印
    def cmd(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self._transport
        #执行命令
        stdin,stdout,stderr = ssh.exec_command(command)
        #获取命令结果集
        result = stdout.read()
        print (str(result))
        return result

   
ssh = SSHConnection(host = '192.168.1.211', port = 22, username = 'root', pwd = 'redhat')
ssh.connect()
ssh.cmd("ls")
# ssh.upload('sl.py', '/tmp/ks77.py')
# ssh.download('/tmp/ks77.py', 'sl.py')
ssh.close()
        
    
        
