import cv2,os
import numpy as np
from PIL import Image, ImageTk


def getImagesAndLabels(path, detector):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:

        pilImage=Image.open(imagePath).convert('L')

        imageNp=np.array(pilImage,'uint8')

        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(imageNp)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            #print(Id)
            Ids.append(Id)
        cv2.imshow("training",imageNp)
        cv2.waitKey(10)

    return Ids, faceSamples

def trainImage():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    path = 'dataSet'
    #print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    Ids, faceSamples = getImagesAndLabels(path, detector)
    recognizer.train(faceSamples, np.array(Ids))
    recognizer.save('recognizer/trainningData.yml')
    cv2.destroyAllWindows()
    #print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(Ids))))

if __name__ == "__main__":
    trainImage()
