import tkinter as tk
from tkinter import ttk as ttk
import tkinter.font as font
import os
import tkinter.messagebox as tkMessageBox
import getface as gf
import train as t
import recognize as r
import sqlite3
import threading

def run():
    r.recognizePerson()

def startIds():
    try:
        global th
        th = threading.Thread(target = run)
        th.setDaemon(True)
        th.start()
    except:
        tkMessageBox.showerror('Message', 'Problem while starting IDS!!!')

def printAllRecord():
    try:
        conn = sqlite3.connect("recface.db")
        cursor = conn.execute("SELECT * from people order by ID")
        data = cursor
        for index, dat in enumerate(data):
            tk.Label(master, text=dat[0],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=0)
            tk.Label(master, text=dat[1],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=1)
            tk.Label(master, text=dat[2],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=2)
            tk.Label(master, text=dat[3],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=3)
    except:
        tkMessageBox.showinfo('Message', 'Cannot connect to database!!!')


def printRecord():
    try:
        name ="\""+(txt112.get())+"\""
        conn = sqlite3.connect("recface.db")
        cursor = conn.execute("SELECT * from people Where Name = "+str(name)+" order by ID")
        data = cursor
        for index, dat in enumerate(data):
            tk.Label(master, text=dat[0],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=0)
            tk.Label(master, text=dat[1],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=1)
            tk.Label(master, text=dat[2],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=2)
            tk.Label(master, text=dat[3],fg="black"  ,bg="white" ,font=('times', 15, ' bold ')).grid(row=index+1, column=3)
    except:
        tkMessageBox.showinfo('Message', 'Cannot connect to database!!!')

def getRecord():
    global master
    master = tk.Toplevel()
    master.state('zoomed')
    master.geometry('500x500')
    master.configure(background='white')
    master.title("Employee's Record")
    Label1 = tk.Label(master, text="Employee Id", width=15,fg="black"  ,bg="white" ,font=('times', 15, ' bold '))
    Label1.grid(row=0, column=0)
    Label2 = tk.Label(master, text="Employee Name", width=15,fg="black"  ,bg="white" ,font=('times', 15, ' bold '))
    Label2.grid(row=0, column=1)
    Label3 = tk.Label(master, text="Employee Age", width=15,fg="black"  ,bg="white" ,font=('times', 15, ' bold '))
    Label3.grid(row=0, column=2)
    Label1 = tk.Label(master, text="Employee Phone No", width=15,fg="black"  ,bg="white" ,font=('times', 15, ' bold '))
    Label1.grid(row=0, column=3)
    global txt112
    lbl = tk.Label(master, text="Enter Employee Name:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') )
    lbl.place(x=870, y=60)
    txt112 = tk.Entry(master,width=20, bg="white" ,fg="black",font=('times', 15, ' bold '))
    txt112.place(x=1200, y=70)
    Data = tk.Button(master, text="Get Record by Name",command = printRecord ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
    Data.place(x=850, y=150)
    Data1 = tk.Button(master, text="Get all Record ",command = printAllRecord ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
    Data1.place(x=1200, y=150)

def delete():
    try:
        Id =(int)(txt11.get())
        conn = sqlite3.connect("recface.db")
        cmd = "Delete from people WHERE ID = "+str(Id)
        conn.execute(cmd)
        conn.commit()
        tkMessageBox.showinfo('Message', 'Record deleted sucessfully!!!')
        conn.close()
        back()
    except:
        tkMessageBox.showinfo('Message', 'Cannot connect to databases!!!')

def update():
    try:
        Id =(int)(txt11.get())
        Name ="\""+(txt22.get())+"\""
        Age =(int)(txt44.get())
        Phone =(int)(txt33.get())
        if len(str(Phone)) == 10:
            gf.insertorUpdate(Id, Name, Age, Phone)
            back()
        else:
            tkMessageBox.showinfo('Message', 'Phone number must be 10 digits!!!')
    except:
        tkMessageBox.showinfo('Message', 'Please fill above fields!!!')

def getimg():
    try:
        Id =(int)(txt11.get())
        Name ="\""+(txt22.get())+"\""
        Age =(int)(txt44.get())
        Phone =(int)(txt33.get())
        if len(str(Phone)) == 10:
            gf.get(Id, Name, Age, Phone)
            tkMessageBox.showinfo('Message', 'Record has been saved please wait until data to be trained!!!')
            t.trainImage()
            tkMessageBox.showinfo('Message', 'Data has been trained sucessfully!!!')
            back()
        else:
            tkMessageBox.showinfo('Message', 'Phone number must be 10 digits!!!')
    except:
        tkMessageBox.showinfo('Message', 'Please fill above fields!!!')

def logout():
    top.withdraw()
    window.deiconify()
    window.state('zoomed')

def back():
    top1.withdraw()
    top.deiconify()

def register():
    top.withdraw()
    global top1
    top1 = tk.Toplevel()
    top1.title("Admin Login")
    top1.geometry('1920x1080')
    top1.overrideredirect(2)
    top1.configure(background='white')
    top1.grid_rowconfigure(0, weight=1)
    top1.grid_columnconfigure(0, weight=1)
    global txt11, txt22, txt33, txt44
    message = tk.Label(top1, text="Employee Registration" ,bg="white"  ,fg="black"  ,width=30  ,height=3,font=('times', 30, 'italic bold underline'))
    message.place(x=450, y=20)

    lbl = tk.Label(top1, text="Enter Employee Id:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') )
    lbl.place(x=550, y=200)

    txt11 = tk.Entry(top1,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
    txt11.place(x=800, y=215)

    lbl2 = tk.Label(top1, text="Enter Employee Name:",width=20  ,fg="black"  ,bg="white"    ,height=2 ,font=('times', 15, ' bold '))
    lbl2.place(x=530, y=300)

    txt22 = tk.Entry(top1,width=20,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
    txt22.place(x=800, y=315)

    lb3 = tk.Label(top1, text="Enter Employee Phone No:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') )
    lb3.place(x=510, y=400)

    txt33 = tk.Entry(top1,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
    txt33.place(x=800, y=415)

    lbl4 = tk.Label(top1, text="Enter Employee Age:",width=20  ,fg="black"  ,bg="white"    ,height=2 ,font=('times', 15, ' bold '))
    lbl4.place(x=540, y=500)

    txt44 = tk.Entry(top1,width=20,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
    txt44.place(x=800, y=515)

    getFace = tk.Button(top1, text="Get Face",command = getimg ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
    getFace.place(x=500, y=650)

    Update = tk.Button(top1, text="Update",command = update ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
    Update.place(x=800, y=650)

    Delete = tk.Button(top1, text="Delete",command = delete ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
    Delete.place(x=500, y=750)

    Done = tk.Button(top1, text="Done",command = back ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
    Done.place(x=800, y=750)

def auto():
    Id = (txt.get())
    password = (txt2.get())
    txt.delete('0', tk.END)
    txt2.delete('0', tk.END)
    if(Id == "q") and (password == "q"):
        tkMessageBox.showinfo('Message', 'Welcome Admin')
        window.withdraw()
        global top
        top = tk.Toplevel()
        top.title("Admin Login")
        top.geometry('1920x1080')
        top.overrideredirect(2)
        top.configure(background='white')
        top.grid_rowconfigure(0, weight=1)
        top.grid_columnconfigure(0, weight=1)

        lb1 = tk.Label(top, text="Register/Update/Delete Employee:" ,bg="white"  ,fg="black"  ,width=25  ,height=3,font=('times', 25, 'italic bold underline'))
        lb1.place(x=300, y=150)

        register1 = tk.Button(top, text="Register/Update/Delete",command = register ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
        register1.place(x=840, y=180)

        lb2 = tk.Label(top, text="Get Employee Detail:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 25, ' italic bold underline ') )
        lb2.place(x=300, y=350)

        detail = tk.Button(top, text="Get Details",command = getRecord ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
        detail.place(x=840, y=380)

        lb3 = tk.Label(top, text="Start IDS:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 25, ' italic bold underline ') )
        lb3.place(x=300, y=550)

        start = tk.Button(top, text="Start",command = startIds ,fg="black"  ,bg="white"  ,width=20  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
        start.place(x=840, y=580)

        logout1 = tk.Button(top, text="Logout" ,command = logout, fg="black"  ,bg="white"  ,width=20  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
        logout1.place(x=1280, y=10)
    else:
        tkMessageBox.showinfo('Message', 'Wrong Username or Password try again!!!')

window = tk.Tk()
window.title("Admin Login")
window.state('zoomed')
window.geometry("1920x1080")
#window.overrideredirect(2)
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message1 = tk.Label(window, text="**Intrusion Detection System**" ,bg="white"  ,fg="black"  ,width=60  ,height=3,font=('times', 30, 'italic bold underline'))
message1.place(x=120, y=5)

message = tk.Label(window, text="Admin Login!!!" ,bg="white"  ,fg="black"  ,width=30  ,height=2,font=('times', 30, 'italic bold underline'))
message.place(x=450, y=120)

lbl = tk.Label(window, text="Enter Username:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') )
lbl.place(x=550, y=280)

txt = tk.Entry(window,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
txt.place(x=800, y=295)

lbl2 = tk.Label(window, text="Enter Password:",width=20  ,fg="black"  ,bg="white"    ,height=2 ,font=('times', 15, ' bold '))
lbl2.place(x=550, y=380)

txt2 = tk.Entry(window,width=20,show = '*'  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
txt2.place(x=800, y=385)

Login = tk.Button(window, text="Authenticate", command=auto ,fg="black"  ,bg="white"  ,width=20  ,height=3, activebackground = "white" ,font=('times', 15, ' bold '))
Login.place(x=680, y=530)

if __name__ == "__main__":
    window.mainloop()
