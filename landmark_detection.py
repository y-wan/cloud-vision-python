from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(filename='res/selfie.png')
landmarks = image.detect_landmarks(limit=5)
for i, landmark in enumerate(landmarks):
    print('Landmark {0}:'.format(i+1))
    print(landmark.description+'\n'+str(landmark.locations[0].latitude)+'\n'+str(landmark.locations[0].longitude)+'\n'+str(landmark.score)+'\n')
