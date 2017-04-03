from PIL import Image, ImageDraw, ImageFont

im = Image.open("cat.jpg")
font = ImageFont.truetype("Lobster-Regular.ttf", 40)
draw = ImageDraw.Draw(im)

size = draw.textsize("Китайский кот", font=font)

draw.text((im.width//2-size[0]//2, im.height//2-size[1]//2),
          "Китайский кот", (120, 255, 120), font=font)
im.show()
