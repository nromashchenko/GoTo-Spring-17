from PIL import Image

im = Image.open("cat.jpg")
pixels = im.load()

im.show()

for i in range(im.width):
    for j in range(im.height):
        r, g, b = pixels[i, j]
        r = min(255 - r+50,255)
        b = abs(255 - b)
        g = abs(255 - g)
        pixels[i, j] = (r, g, b)

im.show()
