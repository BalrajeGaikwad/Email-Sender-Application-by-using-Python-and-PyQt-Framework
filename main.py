from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
from email_sender import send_email

class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("main.ui",self)

        self.pushButton.clicked.connect(self.send_email)

    def send_email(self):
        print("Email was Sent")
        if self.lineEdit.text():
            send_email(recepient=self.lineEdit.text(), email=self.textEdit.toPlainText())
        else:
            message=QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("Invalid Recipant")
            message.setWindowTitle("Error!")
            message.exec_()




if __name__=="__main__":
    app=QApplication(sys.argv)
    Windo=EmailSender()
    Windo.show()
    app.exec_()