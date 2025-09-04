import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@369'

)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done !")
