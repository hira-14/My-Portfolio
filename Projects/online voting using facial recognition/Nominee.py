from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
class Ui_AddNominee(object):

    def addnomine(self):
        try:
            name = self.lineEdit.text()
            symbol = self.lineEdit_2.text()
            database = DBConnection.getConnection()
            cursor = database.cursor()
            if name == "" or name == "null" or symbol == "" or symbol == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from nominee where name='" + name + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.showMessageBox("Information", "Nominee name already exists..!")
                else:
                    query = "insert into nominee values(%s,%s)"
                    values = (name, symbol)
                    cursor.execute(query, values)
                    database.commit()

                    self.showMessageBox("Information", "Nominee Added Successfully..!")
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)
