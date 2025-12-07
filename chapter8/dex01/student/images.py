from images import Image
import random

def main():
    """Generates and saves images with random colors.
    Inputs: The image's width, height,
    and output file name."""
    width = int(input("Enter the image's width: "))
    height = int(input("Enter the image's height: "))
    fileName = input("Enter the image's file name: ")

    # Create a table of 256 unique colors for GIF image
    colors = []
    while len(colors) < 256:   # FIXED (255 → 256)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if (r, g, b) not in colors:
            colors.append((r, g, b))

    image = Image(width, height)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            color = random.choice(colors)
            image.setPixel(x, y, color)

    print("Close the image window to quit.")
    image.draw()
    image.save(fileName)

if __name__ == "__main__":
    main()
