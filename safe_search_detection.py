from __future__ import print_function
from google.cloud import vision
client = vision.Client()
image = client.image(source_uri='gs://gracewan-images-bucket/safe.jpg')
safe_search = image.detect_safe_search()
print('Adult:',end='\t\t')
print(safe_search.adult)
print('Spoof:',end='\t\t')
print(safe_search.spoof)
print('Medical:',end='\t')
print(safe_search.medical)
print('Violence:',end='\t')
print(safe_search.violence)
