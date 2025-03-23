from PyQt5 import QtCore, QtGui, QtWidgets
from AddNominee import Ui_AddNominee
from ViewNominee import Ui_ViewNominee
from Results import Ui_Results
class Ui_AdminHome(object):

    def __init__(self, Dialog):
        self.dialog = Dialog

    def addnomine(self):
        try:
            self.adnm = QtWidgets.QDialog()
            self.ui1 = Ui_AddNominee()
            self.ui1.setupUi(self.adnm)
            self.adnm.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewnomine(self):
        try:
            self.viewnm = QtWidgets.QDialog()
            self.ui1 = Ui_ViewNominee()
            self.ui1.setupUi(self.viewnm)
            self.ui1.details()
            self.viewnm.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def results(self):

        self.res = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.res)
        self.ui.viewres()
        self.res.show()
