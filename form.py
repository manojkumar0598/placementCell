from tkinter import *
import sqlite3
import time
import sys
from PIL import Image,ImageTk
import pymysql
connection=pymysql.connect(host='localhost',user='root',passwd='manoj',db='new_schema')
c=connection.cursor()

class Application:
	def __init__(self,master):
		self.master=master
		self.left=Frame(master,width=500,height=500,bg='black')
		self.left.pack(side='left')

		self.heading=Label(self.left,text="     PLACEMENT CELL     ",font=('Times 30 bold'),fg='lightgreen',bg='black')
		self.heading.place(x=0,y=0)
		self.name=Label(self.left,text='NAME',font=('arial 13'),fg='steelblue',bg='black')
		self.name.place(x=0,y=100)
		self.Age=Label(self.left,text='AGE',font=('arial 13 '),fg='steelblue',bg='black')
		self.Age.place(x=0,y=140)
		self.USN=Label(self.left,text='USN',font=('arial 13 '),fg='steelblue',bg='black')
		self.USN.place(x=0,y=180)
		
		self.EMAIL=Label(self.left,text='EMAIL-ID',font=('arial 13 '),fg='steelblue',bg='black')
		self.EMAIL.place(x=0,y=220)
		self.username=Label(self.left,text='USERNAME',font=('arial 13 '),fg='steelblue',bg='black')
		self.username.place(x=0,y=260)
		self.password=Label(self.left,text='PASSWORD',font=('arial 13 '),fg='steelblue',bg='black')
		self.password.place(x=0,y=300)
		self.name_e=Entry(self.left,width=30)
		self.name_e.place(x=120,y=100)
		self.Age_e=Entry(self.left,width=30)
		self.Age_e.place(x=120,y=140)
		self.USN_e=Entry(self.left,width=30)
		self.USN_e.place(x=120,y=180)
		
		self.EMAIL_e=Entry(self.left,width=30)
		self.EMAIL_e.place(x=120,y=220)
		self.username_e=Entry(self.left,width=30)
		self.username_e.place(x=120,y=260)
		self.password_e=Entry(self.left,width=30,show='*')
		self.password_e.place(x=120,y=300)

		self.submit=Button(width=20,height=5, text='Submit',fg='white',bg='black',command=self.doit)
		self.submit.place(x=120,y=380)
		self.sub=Button()

		self.exit=Button(width=20,height=5,text='Exit',fg='white',bg='black',command=self.doit2)
		self.exit.place(x=280,y=380)
		
	def doit(self):
		self.var1 = self.name_e.get()
		self.var2 = self.Age_e.get()
		self.var3 = self.USN_e.get()
		
		self.var5 = self.EMAIL_e.get()
		self.var6 = self.username_e.get()
		self.var7 = self.password_e.get()

		
		sql="INSERT INTO users (Name,Age,Usn,emailid,Username,Password) VALUES(%s,%s,%s,%s,%s,%s)"
		c.execute(sql,(self.var1,self.var2,self.var3,self.var5,self.var6,self.var7))
		connection.commit()

	def doit2(self):
		sys.exit()

 

root=Tk()
root.configure(background='black')
b=Application(root)
root.mainloop()







       


