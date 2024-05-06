import mysql.connector as sql

class DBConnection:

    @staticmethod
    def getConnection(self):
        try:
            conn = sql.connect(host='localhost', database = 'cms2', user = 'root', password = 'Priyanshu2003')

            if conn.is_connected():
                print("Database is connected:")
            else:
                print("Not connected with Database:")
        except Exception as e:
            print(str(e)+"---Database is not connected---")
        return conn

    def close(self):
        self.conn.close()













