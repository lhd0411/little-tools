# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
# Embedded file name: MultiWindow1.py
# Compiled at: 1995-09-28 00:18:56
# Size of source mod 2**32: 272 bytes
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import GetSpell, pyperclip

class MultiWindow(QWidget):

    def __init__(self):
        self.r = (123, 'xyz', 'zara', 'abc')
        self.put = '我'
        super().__init__()
        self.setWindowTitle('查注音')
        self.label = QLabel(self)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.textChanged.connect(self.text1)
        self.button1 = QPushButton('查询')
        self.button1.clicked.connect(self.onButton1Click)
        self.button2 = QPushButton('退出')
        self.button2.clicked.connect(self.onButton2Click)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.label)
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)
        self.label.setText('输入单个汉字查注音')

    def onButton1Click(self):
        global l
        global list1
        global s0
        global s1
        global s2
        global s3
        global s4
        global s5
        a = self.put
        self.r = GetSpell.get_message(a)
        result1 = self.r
        dict1 = result1[2]
        k = 6
        list1 = list(dict1.keys())
        l = len(dict1)
        if l == 1:
            s0 = str(dict1[list1[0]])
            s1 = '1'
            s2 = '1'
            s3 = '1'
            s4 = '1'
            s5 = '1'
        if l == 2:
            s0 = str(dict1[list1[0]])
            s1 = str(dict1[list1[1]])
            s2 = '1'
            s3 = '1'
            s4 = '1'
            s5 = '1'
        if l == 3:
            s0 = str(dict1[list1[0]])
            s1 = str(dict1[list1[1]])
            s2 = str(dict1[list1[2]])
            s3 = '1'
            s4 = '1'
            s5 = '1'
        if l == 4:
            s0 = str(dict1[list1[0]])
            s1 = str(dict1[list1[1]])
            s2 = str(dict1[list1[2]])
            s3 = str(dict1[list1[3]])
            s4 = '1'
            s5 = '1'
        if l == 5:
            s0 = str(dict1[list1[0]])
            s1 = str(dict1[list1[1]])
            s2 = str(dict1[list1[2]])
            s3 = str(dict1[list1[3]])
            s4 = str(dict1[list1[4]])
            s5 = '1'
        if l == 6:
            s0 = str(dict1[list1[0]])
            s1 = str(dict1[list1[1]])
            s2 = str(dict1[list1[2]])
            s3 = str(dict1[list1[3]])
            s4 = str(dict1[list1[4]])
            s5 = str(dict1[list1[5]])
        d = textdialog(self.r)
        result = d.exec()
        self.lineEdit.setText('')
        d.destroy()

    def onButton2Click(self):
        self.close()

    def text1(self, text):
        self.put = text
        print(text)


class textdialog(QDialog):

    def __init__(self, myResult, parent=None):
        super(textdialog, self).__init__(parent)
        self.setWindowTitle('textdialog')
        layout = QVBoxLayout()
        self.setLayout(layout)
        if l == 1:
            self.btn1 = QPushButton(s0)
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(lambda : self.whichbtn0(self.btn1))
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
        if l == 2:
            self.btn1 = QPushButton(s0)
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(lambda : self.whichbtn0(self.btn1))
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
            self.btn2 = QPushButton(s1)
            self.btn2.setCheckable(True)
            self.btn2.toggle()
            self.btn2.clicked.connect(lambda : self.whichbtn1(self.btn2))
            self.btn2.clicked.connect(self.btnstate)
            layout.addWidget(self.btn2)
        if l == 3:
            self.btn1 = QPushButton(s0)
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(lambda : self.whichbtn0(self.btn1))
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
            self.btn2 = QPushButton(s1)
            self.btn2.setCheckable(True)
            self.btn2.toggle()
            self.btn2.clicked.connect(lambda : self.whichbtn1(self.btn2))
            self.btn2.clicked.connect(self.btnstate)
            layout.addWidget(self.btn2)
            self.btn3 = QPushButton(s2)
            self.btn3.setCheckable(True)
            self.btn3.toggle()
            self.btn3.clicked.connect(lambda : self.whichbtn2(self.btn3))
            self.btn3.clicked.connect(self.btnstate)
            layout.addWidget(self.btn3)
        if l == 4:
            self.btn1 = QPushButton(s0)
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(lambda : self.whichbtn0(self.btn1))
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
            self.btn2 = QPushButton(s1)
            self.btn2.setCheckable(True)
            self.btn2.toggle()
            self.btn2.clicked.connect(lambda : self.whichbtn1(self.btn2))
            self.btn2.clicked.connect(self.btnstate)
            layout.addWidget(self.btn2)
            self.btn3 = QPushButton(s2)
            self.btn3.setCheckable(True)
            self.btn3.toggle()
            self.btn3.clicked.connect(lambda : self.whichbtn2(self.btn3))
            self.btn3.clicked.connect(self.btnstate)
            layout.addWidget(self.btn3)
            self.btn4 = QPushButton(s3)
            self.btn4.setCheckable(True)
            self.btn4.toggle()
            self.btn4.clicked.connect(lambda : self.whichbtn3(self.btn4))
            self.btn4.clicked.connect(self.btnstate)
            layout.addWidget(self.btn4)
        if l == 5:
            self.btn1 = QPushButton(s0)
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(lambda : self.whichbtn0(self.btn1))
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
            self.btn2 = QPushButton(s1)
            self.btn2.setCheckable(True)
            self.btn2.toggle()
            self.btn2.clicked.connect(lambda : self.whichbtn1(self.btn2))
            self.btn2.clicked.connect(self.btnstate)
            layout.addWidget(self.btn2)
            self.btn3 = QPushButton(s2)
            self.btn3.setCheckable(True)
            self.btn3.toggle()
            self.btn3.clicked.connect(lambda : self.whichbtn2(self.btn3))
            self.btn3.clicked.connect(self.btnstate)
            layout.addWidget(self.btn3)
            self.btn4 = QPushButton(s3)
            self.btn4.setCheckable(True)
            self.btn4.toggle()
            self.btn4.clicked.connect(lambda : self.whichbtn3(self.btn4))
            self.btn4.clicked.connect(self.btnstate)
            layout.addWidget(self.btn4)
            self.btn5 = QPushButton(s4)
            self.btn5.setCheckable(True)
            self.btn5.toggle()
            self.btn5.clicked.connect(lambda : self.whichbtn4(self.btn5))
            self.btn5.clicked.connect(self.btnstate)
            layout.addWidget(self.btn5)
        if l == 6:
            self.btn1 = QPushButton(s0)
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(lambda : self.whichbtn0(self.btn1))
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
            self.btn2 = QPushButton(s1)
            self.btn2.setCheckable(True)
            self.btn2.toggle()
            self.btn2.clicked.connect(lambda : self.whichbtn1(self.btn2))
            self.btn2.clicked.connect(self.btnstate)
            layout.addWidget(self.btn2)
            self.btn3 = QPushButton(s2)
            self.btn3.setCheckable(True)
            self.btn3.toggle()
            self.btn3.clicked.connect(lambda : self.whichbtn2(self.btn3))
            self.btn3.clicked.connect(self.btnstate)
            layout.addWidget(self.btn3)
            self.btn4 = QPushButton(s3)
            self.btn4.setCheckable(True)
            self.btn4.toggle()
            self.btn4.clicked.connect(lambda : self.whichbtn3(self.btn4))
            self.btn4.clicked.connect(self.btnstate)
            layout.addWidget(self.btn4)
            self.btn5 = QPushButton(s4)
            self.btn5.setCheckable(True)
            self.btn5.toggle()
            self.btn5.clicked.connect(lambda : self.whichbtn4(self.btn5))
            self.btn5.clicked.connect(self.btnstate)
            layout.addWidget(self.btn5)
            self.btn6 = QPushButton(s5)
            self.btn6.setCheckable(True)
            self.btn6.toggle()
            self.btn6.clicked.connect(lambda : self.whichbtn5(self.btn6))
            self.btn6.clicked.connect(self.btnstate)
            layout.addWidget(self.btn6)
        if l > 6:
            self.btn1 = QPushButton('注音太多')
            self.btn1.setCheckable(True)
            self.btn1.toggle()
            self.btn1.clicked.connect(self.btnstate)
            layout.addWidget(self.btn1)
        self.btn7 = QPushButton('在查一个')
        self.btn7.setCheckable(True)
        self.btn7.toggle()
        self.btn7.clicked.connect(self.goout)
        self.btn7.clicked.connect(self.btnstate)
        layout.addWidget(self.btn7)

    def btnstate(self):
        if self.btn1.isChecked():
            print('button pressed')
        else:
            print('button released')

    def whichbtn0(self, btn):
        print('clicked button is ' + btn.text())
        pyperclip.copy(list1[0])

    def whichbtn1(self, btn):
        print('clicked button is ' + btn.text())
        pyperclip.copy(list1[1])

    def whichbtn2(self, btn):
        print('clicked button is ' + btn.text())
        pyperclip.copy(list1[2])

    def whichbtn3(self, btn):
        print('clicked button is ' + btn.text())
        pyperclip.copy(list1[3])

    def whichbtn4(self, btn):
        print('clicked button is ' + btn.text())
        pyperclip.copy(list1[4])

    def whichbtn5(self, btn):
        print('clicked button is ' + btn.text())
        pyperclip.copy(list1[5])

    def goout(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MultiWindow()
    form.show()
    sys.exit(app.exec_())
# okay decompiling MultiWindow1.pyc
