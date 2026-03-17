import mysql.connector
class MysqlClient:
    def __init__(self,host,port,user,password,database):
        self.connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
        self.cursor = self.connection.cursor()

    def fetch_all(self,qwery,params = None):
        self.cursor.execute(qwery,params)
        return self.cursor.fetchall()