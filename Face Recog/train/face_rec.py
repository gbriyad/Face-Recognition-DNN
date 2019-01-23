import os
import threading

import face_recognition
import cv2
import datetime
import ui.ui as ui
import mysql.connector

NAME_COL=0
INFO_COL=1
IMAGE_COL=3

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="face_rec"
)


only_detect = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")


def count_total_image_files():
    my_cursor = my_db.cursor()
    my_cursor.execute("select * from person")
    my_cursor.fetchall()
    row_number=my_cursor.rowcount
    my_cursor.close()
    return row_number



def load_and_encode_images():
    msg = ui.get_msg_setter()
    msg.set("Loading")
    known_face_encodings = []
    known_face_names = []
    known_face_info =[]

    total_image = str(count_total_image_files())
    msg.set(total_image + ' Images Found')
    cnt = 0

    my_cursor = my_db.cursor()
    my_cursor.execute("select * from person")
    record=my_cursor.fetchall()
    for row in record:
        #msg.set(str(cnt) + " out of " + total_image + ' images Trained.\nNow Training image: ' + file)
        image = face_recognition.load_image_file(row[IMAGE_COL])
        a = datetime.datetime.now()
        face_encoding = face_recognition.face_encodings(image)[0]
        print(datetime.datetime.now() - a)
        known_face_encodings.append(face_encoding)
        known_face_names.append(row[NAME_COL])
        if row[INFO_COL]:
            known_face_info.append(row[INFO_COL])
        else:
            known_face_info.append('No information available.')
        cnt += 1


    msg.set(str(cnt) + " out of " + total_image + ' images Trained.')
    return known_face_encodings, known_face_names, known_face_info


def recognize(known_face_encodings, known_face_names, known_face_info, frame):
    if known_face_names is None:
        return None, None, None

    name = ""
    info = ""

    small_frame = cv2.resize(frame, (0, 0), fx=0.20, fy=0.20)
    rgb_small_frame = small_frame[:, :, ::-1]



    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            info = known_face_info[first_match_index]

        face_names.append(name)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    return frame, name, info
