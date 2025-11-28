from images import Image

def grayscale(image):
    w = image.getWidth()
    h = image.getHeight()
    for x in range(w):
        for y in range(h):
            r, g, b = image.getPixel(x, y)
            gray = int((r + g + b) / 3)
            image.setPixel(x, y, (gray, gray, gray))

def sepia(image):
    grayscale(image)
    w = image.getWidth()
    h = image.getHeight()
    for x in range(w):
        for y in range(h):
            red, green, blue = image.getPixel(x, y)

            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)

            image.setPixel(x, y, (red, green, blue))

def main():
    filename = input("Enter the image file name: ")
    img = Image(filename)
    sepia(img)
    img.draw()

main()
