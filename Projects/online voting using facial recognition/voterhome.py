from PyQt5 import QtCore, QtGui, QtWidgets
from Voting import Ui_Voting
from Results import Ui_Results
class Ui_VoterHome(object):

    def init(self,unm):
        self.unm=unm

    def voting(self):
        self.vote = QtWidgets.QDialog()
        self.ui = Ui_Voting(self.vote, self.unm)
        self.ui.setupUi(self.vote)
        self.ui.nominelist()
        self.vote.show()
    def results(self):

        self.res = QtWidgets.QDialog()
        self.ui = Ui_Results()
        self.ui.setupUi(self.res)
        self.ui.viewres()
        self.res.show()
