#/usr/bin/python
# -*- conding:utf8 -*-

print("hello world")

# 邮件信息解析
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 邮件接收
import poplib

# 调试
import pdb
# 收件人邮箱信息用于登陆
addr= "**@qq.com"
# 授权码
password = "**"
# 邮箱服务地址 
pop_server = "pop.qq.com"

# 创建服务，登陆接收邮件
server = poplib.POP3(pop_server)
# 调试信息
server.set_debuglevel(1)
# 邮箱欢迎信息
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(addr)
server.pass_(password)
# stat() 获取邮件数量及占用空间
print("Email list: num %s , size %s " % server.stat())

# list() 获取列表信息(response,[mes_num octets ...],octets)
resp,nums,octets = server.list()
# 打印输出
# print(nums[1:10])

# retr() 按索引号获取每一份信息，设置可见标识；返回参数：(response,[line ...],octets)
index = len(nums)
resp,lines,octets = server.retr(index)

# lines 标识原始邮件信息的每一行
# 合并后解码
content = b'\r\b'.join(lines).decode('utf-8')

# 解析内容为 Message 对象
# pdb.set_trace()
msg = Parser().parsestr(content)
# print(msg.as_string())
# Message 对象可能对应的就是MIMEText 、 MIMEBase 、MIMEMultipart 多层嵌套
for item in msg.items():
    header,value = item
    print(header,value)

content = msg.get_payload()
print(content.decode("gb2312"))
# 1. 解析头部信息
# for header in ["From","To","Subject"]:
#     value = msg.get(header,'')
#     if value:
#         # 主题 Subject 信息解析和 From 、 To 不一样
#         if header == "Subject":
#             info,charset = decode_header(value)[0]
#             # 信息头设定了自己的编码，则解码
#             if charset:
#                 info.decode(charset)
#             print("主题："+info)
#         else:
#             # 收发人信息、称呼以及邮箱地址
#             ndr,addr = parseaddr(value)
#             info.charset = decode_header(ndr)[0]
#             if charset:
#                 info.decode(charset)
#             print("%s ：<%s>" % info % addr)

# # 2. 解析内容信息 ,内容信息可能会多层嵌套，需要递归处理
# def guess_charset(msg):
#     charset = msg.get_charset()
#     if charset is None:
#         content_type = msg.get('Content-Type', '').lower()
#         pos = content_type.find('charset=')
#         if pos >= 0:
#             charset = content_type[pos + 8:].strip()
#     return charset

# def parseBody(obj):
#     # 多对象
#     pdb.set_trace()
#     if (obj.is_multipart()):
#         # 递归处理
#         parts = obj.get_payload()
#         for n,part in enumerate(parts):
#             parseBody(part)
#     else:
#         content_type = obj.get_content_type()
#         # 处理内容格式
#         if content_type == "text/plain" or content_type == "text/html":
#             content = obj.get_payload(decode=True)
#             charset = guess_charset(obj)
#             if charset:
#                content = content.decode(charset)
#             print("info: %s " % content)
#         else:
#             print("附件：%s " % content_type)

# parseBody(msg)

# 结束
server.quit()