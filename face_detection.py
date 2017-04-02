from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(source_uri='gs://gracewan-images-bucket/selfie.png')
faces = image.detect_faces(limit=10)
for i, face in enumerate(faces):
    print('=====Face No.{0}====='.format(i))
    print('landmarks.left_eye.landmark_type',end='\n\t')
    print(face.landmarks.left_eye.landmark_type)
    print('landmarks.left_eye.position.x_coordinate',end='\n\t')
    print(face.landmarks.left_eye.position.x_coordinate)
    print('detection_confidence',end='\n\t')
    print(face.detection_confidence)
    print('joy',end='\n\t')
    print(face.joy)
    print('anger',end='\n\t')
    print(face.anger)
