# sharpen.py

def sharpen(image, degree, threshold):
    """Sharpens an image by darkening pixels that lie along edges.
       image     : Image object
       degree    : amount to darken sharp edges
       threshold : how strong an edge must be detected"""

    width = image.getWidth()
    height = image.getHeight()

    # Clone so we don’t overwrite pixels we still need to read
    source = image.clone()

    for x in range(width - 1):
        for y in range(height - 1):

            # Current pixel
            r1, g1, b1 = source.getPixel(x, y)

            # Neighbor pixel (right)
            r2, g2, b2 = source.getPixel(x + 1, y)

            # Compute intensity difference
            diff = abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2)

            if diff > threshold:
                # This is an edge -> darken by degree
                r = max(0, r1 - degree)
                g = max(0, g1 - degree)
                b = max(0, b1 - degree)
                image.setPixel(x, y, (r, g, b))
            else:
                # Not an edge -> leave original color
                image.setPixel(x, y, (r1, g1, b1))
