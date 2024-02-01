from tkinter import *
import sqlite3
import time
from PIL import Image,ImageTk
import pymysql
connection=pymysql.connect(host='localhost',user='root',passwd='manoj',db='new_schema')
c=connection.cursor()

class Application:
    def __init__(self,master):
        self.master=master
        self.left=Frame(master,width=1000,height=1000,bg='black')
        self.left.pack(side='left')
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack( side = RIGHT, fill = Y )

        self.heading=Label(self.left,text="     PLACEMENT CELL MANAGEMENT SYSTEM     ",font=('Times 30 bold'),fg='lightgreen',bg='black')
        self.heading.place(x=0,y=0)
        self.name=Label(self.left,text='NAME',font=('arial 13'),fg='steelblue',bg='black')
        self.name.place(x=0,y=100)
        self.USN=Label(self.left,text='USN',font=('arial 13 '),fg='steelblue',bg='black')
        self.USN.place(x=0,y=140)
        self.branch=Label(self.left,text='BRANCH', font=('ariel 13'),fg='steelblue',bg='black')
        self.branch.place(x=0,y=180)
        self.cgpa=Label(self.left,text='CGPA', font=('ariel 13'),fg='steelblue',bg='black')
        self.cgpa.place(x=0,y=220)
        self.sgpa1=Label(self.left,text='SGPA SEM 1', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa1.place(x=0,y=260)
        self.sgpa2=Label(self.left,text='SGPA SEM 2', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa2.place(x=0,y=300)
        self.sgpa3=Label(self.left,text='SGPA SEM 3', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa3.place(x=0,y=340)
        self.sgpa4=Label(self.left,text='SGPA SEM 4', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa4.place(x=0,y=380)
        self.sgpa5=Label(self.left,text='SGPA SEM 5', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa5.place(x=0,y=420)
        self.sgpa6=Label(self.left,text='SGPA SEM 6', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa6.place(x=0,y=460)
        self.sgpa7=Label(self.left,text='SGPA SEM 7', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa7.place(x=0,y=500)
        self.sgpa8=Label(self.left,text='SGPA SEM 8', font=('ariel 13'),fg='steelblue',bg='black')
        self.sgpa8.place(x=0,y=540)
        self.hob=Label(self.left,text='Have you had backlogs?', font=('ariel 13'),fg='steelblue',bg='black')
        self.hob.place(x=0,y=580)
        self.hob1=Label(self.left,text='If yes, how many?', font=('ariel 13'),fg='steelblue',bg='black')
        self.hob1.place(x=0,y=620)
        self.yop=Label(self.left,text='YEAR OF PASSING',font=('ariel 13'),fg='steelblue',bg='black')
        self.yop.place(x=0,y=660)
        self.name_e=Entry(self.left,width=30)
        self.name_e.place(x=240,y=100)
        self.USN_e=Entry(self.left,width=30)
        self.USN_e.place(x=240,y=140)
        self.branch_e=Entry(self.left,width=30)
        self.branch_e.place(x=240,y=180)
        self.cgpa_e=Entry(self.left,width=30)
        self.cgpa_e.place(x=240,y=220)
        self.sgpa1_e=Entry(self.left,width=30)
        self.sgpa1_e.place(x=240,y=260)
        self.sgpa2_e=Entry(self.left,width=30)
        self.sgpa2_e.place(x=240,y=300)
        self.sgpa3_e=Entry(self.left,width=30)
        self.sgpa3_e.place(x=240,y=340)
        self.sgpa4_e=Entry(self.left,width=30)
        self.sgpa4_e.place(x=240,y=380)
        self.sgpa5_e=Entry(self.left,width=30)
        self.sgpa5_e.place(x=240,y=420)
        self.sgpa6_e=Entry(self.left,width=30)
        self.sgpa6_e.place(x=240,y=460)
        self.sgpa7_e=Entry(self.left,width=30)
        self.sgpa7_e.place(x=240,y=500)
        self.sgpa8_e=Entry(self.left,width=30)
        self.sgpa8_e.place(x=240,y=540)
        self.hob_e=Entry(self.left,width=30)
        self.hob_e.place(x=240,y=580)
        self.hob1_e=Entry(self.left,width=30)
        self.hob1_e.place(x=240,y=620)
        self.yop_e=Entry(self.left,width=30)
        self.yop_e.place(x=240,y=660)
        self.submit=Button(text='SUBMIT',width=20,height=10,fg='white',bg='black',command=self.doit)
        self.submit.place(x=240,y=700)

    def doit(self):
        self.var1=self.name_e.get()
        self.var2=self.USN_e.get()
        self.var3=self.branch_e.get()
        self.var4=self.cgpa_e.get()
        self.var5=self.sgpa1_e.get()
        self.var6=self.sgpa2_e.get()
        self.var7=self.sgpa3_e.get()
        self.var8=self.sgpa4_e.get()
        self.var9=self.sgpa5_e.get()
        self.var10=self.sgpa6_e.get()
        self.var11=self.sgpa7_e.get()
        self.var12=self.sgpa8_e.get()
        self.var13=self.hob_e.get()
        self.var14=self.hob1_e.get()
        self.var15=self.yop_e.get()
        sql="INSERT INTO student (NAME,USN,BRANCH,CGPA,SGPA1,SGPA2,SGPA3,SGPA4,SGPA5,SGPA6,SGPA7,SGPA8,HOB,HOB1,YOP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql,(self.var1,self.var2,self.var3,self.var4,self.var5,self.var6,self.var7,self.var8,self.var9,self.var10,self.var11,self.var12,self.var13,self.var14,self.var15))

        
        connection.commit() 









root=Tk()
root.configure(background='black')
b=Application(root)
root.mainloop()
