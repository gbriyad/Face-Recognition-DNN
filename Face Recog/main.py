import train.face_rec as train
import cv2
import PIL.Image, PIL.ImageTk
import ui.ui as ui


ui.load_UI()
a,b=train.loadAndEncodeImages()

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    frame, name=train.recognize(a, b, frame)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    ui.setImage(photo)
    ui.setName(name)
    ui.update()