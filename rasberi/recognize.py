import cv2, os
import numpy as np
import sqlite3
import datetime
import time
import csv
import tkinter.messagebox as tkMessageBox
import pandas as pd
from firebase import firebase

def addrecord(_attendance):
    conn = sqlite3.connect("recface.db")
    tablename = "Entry"
    _attendance.to_sql(tablename, conn, if_exists = 'append', index = False)
    conn.commit()
    conn.close()

def getProfile(id):
    conn = sqlite3.connect("recface.db")
    cmd = "SELECT * FROM people WHERE ID ="+str(id)
    cursor = conn.execute(cmd)
    Profile = None
    for row in cursor:
        Profile = row
    conn.close()
    return Profile


def recognizePerson():
    _firebase = firebase.FirebaseApplication("https://fir-con-5932e.firebaseio.com/", None)
    col_names =  ['Id', 'Name', 'Date', 'Time']
    _attendance = pd.DataFrame(columns = col_names)
    _cascadePath = "haarcascade_frontalface_default.xml"
    _faceCascade = cv2.CascadeClassifier(_cascadePath);

    try:
        global _cam
        _cam = cv2.VideoCapture(0)
    except:
        tkMessageBox.showinfo('Message', 'Camera Not Found!!!')

    _recognizer = cv2.face.LBPHFaceRecognizer_create()
    _recognizer.read('recognizer\\trainningData.yml')
    while True:
        tt2 = None
        tt3 = None
        conn = sqlite3.connect("recface.db")
        ret, im = _cam.read()
        #print(ret)
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        _faces= _faceCascade.detectMultiScale(gray, 1.2,5)
        Name = None

        for(x,y,w,h) in _faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),5)
            Id, conf = _recognizer.predict(gray[y:y+h,x:x+w])
            #print(Id)
            #print(conf)
            count = 0;
            if(conf < 70):
                prof = getProfile(Id)
                conf_1 = "  {0}".format(round(100 - conf))
                ts = time.time()
                Date = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d'))
                #print(Date)
                Time = str(datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S'))
                #print(Time)

                if(prof != None):
                    Name = str(prof[1])
                    tt2 = str(prof[0])
                    tt3 = str(prof[2])

                    if(conf < 61 )and(conf > 59):
                        #print("ok u in")
                        _attendance.loc[len(_attendance)] = [Id, Name, Date, Time]
                        _attendance=_attendance.drop_duplicates(subset=['Id'],keep='first')
                        addrecord(_attendance)
            else:
                Id='Unknown'
                #print(Id)
                tt = str(Id)
                conf_1 = "  {0}%".format(round(100 - conf))
            if(conf > 78) and (conf < 80):
                #disableUSBPort()
                #print("Stop!!!!!!!!!!!!!!!!!!!!!")
                try:
                    _firebase.put("/fir-con-5932e/Login/-M49ieZenKigrVjHsT0W", "InOut", "False")
                except:
                    tkMessageBox.showinfo('Message', 'Cannot connect to internet please check Internet Connection!!!')
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])
            cv2.putText(im,str(conf_1),(x,y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
            cv2.putText(im,str(Name),(x,y+h+60), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
        cv2.imshow('Detecting...',im)

        if cv2.waitKey(1)==ord('q'):
            break
    cv2.destroyAllWindows()
    _cam.release()

if __name__ == "__main__":
    recognizePerson()
