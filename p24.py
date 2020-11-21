import tkinter as tk
from functools import partial
from tkinter import ttk




root=tk.Tk()
root['bg']='#345fab'
root.minsize(300,300)
logo = tk.PhotoImage(file="e:/38.png")
l1=tk.Label(root,text="enter no 1")
l1.place(x=10,y=10)
l2=tk.Label(root,text="enter no 2")
l2.place(x=10,y=40)
t1=tk.Entry(root)
t1.place(x=80,y=10)
t2=tk.Entry(root)
t2.place(x=80,y=40)
l3=tk.Label(root,text="----")
l3.place(x=10,y=80)

v=[]
for i in range(1,4):
    v.append(input("enter item"))

def sum():
    cmb['values']=v



cmb=ttk.Combobox(root,postcommand=sum)
cmb.place(x=10,y=200)


  


b1 = tk.Button(root,text="Exit",command=root.destroy)
b1.place(x=10,y=120)
b2 = tk.Button(root,text="add",command=partial(sum,t1,t2))
b2.place(x=10,y=160)
root.mainloop()
