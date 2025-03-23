from PyQt5 import QtCore, QtGui, QtWidgets
import string
import re
import sys, traceback
from DBConnection import DBConnection
import mysql.connector
class Ui_ViewNominee(object):
    def details(self):
        try:
          database = DBConnection.getConnection()
          cursor=database.cursor()
          cursor.execute("SELECT name,symbol FROM nominee")
          row = cursor.fetchall()
          self.tableWidget.setRowCount(0)
          for row_number, row_data in enumerate(row):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))


        except Exception as e:
               print("Error="+e.args[0])
               tb = sys.exc_info()[2]
               print(tb.tb_lineno)
