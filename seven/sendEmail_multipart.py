#/user/bin/python
# -*- coding:utf8 -*-

print("hello world")

# 发送一个纯文本邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr

import smtplib

import base64

# 发送信息前发送人信息编辑
# addr= input("Email:")
addr= "**@qq.com"
# password = input("Passworld:")
password = "**"
# 收件人地址
# to_addr = input("To:")
to_addr = "**@163.com"

# 邮箱服务地址 
smtp_server = "smtp.qq.com"

# 格式化邮件主题信息
def formate_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,"utf-8").encode(),addr))

# 信息构造 , 消息主题类型为多形式格式
msg = MIMEMultipart()
# msg = MIMEText('hello world , you are my shushine!','plain','utf-8')
msg["From"] = formate_addr('来自关注者 <%s>' % addr)
msg["To"] = formate_addr("Hello [%s]" % to_addr)
msg["Subject"] = Header('大哥，最近还好吗？',"utf-8").encode()
# 可以加入文本信息
# msg.attach(MIMEText('hello world , you are my shushine!','plain','utf-8'))
# with open("./test.html","r",encoding="utf-8") as f:
#     msg.attach(MIMEText(f.read(),'html','utf-8'))
with open("./test.png","rb") as f:
    affix = "data:image/png;base64,"
    stream = base64.b64encode(f.read())
    msg.attach(MIMEText('''<html>
        <head></head><body>
            <h1>hello world</h1>
            <img src="'+affix+stream.decode()+'">
        </body></html>''','html','utf-8'))
# 加入附件文件信息
# 读取当前目录下的一张图片 ， 以字节码读取，网络传输
with open("./test.png","rb") as f:
    # 设置文件基本信息
    mime = MIMEBase("image",'png',filename="test.png")
    # 加入文件头信息
    # mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    # mime.add_header('Content-ID', '<0>')
    # mime.add_header('X-Attachment-Id', '0')
    # 读取文件
    mime.set_payload(f.read())
    # 文件编码 base 64
    encoders.encode_base64(mime)
    msg.attach(mime)
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

