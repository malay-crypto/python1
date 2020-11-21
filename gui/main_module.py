
import tkinter as tk
from functools import partial
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image
import time

from dao import dao
from emp import emp
from getConnection import getConnection

class main:
    def __init__(self):
        self.root=tk.Tk()
        self.root.minsize(300,300)
        self.l2=tk.Label(self.root,text="name")
        self.l2.place(x=10,y=40)
        self.t2=tk.Entry(self.root)
        self.t2.place(x=80,y=40)

        self.l3=tk.Label(self.root,text="dept")
        self.l3.place(x=10,y=80)
        self.t3=tk.Entry(self.root)
        self.t3.place(x=80,y=80)

        self.l4=tk.Label(self.root,text="salary")
        self.l4.place(x=10,y=120)
        self.t4=tk.Entry(self.root)
        self.t4.place(x=80,y=120)

        self.b1 = tk.Button(self.root,text="add",command=self.takeinput)
        self.b1.place(x=10,y=160)

        self.b1 = tk.Button(self.root,text="edit",command=self.edit)
        self.b1.place(x=50,y=160)

        self.b1 = tk.Button(self.root,text="delete",command=self.delete)
        self.b1.place(x=80,y=160)

        self.b1 = tk.Button(self.root,text="show all",command=self.show)
        self.b1.place(x=130,y=160)

        self.l5=tk.Label(self.root,text="")
        self.l5.place(x=10,y=200)

        self.root.mainloop()

    def takeinput(self):
        name=self.t2.get()
        dept=self.t3.get()
        salary=self.t4.get()
        d=dao()
        e=emp(name=name,dept=dept,salary=salary)
        d.insertemp(e)

        self.t2.delete(first=0,last=100)
        self.t3.delete(first=0,last=100)
        self.t4.delete(first=0,last=100)

        messagebox.showinfo("saved","Record saved successfully")              
    
    def show(self):
        d=dao()
        d.showemp()

    def edit(self):
        
        ans=messagebox.askokcancel("edit","are you sure want to edit ?")
        if ans:
            self.editpage()
        

    def editpage(self):
        w=window2()


    def delete(self):
        print("delete...")



class window2:

    def __init__(self):
        self.window=Tk()
        self.window.minsize(400,400)
        self.window.title("edit page")
        self.l1=tk.Label(self.window,text="select id to edit")
        self.l1.place(x=40,y=2)
        
        self.l2=tk.Label(self.window,text="name")
        self.l2.place(x=10,y=40)
        self.t2=tk.Entry(self.window)
        self.t2.place(x=80,y=40)

        self.l3=tk.Label(self.window,text="dept")
        self.l3.place(x=10,y=80)
        self.t3=tk.Entry(self.window)
        self.t3.place(x=80,y=80)

        self.l4=tk.Label(self.window,text="salary")
        self.l4.place(x=10,y=120)
        self.t4=tk.Entry(self.window)
        self.t4.place(x=80,y=120)


        self.b1=Button(self.window,text="Save",command=self.save)
        self.b1.place(x=80,y=150)

        con=getConnection()
        cur=con.cursor()
        sql="select * from emp"
        cur.execute(sql)

        v=[]
        for i in cur:
            v.append(i[0])

        self.cmb=ttk.Combobox(self.window,values=v)
        self.cmb.place(x=40,y=5)
        self.cmb.bind("<<ComboboxSelected>>",self.dispinwindow)

    def dispinwindow(self,event):
        
        self.t2.delete(first=0,last=100)
        self.t3.delete(first=0,last=100)
        self.t4.delete(first=0,last=100)
        id=self.cmb.get()
        
        con=getConnection()
        cur2=con.cursor()
        cur2.execute("SELECT * FROM emp WHERE id = %s", (id,))

        for i in  cur2:
            
            self.t2.insert(0,i[1])
            self.t3.insert(0,i[2])
            self.t4.insert(0,i[3])

        
    def save(self):
        id=self.cmb.get()
        name=self.t2.get()
        dept=self.t3.get()
        salary=self.t4.get()
        print("id in save =",id)

        e=emp(id,name,dept,salary)
        d=dao()
        d.editemp(e)

m=main()


