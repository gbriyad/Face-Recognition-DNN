from tkinter import *

canvas = None
root = None
name = None


def load_UI():
    global name
    global root
    root = Tk()

    view_frame = Frame(root)
    view_frame.pack(side=LEFT)

    info_frame = Frame(root)
    info_frame.pack(side=RIGHT)

    global canvas
    canvas = Canvas(view_frame, width=500, height=500)
    canvas.pack()

    rcanvas = Canvas(info_frame, width=500, height=500)
    rcanvas.pack()

    name = Text(rcanvas)
    name.pack()


def setImage(photo):
    global canvas
    canvas.create_image(0, 0, image=photo, anchor=NW)


def update():
    global root
    root.update_idletasks()
    root.update()

def setName(n):
    global name
    print (n)
    name.insert(INSERT,n)