import cv2
from PIL import Image
import os
import numpy as np

def getImagesData(path):
    #path to all the images in the folder
    imagesPath = [os.path.join(path,f) for f in os.listdir(path)]

    #List to contain faces
    faces = []
    #List to contain Ids
    ids = []

    for imagePath in imagesPath:
        pilImage = Image.open(imagePath).convert('L')
        imgnp = np.array(pilImage, 'uint8')

        Id = int(os.path.split(imagePath)[-1].split("_")[1])

        faces.append(imgnp)
        ids.append(Id)

    return faces, ids

def Training():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    faces, ids = getImagesData('face_data')
    recognizer.train(faces, np.array(ids))
    recognizer.save('Trained_Recognizer/trainner.yml')
