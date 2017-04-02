from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(source_uri='gs://gracewan-images-bucket/text.jpg')
texts = image.detect_text()
print(texts[0].locale)
for text in texts:
    print(text.description)
