from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import sys
class Ui_Results(object):

    def viewres(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("SELECT NAME,symbol,vcnt FROM voting WHERE vcnt=(SELECT MAX(vcnt) FROM voting)")
            row = cursor.fetchall()
            for r in row:
                self.nm.setText(r[0])
                self.symbl.setText(r[1])
                self.vcnt.setText(str(r[2]))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
