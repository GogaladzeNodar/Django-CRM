import mysql.connector
import pymysql
# in case of mysql and not pymysql
#database = mysql.connector.connect()
dataBase = pymysql.connect(
    
    host = 'localhost',
    user = 'root',
    passwd = 'Nodari777$',
 )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mybase")

print("that's all!")