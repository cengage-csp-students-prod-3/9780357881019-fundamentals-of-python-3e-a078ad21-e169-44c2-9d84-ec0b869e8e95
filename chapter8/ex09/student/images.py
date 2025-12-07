# colorfilter.py

def lighten(image, amount):
    """Lightens the image by increasing each RGB value by 'amount'.
       Stops at the limit 255."""
    width = image.getWidth()
    height = image.getHeight()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getPixel(x, y)
            r = min(255, r + amount)
            g = min(255, g + amount)
            b = min(255, b + amount)
            image.setPixel(x, y, (r, g, b))


def darken(image, amount):
    """Darkens the image by decreasing each RGB value by 'amount'.
       Stops at the limit 0."""
    width = image.getWidth()
    height = image.getHeight()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getPixel(x, y)
            r = max(0, r - amount)
            g = max(0, g - amount)
            b = max(0, b - amount)
            image.setPixel(x, y, (r, g, b))


def colorFilter(image, rgb):
    """Applies a color filter. rgb = (rChange, gChange, bChange)
       Each pixel's RGB values are adjusted by these amounts."""
    (dr, dg, db) = rgb
    width = image.getWidth()
    height = image.getHeight()

    for x in range(width):
        for y in range(height):
            r, g, b = image.getPixel(x, y)
            r = min(255, max(0, r + dr))
            g = min(255, max(0, g + dg))
            b = min(255, max(0, b + db))
            image.setPixel(x, y, (r, g, b))
