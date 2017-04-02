from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(source_uri='gs://gracewan-images-bucket/selfie.png')
faces = image.detect_faces(limit=10)
for i, face in enumerate(faces):
    print('Face {0}:'.format(i+1))
    print('landmarks.left_eye.landmark_type:',end=' ')
    print(face.landmarks.left_eye.landmark_type)
    print('landmarks.left_eye.position.x_coordinate:',end=' ')
    print(face.landmarks.left_eye.position.x_coordinate)
    print('detection_confidence:',end=' ')
    print(face.detection_confidence)
    print('joy:',end=' ')
    print(face.joy)
    print('anger:',end=' ')
    print(face.anger,end='\n\n')
