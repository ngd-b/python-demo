#/usr/bin/python
# -*- coding:utf-8 -*-

print("hellow world")

# GUI TKinter
from tkinter import *
# 消息盒子 弹窗信息
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # label 标签信息
        self.helloLabel = Label(self,text="hello world")
        self.helloLabel.pack()
        # input 信息输入
        self.getNameInput = Entry(self)
        self.getNameInput.pack()
        self.sureButton = Button(self,text="ok",command=self.welCome)
        self.sureButton.pack()
        self.quitButton = Button(self,text="Exit",command=self.quit)
        self.quitButton.pack()

    def welCome(self):
        name = self.getNameInput.get() or "world"
        messagebox.showinfo("Message","你好,%s" % name)
        
# 创建程序
app = Application()
# 程序标题title
app.master.title("hello world")
# print(app.master.size)
app.master.minsize(300,300)
app.mainloop()

'''
绘制图形、turtle库
'''
import turtle


# 中心点(0.00,0.00)为原点开始,指定点的位置
turtle.setpos(100,100)
turtle.goto(40,100)
# 回到原点
turtle.home()
turtle.color("red","green")
# 绘制一个正方形,不调用填充
num = 0
while True:
    turtle.forward(75)
    turtle.right(90)
    num+=1
    if num>3:
        break
# 绘制一个圆，调用填充、fill
turtle.begin_fill()
turtle.setpos(-150,0)
turtle.circle(90)
turtle.end_fill()

# 隐藏绘制图形中移动的光标
turtle.hideturtle()
# 绘制一个文本
turtle.color("#2312fa")
turtle.setpos(-100,200)
turtle.write("hello world!",False,align="left",font=("heiti",16,"bold"))
# turtle.write((0,0),True)

# 绑定一个事件
def handleEvent():
    turtle.forward(200)
    turtle.write("onclick",False)
turtle.onclick(handleEvent)
# turtle.onclick(None)

turtle.done()