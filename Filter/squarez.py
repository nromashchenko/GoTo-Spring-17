from PIL import Image, ImageFilter


def paint_blue(im):
    pixels = im.load()
    for i in range(im.width):
        for j in range(im.height):
            r, g, b = pixels[i, j]
            b = min(b + 100, 255)
            pixels[i, j] = (r, g, b)

def paint(im):
    pixels = im.load()
    for i in range(im.width):
        for j in range(im.height):
            r, g, b = pixels[i, j]
            g = min(g + 100, 255)
            pixels[i, j] = (r, g, b)

source = Image.open("cat.jpg")

result = source.copy()

x = result.width//9
y = result.width//9

box = (x,y,source.width-x, source.height-y)
square = source.crop(box)
paint(square)
paint_blue(result)
result.paste(square, box)
result = result.filter(ImageFilter.BLUR)


x = 2*result.width//9
y = 2*result.width//9

box = (x,y,source.width-x, source.height-y)
square = source.crop(box)
result.paste(square, box)

result.show()
