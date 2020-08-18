from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import os
import face_detection
import training
import check
from functools import partial
import numpy as np
import cv2

class Start:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.geometry("700x600")

        self.logo = ImageTk.PhotoImage(Image.open("Resources/logo_image.png"))
        self.logo_img = Label(self.frame, image = self.logo)
        self.heading=Label(self.frame, text="Attendence Management System", font=("Comic sans MS",24,"bold"))
        self.take_attendence=Button(self.frame,
                               text="Take Attendence",
                               width="30",
                               height="2",
                               background="#000000",
                               foreground="#ffffff",
                               activeforeground="#ff0000",
                               command=self.take_attendence
                               )
        self.check_attendence=Button(self.frame,
                                text="Check Attendence",
                                width="30",
                                height="2",
                                background="#000000",
                                foreground="#ffffff",
                                activeforeground="#ff0000",
                                command=self.check_attendence
                                )
        self.register_user=Button(self.frame,
                             text="Register New User",
                             width="30",
                             height="2",
                             background="#000000",
                             foreground="#ffffff",
                             activeforeground="#ff0000",
                             command=self.new_window
                             )
        self.exit_btn=Button(self.frame,
                        text="Exit",
                        width="30",
                        height="2",
                        background="#000000",
                        foreground="#ffffff",
                        activeforeground="#ff0000",
                        command=self.exit_app
                        )
        self.notif1 = Label(self.frame,text="",font=("Arial sans MS",14,"bold"),fg="red")
        self.logo_img.pack(pady="30")
        self.heading.pack(pady=(0,30))
        self.take_attendence.pack(pady=(0,30))
        self.check_attendence.pack(pady=(0,30))
        self.register_user.pack(pady=(0,30))
        self.exit_btn.pack(pady=(0,30))
        self.notif1.pack(pady=(30,0))
        self.frame.pack()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = register_user(self.newWindow)

    def take_attendence(self):
        attendance = check.CheckImage()
        msg = attendance
        self.notif1.configure(text=msg)
    def check_attendence(self):
        messagebox.showinfo("Take Attendence", "This function is not available now")

    def exit_app(self):
        self.master.destroy()

class register_user:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.master.title("Register New User")
        self.master.geometry("500x400")
        self.id_label=Label(self.frame,text="User ID", font=("Arial sans MS",14,"bold"))
        self.id_input=Entry(self.frame,bd=2,width="30",font=("Arial sans MS",14))

        self.name_label=Label(self.frame,text="User Name",font=("Arial sans MS",14,"bold"))
        self.name_input=Entry(self.frame,bd=2,width="30",font=("Arial sans MS",14))
        self.take_face = Button(self.frame,
                                 text="Take Face",
                                 width="30",
                                 height="2",
                                 background="#000000",
                                 foreground="#ffffff",
                                 activeforeground="#ff0000",
                                 command=lambda: self.face_capture(self.id_input.get(), self.name_input.get())
                                 )
        self.complete_registration = Button(self.frame,
                           text="Register",
                           width="30",
                           height="2",
                           background="#000000",
                           foreground="#ffffff",
                           activeforeground="#ff0000",
                           command=self.train_images
                           )
        self.notif1 = Label(self.frame,text="",font=("Arial sans MS",14,"bold"),fg="red")

        self.id_label.pack(pady=(30,0))
        self.id_input.pack()
        self.name_label.pack(pady=(30,0))
        self.name_input.pack()
        self.take_face.pack(pady="30")
        self.complete_registration.pack()
        self.notif1.pack(pady=(30,0))
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def face_capture(self, id, name):
        self.id = id
        self.name = name
        if (self.is_number(self.id) and self.name.isalpha()):
            face_detection.capture(self.id, self.name)
            msg = "Images Recorded for ID: "+self.id+" Name: "+self.name
            self.notif1.configure(text=msg)
        else:
            if self.is_number(self.id):
                msg = "Notification: Invalid Name"
                self.notif1.configure(text=msg)
            if self.name.isalpha():
                msg = "Notification: ID should be number"
                self.notif1.configure(text=msg)

    def train_images(self):
        training.Training()
        self.master.destroy()



def main():
    root = Tk()
    app = Start(root)
    root.mainloop()

if __name__ == '__main__':
    main()
