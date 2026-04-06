import random
from PIL import Image

def dim_eight_pixels_image():
    im = Image.open("palette_more_pixels.png")
    im_dim = Image.new("RGB", (im.width, im.height))
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            r = int(r / 2)
            g = int(g / 2)
            b = int(b / 2)
            im_dim.putpixel((col, row), (r, g, b))
    im_dim.save("img1_palette_dim.png")

def blue_washed_image():
    im = Image.open("rick_and_morty.png")
    im_blue = Image.new("RGB", [im.width, im.height])
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            im_blue.putpixel((col, row), (0, 0, b))
    im_blue.save("img2_rick_blue_washed.png")

def create_alternate_lines(width, height):
    im = Image.new("RGB", (width, height))
    for row in range(height):
        for col in range(width):
            if row % 2 == 0:
                im.putpixel((col, row), (255, 255, 255))
            else:
                im.putpixel((col, row), (0, 0, 0))
    im.save("img3_alternate_lines.png")

def create_random_noise(width, height):
    im = Image.new("RGB", (width, height))
    for row in range(height):
        for col in range(width):
            if random.random() > 0.5:
                im.putpixel((col, row), (255, 255, 255))
            else:
                im.putpixel((col, row), (0, 0, 0))
    im.save("img4_random.png")

def decode_image():
    im = Image.open("rick_encoded.png")
    im_secret = Image.new("RGB", [im.width, im.height])
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            if r % 2 == 1:
                im_secret.putpixel((col, row), (0, 0, 0))
            else:
                im_secret.putpixel((col, row), (255, 0, 0))
    im_secret.save("img5_rick_secret.png")

if __name__ == "__main__":
    dim_eight_pixels_image()
    blue_washed_image()
    create_alternate_lines(100, 120)
    create_random_noise(150, 150)
    decode_image()
