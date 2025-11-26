import turtle
import math

def drawCircle(t, x, y, radius):
    """
    Draws a circle with the given Turtle object, center (x, y), and radius.
    The circle is drawn by turning 3 degrees and moving a calculated distance 120 times.
    """
    # Calculate step length along the circumference
    step_length = 2.0 * math.pi * radius / 120.0

    # Move the turtle to the starting point without drawing
    t.penup()
    t.goto(x, y - radius)  # start at bottom of circle
    t.pendown()

    # Draw the circle
    for _ in range(120):
        t.forward(step_length)
        t.left(3)

# Example usage:
if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    drawCircle(t, 0, 0, 100)
    screen.mainloop()
