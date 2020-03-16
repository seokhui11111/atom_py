import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.user_id=None
        self.user_pw=None

    def setupUI(self):
        self.setGeometry(150,500,150,50)
        self.setWindowTitle("Sign In")
        self.setFixedSize(300,100)

        self.label1=QLabel("ID ")
        self.label2=QLabel("password ")

        self.lineEdit1=QLineEdit()
        self.lineEdit2=QLineEdit()
        self.lineEdit2.setEchoMode(QLineEdit().Password)

        self.pushButton=QPushButton("로그인")
        #로그인버튼 활성->이벤트 발생(시그널)
        self.pushButton.clicked.connect(self.submitLogin)

        layout=QGridLayout()
        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.pushButton,0,2)
        layout.addWidget(self.label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)

        self.setLayout(layout)

    #슬롯
    def submitLogin(self):
        self.user_id=self.lineEdit1.text()
        self.user_pw=self.lineEdit2.text()
        print(self.user_id,self.user_pw)

        if self.user_id is None or self.user_id=='' or not self.user_id:
            QMessageBox.about(self,"인증오류","id를 입력하세요")
            #커서이동
            self.lineEdit1.setFocus(True)
            return None

        if self.user_id is None or self.user_pw=='' or not self.user_pw:
            QMessageBox.about(self,"인증오류","pw를 입력하세요")
            self.lineEdit2.setFocus(True)
            return None
        self.close()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    loginDialog = AuthDialog()
    loginDialog.show()
    app.exec_()
