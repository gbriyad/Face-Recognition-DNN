import threading
from tkinter import *
canvas = None
root = None
name = None
msg = None
v = None




def load_UI(trainCallback):
    print(threading.currentThread())
    global name, root, msg, canvas, v
    root = Tk()
    v=StringVar()

    view_frame = Frame(root, width=500, height=500)
    view_frame.grid(row=0, column=0)

    canvas = Canvas(view_frame, width=600, height=500)
    canvas.grid(row=0,column=0, padx=10, pady=10)

    info_frame = Frame(root, width=500, height=500)
    info_frame.grid(row=0, column=1)

    trainButton = Button(info_frame, text="Train Model", command=trainCallback
                         , width=25, height=3)
    trainButton.grid(row=0, column=0, padx=10, pady=10)


    name = Text(info_frame, width=50, height=10)
    name.grid(row=1,column=0, padx=10, pady=10)


    msg = Label(info_frame, width=50, height=10, textvariable=v)
    msg.grid(row=2,column=0, padx=10, pady=10)





def setImage(photo):
    global canvas
    canvas.create_image(0, 0, image=photo, anchor=NW)


def update():
    print(threading.currentThread())
    global root
    root.update_idletasks()
    root.update()

def setName(n,info):
    global name
    name.delete(1.0,END)
    if info:
        name.insert(INSERT,"Name: "+ n)
    else:
        name.insert(INSERT,"Name: "+ n)
def setMsg(text):
    global msg,v
    v.set(text)

def get_msg_setter():
    global v
    return v