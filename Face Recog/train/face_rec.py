
import os

import face_recognition
import cv2
import datetime




def loadAndEncodeImages():
    known_face_encodings = []
    known_face_names = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "images")

    cnt=1
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            cnt+=1
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root)
                # print(label, path)

                image = face_recognition.load_image_file(path)
                a=datetime.datetime.now()
                face_encoding = face_recognition.face_encodings(image)[0]
                print(datetime.datetime.now()-a)
                known_face_encodings.append(face_encoding)
                known_face_names.append(file.split(".")[0])
                print(file)

    return known_face_encodings, known_face_names

def recognize(known_face_encodings, known_face_names, frame):
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    name =""


    small_frame = cv2.resize(frame, (0, 0), fx=0.20, fy=0.20)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    return frame, name




