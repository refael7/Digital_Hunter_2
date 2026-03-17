from app.config.conn_mysql import MysqlClient

host="localhost"
port=3306
user="root"
password="root"
database="digital_hunter"

client = MysqlClient(host,port,user,password,database)






