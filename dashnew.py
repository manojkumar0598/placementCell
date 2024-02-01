from tkinter import *
import os
import sys
command3="qwe.py"
command4="test.py"
command5="prev.py"
#command6="filename"

class Application:
    def __init__(self,master):
        self.master=master
        self.left=Frame(master,width=400,height=400,bg='black')
        self.left.pack(side='left')

        self.submit=Button(width=20,height=10, text='Student Details Registration',fg='black',bg='beige', command=self.doit3)
        self.submit.place(x=12,y=10)
        self.sub=Button()
        self.submit=Button(width=20,height=10, text='Company Registration',fg='black',bg='beige', command=self.doit4)
        self.submit.place(x=250,y=10)
        self.sub=Button()
        
        self.sub=Button()
        self.submit=Button(width=20,height=10, text='Previous year Statistics',fg='black',bg='beige',command=self.doit6)
        self.submit.place(x=135,y=200)
        self.sub=Button()
        self.exit=Button(width=20,text='EXIT',bg='black',fg='white',command=self.doit5)
        self.exit.place(x=125,y=375)

    def doit3(self):
        os.system(command3)

    def doit4(self):
        os.system(command4)
    def doit5(self):
        sys.exit()

    def doit6(self):
        os.system(command5)

    #same way other commands can be added after company Details and previous stat files are created




root=Tk()
root.configure(background='black')
b=Application(root)
root.mainloop()
