import mysql.connector as mc
import datetime as dt
print(dt.datetime.now())


con=mc.connect(host="localhost",user="root",passwd="",database="mg1")


cur=con.cursor()
c=cur.execute("select * from order_master")
print(cur)
for i in cur:
    print(i)


