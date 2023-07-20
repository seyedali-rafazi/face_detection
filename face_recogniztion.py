import os
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0

def sort_images(source_folder):
    face_folder = 'faces'
    no_face_folder = 'no_faces'

    if not os.path.exists(face_folder):
        os.mkdir(face_folder)
    
    if not os.path.exists(no_face_folder):
        os.mkdir(no_face_folder)

    for filename in os.listdir(source_folder):
        if detect_faces(os.path.join(source_folder, filename)):
            image_path = os.path.join(source_folder, filename)
            new_path = os.path.join(face_folder, filename)
            os.rename(image_path, new_path)
        else:
            image_path = os.path.join(source_folder, filename)
            new_path = os.path.join(no_face_folder, filename)
            os.rename(image_path, new_path)

source_folder = 'New folder'
sort_images(Image_sourses)