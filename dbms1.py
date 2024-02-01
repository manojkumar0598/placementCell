from tkinter import *
import sqlite3
import time
import tkinter.messagebox
import os
command="proj.py"
command2="dash.py"
from PIL import Image,ImageTk
conn=sqlite3.connect('placement1.db')
c=conn.cursor()


class Application:
	def __init__(self,master):
		self.master=master
		self.canvas=Canvas(master,width=800,height=800,bg='black')
		self.canvas.pack(side='left')
		#self.img=ImageTk.PhotoImage(Image.open("bg.gif"))
		#self.canvas.create_image(0,0,anchor=NW,image=self.img)
		#self.place=ImageTk.PhotoImage(Image.open("download.png"))
		#self.canvas.create_image(50,350,anchor=NW,image=self.place)
		#self.job=ImageTk.PhotoImage(Image.open('jobb.gif'))
		#self.canvas.create_image(385,550,anchor=NW,image=self.job)
		self.heading=Label(text='PLACEMENT CELL BMSIT',bg='black',fg='steelblue',font=('Times 40 bold'))
		self.heading.place(x=50,y=250)
		self.canvas.create_rectangle(20,250,790,790,outline='red')
		self.left=Label(text='New Admission? Create new account!',bg='black',fg='white',font=('arial 13 '))
		self.left.place(x=25,y=550)
		self.button=Button(text='CREATE',width=25,bg='black',fg='white',command=self.doit)
		self.button.place(x=26,y=600)

		self.canvas.create_line(375,260,375,780,fill='blue',dash=(5,5,5,5))
		self.right=Label(text='Registered User?',fg='white',bg='black',font=('Times 13 '))
		self.right.place(x=400,y=400)
		self.user=Label(text='USERNAME',fg='grey',bg='black',font=('arial 13 bold'))
		self.user.place(x=400,y=350)
		self.user_e=Entry(width=25)
		self.user_e.place(x=500,y=350)
		self.passw=Label(text='PASSWORD',fg='grey',bg='black',font=('arial 13 bold '))
		self.passw.place(x=400,y=400)
		self.passw_e=Entry(width=25,show='*')
		self.passw_e.place(x=501,y=400)
		self.login=Button(text='LOGIN',width=20,fg='white',bg='black',command=self.doit2)
		self.login.place(x=504,y=475)
	def doit(self):
		os.system(command)

	def doit2(self):
		self.var1=self.user_e.get()
		self.var2=self.passw_e.get()
		find_user=('SELECT * FROM users  WHERE username=? and password=?')
		c.execute(find_user,[(self.var2),(self.var2)])
		results=c.fetchall()
		if results:
			for i in results:
				os.system(command2)

		else:
			tkinter.messagebox.showinfo("Login Error, Try again")














root=Tk()
root.configure(background='black')
b=Application(root)

root.mainloop()
