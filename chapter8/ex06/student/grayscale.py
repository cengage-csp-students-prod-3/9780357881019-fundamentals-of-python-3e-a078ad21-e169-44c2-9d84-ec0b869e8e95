# Write your code here
from images import Image

def grayscale(image):
    w = image.getWidth()
    h = image.getHeight()
    for x in range(w):
        for y in range(h):
            r, g, b = image.getPixel(x, y)
            gray = int((r + g + b) / 3)  # basit ortalama
            image.setPixel(x, y, (gray, gray, gray))

def main():
    filename = input("Enter the image file name: ")
    img = Image(filename)
    grayscale(img)
    img.draw()

main()
