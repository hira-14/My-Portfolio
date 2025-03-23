from PyQt5 import QtCore, QtGui, QtWidgets
from AdminHome import Ui_AdminHome
import sys
class Ui_Admin(object):
    def __init__(self, Dialog):
        self.dialog = Dialog

    def logincheck(self):
        try:
            unm = self.lineEdit.text()
            pwd = self.lineEdit_2.text()
            if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                if unm == "admin" and pwd == "admin":
                    self.home = QtWidgets.QDialog()
                    self.ui = Ui_AdminHome(self.home)
                    self.ui.setupUi(self.home)
                    self.home.show()
                    self.dialog.hide()

                else:
                    self.showMessageBox("Information", "Invalid Credentials..!")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
