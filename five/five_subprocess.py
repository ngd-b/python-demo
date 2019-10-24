#!/usr/bin/python
# -*- coding:utf-8 -*-

# print("hello world")

'''
子进程 subprocess
'''
import subprocess

print('$ nslookup five_process.py')
r = subprocess.call(['nslookup','www.baidu.com'])
print("exit",r)

# 启动子进程时，传入参数
p = subprocess.Popen(["nslookup"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'')
print(output.decode('utf-8'))
print("Exit",p.returncode)
