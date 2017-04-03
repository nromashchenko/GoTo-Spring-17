from PIL import Image

im = Image.open("cat.jpg")

r, g, b = im.split()

r_pixels = r.load()
print(r_pixels[0,0])

g_pixels = g.load()
print(g_pixels[0,0])

im = Image.merge("RGB", (b, g, r))