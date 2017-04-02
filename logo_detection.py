from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(source_uri='gs://gracewan-images-bucket/logos.png')
logos = image.detect_logos(limit=10)
for i, logo in enumerate(logos):
    print('Logo {0}:'.format(i+1))
    print(logo.description+'\n'+str(logo.score)+'\n'+str(logo.bounds.vertices[0].x_coordinate)+'\n'+str(logo.bounds.vertices[0].y_coordinate)+'\n')
