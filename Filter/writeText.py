from PIL import Image, ImageDraw, ImageFont

im = Image.open("cat.jpg")
font = ImageFont.truetype("Lobster-Regular.ttf", 40)
draw = ImageDraw.Draw(im)
draw.text((0,0), "Китайский кот", (120,255,255), font=font)
im.show()
