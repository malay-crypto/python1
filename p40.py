import mysql.connector as mc
import tkinter as tk
from functools import partial
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk,Image
import time




c=mc.connect(host="localhost",
  user="root",
  passwd="",
  database="mg1")

# c2=mc.connect(host="localhost",
#   user="root",
#   passwd="",
#   database="mg1")

cur=c.cursor()

def add():
    name=t2.get()
    dept=t3.get()
    salary=t4.get()
    sql="insert into emp(name,dept,salary) values('{0}','{1}',{2})".format(name,dept,salary)
    print(sql)
    cur.execute(sql)
    c.commit()



root=tk.Tk()
#root['bg']='#345fab'
root.minsize(300,300)


canvas = tk.Canvas(root, width=1300, height=1300)
img = ImageTk.PhotoImage(Image.open("e:/38.png"))
canvas.create_image(0,0, anchor=NW, image=img)

canvas.place(x=0,y=0)
#canvas.pack()

l2=tk.Label(root,text="name")
l2.place(x=10,y=40)
t2=tk.Entry(root)
t2.place(x=80,y=40)

l3=tk.Label(root,text="dept")
l3.place(x=10,y=80)
t3=tk.Entry(root)
t3.place(x=80,y=80)

l4=tk.Label(root,text="salary")
l4.place(x=10,y=120)
t4=tk.Entry(root)
t4.place(x=80,y=120)




b1 = tk.Button(root,text="add",command=add)
b1.place(x=10,y=160)


root.mainloop()
