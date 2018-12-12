import PIL.Image, PIL.ImageTk
import cv2
from tkinter import *
root = Tk()

view_frame = Frame(root)
view_frame.pack(side=LEFT)

info_frame = Frame(root)
info_frame.pack(side=RIGHT)

video_capture = cv2.VideoCapture(0)

canvas = Canvas(view_frame, width = 500, height = 500)
canvas.pack()

rcanvas = Canvas(info_frame, width = 500, height = 500)
rcanvas.pack()

name=Text(rcanvas)
name.insert(INSERT,"hello")
name.pack()

while True:
    ret, frame = video_capture.read()
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0,0, image=photo,anchor =NW)
    root.update_idletasks()
    root.update()
