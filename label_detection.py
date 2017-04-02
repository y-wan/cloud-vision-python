from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(source_uri='gs://gracewan-images-bucket/donuts.png')
labels = image.detect_labels(limit=5)
for i, label in enumerate(labels):
    print('Label {0}:'.format(i+1))
    print(label.description+'\n'+str(label.score)+'\n')
