import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TestForm(QMainWindow): #PyQt5.QtWidgets에서 상속됨
    #생성자
    def __init__(self):
        super().__init__() #부모의 생성자
        self.setupUI() #함수 선언
    def setupUI(self):
        self.setWindowTitle("PyQT test") #제목표시줄
        self.setGeometry(800,400,500,300) #윈도우에서 실행되는 위치,창크기

        btn_1=QPushButton("Click1",self)
        btn_2=QPushButton("Click2",self)
        btn_3=QPushButton("Click3",self)

        btn_1.move(20,30)
        btn_2.move(20,80)
        btn_3.move(20,130)

        btn_1.clicked.connect(self.btn_1_clicked) #시그널
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit)

    def btn_1_clicked(self):
        QMessageBox.about(self,"message","Clicked1") #슬롯

    def btn_2_clicked(self):
        print("Button Clicked")




if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
    print("After Loop")
