import mysql.connector as mc

c=mc.connect(host="localhost",  user="root",  password="",  database="mg1")

def getConnection():
    return c

