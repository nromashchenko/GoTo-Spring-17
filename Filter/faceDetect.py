import requests, json
from PIL import Image,ImageDraw

file = open("family.jpeg", "rb")
content = file.read()

result = requests.post("https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize", data=content,
                       headers={"Content-Type": "application/octet-stream",
                                "Ocp-Apim-Subscription-Key": "ed949f112a524980ad1907524eb7d32d"})
face_result = json.loads(result.text)

for face in face_result:
    print(" ---------------------- ")
    rectangle = face['faceRectangle']
    print("x: ", rectangle['left'])
    print("y: ", rectangle['top'])
    print("width: ", rectangle['width'])
    print("height: ", rectangle['height'])
