from PyQt5 import QtCore, QtGui, QtWidgets
from Register import Ui_Register
from DBConnection import DBConnection
import sys
from Verify import Ui_Verify
class Ui_User(object):

    def init(self, Dialog):
        self.dialog = Dialog

    def register(self,event):
        try:
            self.reg = QtWidgets.QDialog()
            self.ui = Ui_Register(self.reg)
            self.ui.setupUi(self.reg)
            self.reg.show()
            event.accept()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def login(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            unm = self.lineEdit.text()
            pwd = self.lineEdit_2.text()
            if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from register where unm='" + unm + "' and pwd='" + pwd + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.verfy = QtWidgets.QDialog()
                    self.ui = Ui_Verify(self.verfy,unm)
                    self.ui.setupUi(self.verfy)
                    self.verfy.show()
                    self.dialog.hide()
                else:
                    self.showMessageBox("Information", "Invalid Credentials..!")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
