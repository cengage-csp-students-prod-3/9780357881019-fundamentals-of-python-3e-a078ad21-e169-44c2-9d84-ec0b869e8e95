# testshapes.py

import turtle
from shapes import Line, Rectangle, Circle

# Set window starting location at (0,0)
turtle.setup(1000, 600, 0, 0)

# -------------------------
# HOUSE
# -------------------------

# House base (rectangle)
house = Rectangle(-300, -100, 250, 150, color="black")
house.draw()

# Roof (two angled red lines)
roof1 = Line(-300, 50, -230, 100, color="red")
roof2 = Line(-50, 50, -120, 100, color="red")
roof3 = Line(-230, 100, -120, 100, color="red")
roof1.draw()
roof2.draw()
roof3.draw()

# Door (small blue rectangle)
door = Rectangle(-200, -100, 40, 70, color="blue")
door.draw()

# -------------------------
# STICK FIGURE
# -------------------------

# Head
head = Circle(150, 80, 30, color="black")
head.draw()

# Body
body = Line(150, 50, 150, -50, color="black")
body.draw()

# Arms
arm = Line(100, 0, 200, 0, color="black")
arm.draw()

# Legs
leg1 = Line(150, -50, 120, -120, color="black")
leg2 = Line(150, -50, 180, -120, color="black")
leg1.draw()
leg2.draw()

# Finish turtle graphics
turtle.done()
