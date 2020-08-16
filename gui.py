from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import os
import face_detection
from functools import partial
import numpy as np
import cv2

root = Tk()
root.geometry("700x600")
root.config(background="#ffffff")
logo = ImageTk.PhotoImage(Image.open("Resources/logo_icon.png"))
logo_img = Label(root, image = logo,background="#ffffff")

# Face Detection
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#
# def face_detector(img):
#
# 	faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)
# 	if faces is():
# 		return None
# 	else:
# 		return faces
#
# def capture(id = "m"):
#
# 	cap = cv2.VideoCapture(0)
# 	count=0
# 	while(True):
# 		ret, frame = cap.read()
# 		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 		faces=face_detector(gray)
# 		if faces is not None:
# 			for (x,y,w,h) in faces:
# 				print(x, y, w, h)
# 				color = (255, 0, 0)
# 				stroke = 2
# 				x2 = x + w
# 				y2 = y + h
# 				cv2.rectangle(frame, (x, y), (x2, y2), color, stroke)
# 				face_crop = gray[y:y2, x:x2]
# 				cv2.imwrite("face_data/"+id+"_"+str(count)+".jpg",face_crop)
# 				count+=1
# 				cv2.imshow('frame', frame)
# 				if count == 50:
# 					break
#
# 			if count == 50:
# 				break
# 		if cv2.waitKey(20) & 0xFF == ord('q'):
# 			break
# 	cap.release()
# 	cv2.destroyAllWindows()
#Function goes here

def take_attendence():
    messagebox.showinfo("Take Attendence", "This function is not available now")
def check_attendence():
    messagebox.showinfo("Take Attendence", "This function is not available now")
def register_user():
    ##NEW SEPERATE WINDOW FOR NEW USER REGISTRATION
    register=Tk()
    register.title("Register New User")
    register.geometry("500x400")
    register.config(background="#ffffff")
    id_label=Label(register,text="User ID", font=("Arial sans MS",14,"bold"),background="#ffffff")
    id_input=Entry(register,bd=2,width="30",font=("Arial sans MS",14))
    name_label=Label(register,text="User Name",font=("Arial sans MS",14,"bold"),background="#ffffff")
    name_input=Entry(register,bd=2,width="30",font=("Arial sans MS",14))
    take_face = Button(register,
                             text="Take Face",
                             width="30",
                             height="2",
                             background="#000000",
                             foreground="#ffffff",
                             activeforeground="#ff0000",
                             command=lambda: face_detection.capture(str(id_input.get()))
                             )
    complete_registration = Button(register,
                       text="Register",
                       width="30",
                       height="2",
                       background="#000000",
                       foreground="#ffffff",
                       activeforeground="#ff0000"
                       )
    id_label.pack(pady=(30,0))
    id_input.pack()
    name_label.pack(pady=(30,0))
    name_input.pack()
    take_face.pack(pady="30")
    complete_registration.pack()
    register.mainloop()
def exit_app():
    root.destroy()

##COMPONENTS HERE

heading=Label(
    root,
    text="Attendence Management System",
    font=("Comic sans MS",24,"bold"),
    background="#ffffff"
)
take_attendence=Button(root,
                       text="Take Attendence",
                       width="30",
                       height="2",
                       background="#000000",
                       foreground="#ffffff",
                       activeforeground="#ff0000",
                       command=take_attendence)
check_attendence=Button(root,
                        text="Check Attendence",
                        width="30",
                        height="2",
                        background="#000000",
                        foreground="#ffffff",
                        activeforeground="#ff0000",
                        command=check_attendence
                        )
register_user=Button(root,
                     text="Register New User",
                     width="30",
                     height="2",
                     background="#000000",
                     foreground="#ffffff",
                     activeforeground="#ff0000",
                     command=register_user
                     )
exit_btn=Button(root,
                text="Exit",
                width="30",
                height="2",
                background="#000000",
                foreground="#ffffff",
                activeforeground="#ff0000",
                command=exit_app
                )

logo_img.pack(pady="30")
heading.pack(pady=(0,30))
take_attendence.pack(pady=(0,30))
check_attendence.pack(pady=(0,30))
register_user.pack(pady=(0,30))
exit_btn.pack(pady=(0,30))
root.mainloop()
