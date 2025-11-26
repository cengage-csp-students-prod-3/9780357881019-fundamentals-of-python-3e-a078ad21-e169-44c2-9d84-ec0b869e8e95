# Write your code here# mondrian.py
from turtle import Turtle, Screen
import random

def random_color():
    """Return a random color."""
    colors = ["red", "blue", "yellow", "white", "black"]
    return random.choice(colors)

def draw_rectangle(t, x, y, width, height, color):
    """Draw a filled rectangle at (x, y) with given width, height, and color."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def mondrian(t, x, y, width, height, depth, horizontal=True):
    """Recursively draw Mondrian-style subdivisions."""
    if depth == 0 or width < 20 or height < 20:
        # Base case: fill rectangle with a random color
        draw_rectangle(t, x, y, width, height, random_color())
        return

    # Decide the split ratio (1/3 and 2/3)
    if horizontal:
        split = width / 3
        # Left rectangle
        mondrian(t, x, y, split, height, depth - 1, not horizontal)
        # Right rectangle
        mondrian(t, x + split, y, width - split, height, depth - 1, not horizontal)
    else:
        split = height / 3
        # Top rectangle
        mondrian(t, x, y, width, split, depth - 1, not horizontal)
        # Bottom rectangle
        mondrian(t, x, y - split, width, height - split, depth - 1, not horizontal)

def main():
    screen = Screen()
    screen.bgcolor("white")

    t = Turtle()
    t.speed(0)
    t.hideturtle()

    # Initial rectangle parameters
    x, y = -200, 200   # Top-left corner
    width, height = 400, 400
    depth = 4          # Adjust recursion depth

    mondrian(t, x, y, width, height, depth)

    screen.mainloop()

if __name__ == "__main__":
    main()
