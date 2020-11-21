from emp import emp
from getConnection import getConnection
class dao:

    def __init__(self):
        self.con=getConnection()
        self.cur=self.con.cursor()

    def insertemp(self,e):
        sql="insert into emp(name,dept,salary) values('{0}','{1}',{2})".format(e.name,e.dept,e.salary)
        self.cur.execute(sql)
        self.con.commit()
        self.con.close()

    def editemp(self,e):
        print("id=",e.id)
        print("name=",e.name)
        
        cur2=self.con.cursor()
        cur2.execute("update emp set name=%s,dept=%s, salary=%s WHERE id = %s", (e.name,e.dept,e.salary,e.id))
        self.con.commit()
        self.con.close()
        print("record updated successfully")

    def delemp(self,e):
        pass

    def showemp(self):
        sql="select * from emp"
        self.cur.execute(sql)
        for i in self.cur:
            print(i)


