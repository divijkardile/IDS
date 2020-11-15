import tkinter as tk
from tkinter import ttk as ttk
import tkinter.font as font
import os
from firebase import firebase
import tkinter.messagebox as tkMessageBox
#from usb import *
from lockWindows import *
import sendvalidation as s

_firebase = None
try:
    _firebase = firebase.FirebaseApplication("https://fir-con-5932e.firebaseio.com/", None)
except:
    tkMessageBox.showinfo('Message', 'Cannot connect to internet please check your Internet Connection!!!')

def auto():
    Id = (txt.get())
    password = (txt2.get())
    
    if(Id == _username) and (password == _password1):
        try:
            tkMessageBox.showinfo('Message', 'Welcome Admin')
            _firebase.put("/fir-con-5932e/Login/-M49ieZenKigrVjHsT0W", "InOut", "True")
            #enableUSBPort()
            window.destroy()
        except:
            tkMessageBox.showinfo('Message', 'No Internet Connection!!!')
            lock()
    else:
        tkMessageBox.showinfo('Message', 'Wrong Username or Password try again!!!')
        lock()
            
def login1():
    global window, _username, _password1
    window = tk.Tk()
    lock()
    #os.system("python processDisable.py")
    try:
        _username, _password1 = s.sendValidation("kardiledivij@gmail.com")
    except:
        tkMessageBox.showinfo('Message', 'Cannot send Username and Password please check Internet Connection!!!')
    window.title("Security Login")
    window.geometry('1920x1080')
    #window.overrideredirect(2)
    window.configure(background='white')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    message = tk.Label(window, text="Security Login!!!" ,bg="white"  ,fg="black"  ,width=30  ,height=3,font=('times', 30, 'italic bold underline')) 
    message.place(x=450, y=20)

    lbl = tk.Label(window, text="Enter Username:",width=20  ,height=2  ,fg="black"  ,bg="white" ,font=('times', 15, ' bold ') ) 
    lbl.place(x=550, y=200)
    global txt, txt2
    txt = tk.Entry(window,width=20  ,bg="white" ,fg="black",font=('times', 15, ' bold '))
    txt.place(x=800, y=215)

    lbl2 = tk.Label(window, text="Enter Password:",width=20  ,fg="black"  ,bg="white"    ,height=2 ,font=('times', 15, ' bold ')) 
    lbl2.place(x=550, y=300)

    txt2 = tk.Entry(window,width=20,show = '*'  ,bg="white"  ,fg="black",font=('times', 15, ' bold ')  )
    txt2.place(x=800, y=315)

    Login = tk.Button(window, text="Authenticate", command=auto ,fg="black"  ,bg="white"  ,width=20  ,height=3, activebackground = "white" ,font=('times', 15, ' bold '))
    Login.place(x=680, y=450)
    window.mainloop()

