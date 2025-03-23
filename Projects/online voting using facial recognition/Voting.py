from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from DBConnection import DBConnection

class Ui_Voting(object):
    def __init__(self,dialog,unm):
        self.dialog=dialog;
        self.unm = unm

    def nominelist(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("select name,symbol from nominee")
            records = cursor.fetchall()
            for row in records:
                self.comboBox.addItem(str(row[0]) + "  -->  " + str(row[1]))

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def votingnm(self):
        database = DBConnection.getConnection()
        cursor = database.cursor()
        nmlist = self.comboBox.currentText()
        nm = nmlist.split("  -->  ")
        nominee = nm[0]
        symbol = nm[1]
        sql = "select count(*) from voting where unm='" + self.unm + "'"
        cursor.execute(sql)
        res = cursor.fetchone()[0]
        if res > 0:
            self.showMessageBox("Information", "Already Voted..!")
        else:
            try:
                vcnt = 0;
                sql = "select count(*) from voting where name='" + nominee + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    sql = "select vcnt from voting where name='" + nominee + "'"
                    cursor.execute(sql)
                    vcnt = cursor.fetchone()[0]
                    vcnt = vcnt + 1
                    sqll = "update voting set vcnt=" + str(vcnt) + " where name='" + nominee + "'"
                    cursor.execute(sqll)
                    database.commit();
                    self.showMessageBox("Information", "Voted Successfully..!")
                    self.dialog.hide()
                else:
                    vcnt = 1;
                    sql = "insert into voting values(%s,%s,%s,%s)"
                    values = (nominee, symbol, int(vcnt), self.unm)
                    cursor.execute(sql, values)
                    database.commit()
                    self.showMessageBox("Information", "Voted Successfully..!")
                    self.dialog.hide()

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
