from images import Image

def posterize(image, color):
    w = image.getWidth()
    h = image.getHeight()
    for x in range(w):
        for y in range(h):
            r, g, b = image.getPixel(x, y)
            # Ortalama 128 eşik değeri: üstü seçilen renk, altı beyaz
            if (r + g + b) / 3 >= 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel(x, y, (255, 255, 255))

def main():
    filename = input("Enter the image file name: ")
    r = int(input("Enter an integer [0..255] for red: "))
    g = int(input("Enter an integer [0..255] for green: "))
    b = int(input("Enter an integer [0..255] for blue: "))

    img = Image(filename)
    posterize(img, (r, g, b))
    img.draw()

main()

