from PIL import Image

im = Image.open("cat.jpg")
pixels = im.load()

im.show()

for i in range(im.width):
    for j in range(im.height):
        r, g, b = pixels[i, j]
        a = (r+b+g)//3
        if a<100:
            pixels[i, j] = (0, 0, 0)
        else:
            pixels[i, j] = (200, 255, 255)

im.show()
