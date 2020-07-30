import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import calculator
# import operator

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import operator
# from calculator import Ui_MainWindow

READY = 0
INPUT = 1

class MainCode(QMainWindow, calculator.Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super(MainCode,self).__init__(*args,**kwargs)
        self.setupUi(self)
        #set up numbers.
        for n in range(0,10):
            getattr(self,'pushButton_n%s' %n).pressed.connect(lambda v=n:self.input_number(v))

def input_number(self,v):
    if self.state == READY:
        self.state = INPUT
        self.stack[-1] = v
    else:
        self.stack[-1] = self.stack[-1]*10+v
        self.display()
def display(self):
        self.lcdNumber.display(self.stack[-1])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())