# shapes.py
import turtle
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for all shapes."""

    def __init__(self, color="black"):
        self.color = color
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.color(self.color)

    @abstractmethod
    def draw(self):
        pass


class Line(Shape):
    """A line segment from (x1, y1) to (x2, y2)."""

    def __init__(self, x1, y1, x2, y2, color="black"):
        super().__init__(color)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def draw(self):
        self.t.penup()
        self.t.goto(self.x1, self.y1)
        self.t.pendown()
        self.t.goto(self.x2, self.y2)


class Rectangle(Shape):
    """A rectangle defined by bottom-left corner, width, and height."""

    def __init__(self, x, y, width, height, color="black"):
        super().__init__(color)
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def draw(self):
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

        self.t.forward(self.w)
        self.t.left(90)
        self.t.forward(self.h)
        self.t.left(90)
        self.t.forward(self.w)
        self.t.left(90)
        self.t.forward(self.h)
        self.t.left(90)   # Back to original direction


class Circle(Shape):
    """A circle defined by a center point and a radius."""

    def __init__(self, x, y, radius, color="black"):
        super().__init__(color)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.t.penup()
        self.t.goto(self.x, self.y - self.radius)
        self.t.pendown()
        self.t.circle(self.radius)
