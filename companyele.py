from tkinter import *
import sqlite3
import time
from PIL import Image,ImageTk
conn=sqlite3.connect('placement.db')
c=conn.cursor()

class Application:
    def __init__(self,master):
        self.master=master
        self.left=Frame(master,width=1000,height=1000,bg='#DCDCDC')
        self.left.pack(side='left')
        self.scrollbar = Scrollbar(master)
        self.scrollbar.pack( side = RIGHT, fill = Y )

        self.heading=Label(self.left,text="      Placement Cell Management System     ",font=("Helvetica", 34, "bold italic"),fg='#FC4A1A',bg='#DCDCDC')
        self.heading.place(x=0,y=0)
        self.name=Label(self.left,text='STUDENT DETAILS',font=('arial 17 bold'),fg='#00303F',bg='#DCDCDC')
        self.name.place(x=0,y=70)
        self.name=Label(self.left,text='NAME',font=('arial 13'),fg='#00303F',bg='#DCDCDC')
        self.name.place(x=0,y=140)
        self.USN=Label(self.left,text='USN',font=('arial 13 '),fg='#00303F',bg='#DCDCDC')
        self.USN.place(x=0,y=180)
        self.branch=Label(self.left,text='BRANCH', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.branch.place(x=0,y=220)
        self.cgpa=Label(self.left,text='CGPA', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.cgpa.place(x=0,y=260)
        self.sgpa1=Label(self.left,text='12th Percentage', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.sgpa1.place(x=0,y=300)
        self.sgpa2=Label(self.left,text='10th Percentage', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.sgpa2.place(x=0,y=340)
        self.hob=Label(self.left,text='History of backs', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.hob.place(x=0,y=380)
        self.hob1=Label(self.left,text='Current backs', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.hob1.place(x=0,y=420)
        self.yop=Label(self.left,text='YEAR OF PASSING',font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.yop.place(x=0,y=460)

        self.name_e=Entry(self.left,width=30)
        self.name_e.place(x=240,y=140)
        self.USN_e=Entry(self.left,width=30)
        self.USN_e.place(x=240,y=180)
        self.branch_e=Entry(self.left,width=30)
        self.branch_e.place(x=240,y=220)
        self.cgpa_e=Entry(self.left,width=30)
        self.cgpa_e.place(x=240,y=260)
        self.sgpa1_e=Entry(self.left,width=30)
        self.sgpa1_e.place(x=240,y=300)
        self.sgpa2_e=Entry(self.left,width=30)
        self.sgpa2_e.place(x=240,y=340)
        self.hob_e=Entry(self.left,width=30)
        self.hob_e.place(x=240,y=380)
        self.hob1_e=Entry(self.left,width=30)
        self.hob1_e.place(x=240,y=420)
        self.yop_e=Entry(self.left,width=30)
        self.yop_e.place(x=240,y=460)


        self.c=Label(self.left,text='COMPANY REQUIREMENT',font=('arial 17 bold'),fg='#00303F',bg='#DCDCDC')
        self.c.place(x=500,y=70)
        self.cname=Label(self.left,text='COMPANY NAME',font=('arial 13'),fg='#00303F',bg='#DCDCDC')
        self.cname.place(x=500,y=140)
        self.HOB=Label(self.left,text='History of backs',font=('arial 13 '),fg='#00303F',bg='#DCDCDC')
        self.HOB.place(x=500,y=180)
        self.cb=Label(self.left,text='Current backs', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.cb.place(x=500,y=220)
        self.rcgpa=Label(self.left,text='CGPA', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.rcgpa.place(x=500,y=260)
        self.bond=Label(self.left,text='BOND', font=('ariel 13'),fg='#00303F',bg='#DCDCDC')
        self.bond.place(x=500,y=300)



        self.cname_e=Entry(self.left,width=30)
        self.cname_e.place(x=700,y=140)
        self.HOB_e=Entry(self.left,width=30)
        self.HOB_e.place(x=700,y=180)
        self.cb_e=Entry(self.left,width=30)
        self.cb_e.place(x=700,y=220)
        self.rcgpa_e=Entry(self.left,width=30)
        self.rcgpa_e.place(x=700,y=260)
        self.bond_e=Entry(self.left,width=30)
        self.bond_e.place(x=700,y=300)








root=Tk()
root.configure(background='black')
b=Application(root)
root.mainloop()
