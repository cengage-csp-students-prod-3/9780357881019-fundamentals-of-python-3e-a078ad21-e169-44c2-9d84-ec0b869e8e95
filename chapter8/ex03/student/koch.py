# Write your code here# koch.py
from turtle import Turtle, Screen

def drawFractalLine(t, distance, angle, level):
    """Draws a Koch fractal line using recursion."""
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        # Each segment is 1/3 of the current distance
        new_distance = distance / 3
        # Draw the four segments for the Koch line
        drawFractalLine(t, new_distance, angle, level - 1)
        drawFractalLine(t, new_distance, angle + 60, level - 1)
        drawFractalLine(t, new_distance, angle - 60, level - 1)
        drawFractalLine(t, new_distance, angle, level - 1)

def drawKochSnowflake(t, distance, level):
    """Draws the Koch snowflake using three Koch fractal lines."""
    angles = [0, -120, 120]  # Initial angles for the three sides
    for angle in angles:
        drawFractalLine(t, distance, angle, level)

def main():
    screen = Screen()
    screen.bgcolor("white")

    t = Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(-150, 100)  # Starting position
    t.pendown()

    distance = 300  # Length of each side
    level = 3       # Change this to increase/decrease fractal complexity

    drawKochSnowflake(t, distance, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
