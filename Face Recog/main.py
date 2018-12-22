import threading

import train.face_rec as train
import cv2
import PIL.Image, PIL.ImageTk
import ui.ui as ui
known_face_encodings = None
known_face_names= None

def trainModel():
    global known_face_encodings,known_face_names
    known_face_encodings, known_face_names = train.loadAndEncodeImages()


ui.load_UI(trainModel)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()


    recognized_frame, name=train.recognize(known_face_encodings, known_face_names, frame)
    if recognized_frame is None:
        recognized_frame = frame
        ui.setMsg("Please Train the Model First")

    b, g, r = cv2.split(recognized_frame)
    recognized_frame = cv2.merge((r, g, b))
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(recognized_frame))

    ui.setImage(photo)
    if name is not None:
        ui.setName(name, None)
    ui.update()