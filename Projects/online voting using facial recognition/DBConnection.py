import mysql.connector
class DBConnection:
    @staticmethod
    def getConnection():
        database = mysql.connector.connect(host="localhost", user="root", passwd="root", db='voting')
        return database
if name=="main":
    print(DBConnection.getConnection())
