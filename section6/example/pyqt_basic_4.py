import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyqt_basic_ui import Ui_MainWindow


# form_class=uic.loadUiType('D:/atom_py/section6/example/basic_test_01.ui')[0]


class TestForm(QMainWindow, Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__() #부모의 생성자
        self.setupUi(self) #함수 선언





if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=TestForm()
    window.show()
    app.exec_()
    print("After Loop")
