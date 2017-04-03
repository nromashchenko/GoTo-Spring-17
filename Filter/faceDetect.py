import requests, json
from PIL import Image,ImageDraw

file = open("family.jpeg", "rb")
content = file.read()

result = requests.post("https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize", data=content,
                       headers={"Content-Type": "application/octet-stream",
                                "Ocp-Apim-Subscription-Key": "ed949f112a524980ad1907524eb7d32d"})
face_result = json.loads(result.text)

family = Image.open("family.jpeg").convert('RGBA')
mask = Image.open("mask.png")

for face in face_result:
    rectangle = face['faceRectangle']
    x = rectangle['left']
    y = rectangle['top']
    w = rectangle['width']
    h = rectangle['height']

    box = (x, y, x + w, y + h)
    m = mask.resize((w, h))
    family.paste(m, box, m)

family.show()

