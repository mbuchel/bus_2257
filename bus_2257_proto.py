import cv2, os, sys
import numpy as np
import logging as log
import datetime as dt
from PIL import Image
from time import sleep

cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
log.basicConfig(filename='proto.log', level=log.INFO)

images = []
labels = []

rec = cv2.face.createLBPHFaceRecognizer()

def train(path, label):
    images_path = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.txt')]
    for image_path in images_path:
        pil = Image.open(image_path).convert('L')
        image = np.array(pil, "uint8")
        faces = face_cascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(label)
            cv2.imshow("Adding faces to training set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)

path = 'yalefaces'
train(path, 0)
path = 'training_set'
train(path, 1)
cv2.destroyAllWindows()

rec.train(images, np.array(labels))

vid_cap = cv2.VideoCapture(1)
anterior = 0

while True:
    if not vid_cap.isOpened():
        print "unable to load camera."
        sleep(5)
        pass

    ret, frame = vid_cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        if rec.predict(grey[y: y + h, x: x + w]):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Live stream', frame)

vid_cap.release()
cv2.destroyAllWindows()
