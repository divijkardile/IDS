import cv2
import sqlite3
import tkinter.messagebox as tkMessageBox

def insertorUpdate(Id, Name, Age, Phone):
    try:
        conn = sqlite3.connect("recface.db")
        cmd = "SELECT * FROM people WHERE ID ="+str(Id)
        cursor = conn.execute(cmd)
        isRecordExist = 0
        for row in cursor:
            isRecordExist = 1
        if(isRecordExist == 1):
            cmd = "UPDATE people SET Name = "+str(Name)+","+"Age = "+str(Age)+","+"Phone = "+str(Phone)+" WHERE ID = "+str(Id)
        else:
            cmd = "INSERT INTO people(ID, Name, Age, Phone) VALUES("+str(Id)+","+str(Name)+","+str(Age)+","+str(Phone)+")"
        conn.execute(cmd)
        conn.commit()
        conn.close()
    except:
        tkMessageBox.showinfo('Message', 'Cannot connect to databases!!!')

def extract(img, detector):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.5, 5)
    if faces is():
        return None
    for (x,y,w,h) in faces:
        crop = img[y:y+h,x:x+w]
    return crop

def get(Id, Name, Age, Phone):
    cam = cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    insertorUpdate(Id, Name, Age, Phone)
    sampleNum=0
    while(True):
        ret, img = cam.read()
        if extract(img, detector) is not None:
            faces = cv2.resize(extract(img, detector),(200,200))
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)

            sampleNum=sampleNum+1
            ID = str(Id)
            cv2.imwrite("dataSet/User."+ID +'.'+ str(sampleNum) + ".jpg", faces)
            name = str(sampleNum)
            font = cv2.FONT_HERSHEY_DUPLEX
            color = (0,255,0)
            stroke = 2
            cv2.putText(faces, name, (50, 50), font, 1, color, stroke)
            cv2.imshow('frame',faces)
        else:
            #print("ERROR!!!!")
            pass
        #wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum>80:
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    get(Id, Name, Age, Phone)
