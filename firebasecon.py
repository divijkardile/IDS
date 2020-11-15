from firebase import firebase
import os
import tkinter.messagebox as tkMessageBox
#from intruptLogin import *
import intruptLogin as il
#from usb import *

try:
    firebase = firebase.FirebaseApplication("https://fir-con-5932e.firebaseio.com/", None)
except:
    tkMessageBox.showinfo('Message', 'Cannot connect to internet please check your Internet Connection!!!')

data = {
    'InOut':'True'
}

#To insert record
result = firebase.post("/fir-con-5932e/Login", data)
print(result)

#To get record
while True:
    #try:
    result = firebase.get("/fir-con-5932e/Login/-M49ieZenKigrVjHsT0W", "InOut")
        #print(result)

    if result == "True":
        print("True...")
    else:
        #disableUSBPort()
        print("Flase...")
        #firebase.put("/fir-con-5932e/Login/-M49ieZenKigrVjHsT0W", "InOut", "False")
        il.login1()
    #except:
        #tkMessageBox.showinfo('Message', 'Cannot connect to internet please check your Internet Connection!!!')

#To update record
#firebase.put("/fir-con-5932e/Login/-M49ieZenKigrVjHsT0W", "InOut", "True")
#print("Record Updated")

#To delete record
#firebase.delete("/fir-con-5932e/Login/", "-M49iwexat0jPWOW1Q7u")
