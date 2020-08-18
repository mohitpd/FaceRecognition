import numpy as np
import cv2
import csv

def face_detector(img):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
	faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)
	if faces is():
		return None
	else:
		return faces

def capture(id, name):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
	cap = cv2.VideoCapture(0)
	count=0
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces=face_detector(gray)
		if faces is not None:
			for (x,y,w,h) in faces:
				print(x, y, w, h)
				cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
				face_crop = gray[y:y+h, x:x+w]
				cv2.imwrite("face_data/"+str(name)+'_'+str(id)+"_"+str(count)+".jpg",face_crop)
				count+=1
				cv2.imshow('frame', frame)
				if count == 50:
					break

			if count == 50:
				break
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
	cap.release()
	row = [id , name]
	with open('Attendance_Record\AttendanceDetails.csv','a+') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row)
	csvFile.close()
	cv2.destroyAllWindows()
