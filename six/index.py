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