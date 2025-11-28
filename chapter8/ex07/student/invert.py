from images import Image

def invert(image):
    w = image.getWidth()
    h = image.getHeight()
    for x in range(w):
        for y in range(h):
            r, g, b = image.getPixel(x, y)
            image.setPixel(x, y, (255 - r, 255 - g, 255 - b))

def main():
    filename = input("Enter the image file name: ")
    img = Image(filename)
    invert(img)
    img.draw()

main()
