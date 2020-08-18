import cv2
import datetime
import time
import os
import pandas as pd

def face_detector(img):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
	faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)
	if faces is ():
		return None
	else:
		return faces

def CheckImage():
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("Trained_Recognizer/trainner.yml")
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    df=pd.read_csv("Attendance_Record/AttendanceDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)
    while True:
        ret, frame =cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_detector(gray)
        if faces is not None:
                for (x,y,w,h) in faces:
                    print(x, y, w, h)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
                    if(conf < 50):
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        aa=df.loc[df['Id'] == Id]['Name'].values
                        tt=str(Id)+"-"+aa
                        attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                    else:
                        Id='Unknown'
                        tt=str(Id)
                    cv2.putText(frame,str(tt),(x,y+h), font, 1,(255,255,255),2)
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
        cv2.imshow('frame', frame)
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance_Record/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    return attendance
