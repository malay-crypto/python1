class emp:
    def __init__(self,id=0,name="x",dept="acct",salary=0):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary

    def __str__(self):
        return self.name+"--"+self.dept+" --"+str(self.salary)


    