#/user/bin/python
# -*- coding:utf8 -*-

print("hello world")

# 发送一个纯文本邮件
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr

import smtplib

# 发送信息前发送人信息编辑
# addr= input("Email:")
addr= "**4@qq.com"
# password = input("Passworld:")
password = "***"
# 收件人地址
# to_addr = input("To:")
to_addr = "***@163.com"

# 邮箱服务地址 ； 我用的是163邮箱 ；
smtp_server = "smtp.qq.com"

# 格式化邮件主题信息
def formate_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,"utf-8").encode(),addr))

# 信息构造
msg = MIMEText('hello world , you are my shushine!','plain','utf-8')
msg["From"] = formate_addr('来自关注者 <%s>' % addr)
msg["To"] = formate_addr("Hello [%s]" % to_addr)
msg["Subject"] = Header('大哥，最近还好吗？',"utf-8").encode()
# 新建一个服务连接
server = smtplib.SMTP(smtp_server,25)
# 加密发送
server.starttls()

server.set_debuglevel(1)
# 登陆
server.login(addr,password)
# 信息发送给
server.sendmail(addr,[to_addr],msg.as_string())
server.quit()

