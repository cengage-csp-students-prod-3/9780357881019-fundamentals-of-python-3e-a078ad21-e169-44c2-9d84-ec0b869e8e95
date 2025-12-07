"""
Program: bouncywithgui.py
GUI version of the Bouncy program from Chapter 3.
Computes the total distance traveled by a bouncing ball.
"""

from breezypythongui import EasyFrame

class BouncyGUI(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Bouncy")

        # Input fields
        self.addLabel(text="Initial height", row=0, column=0)
        self.heightField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Bounciness index", row=1, column=0)
        self.bounceIndexField = self.addFloatField(value=0.0, row=1, column=1)

        self.addLabel(text="Number of bounces", row=2, column=0)
        self.numBouncesField = self.addIntegerField(value=0, row=2, column=1)

        # Compute button
        self.addButton(text="Compute", row=3, column=1, command=self.computeDistance)

        # Output field
        self.addLabel(text="Total distance", row=4, column=0)
        self.outputField = self.addFloatField(value=0.0, row=4, column=1, precision=6)
        self.outputField.setState("readonly")

    def computeDistance(self):
        # Read user inputs
        height = self.heightField.getNumber()
        bIndex = self.bounceIndexField.getNumber()
        numBounces = self.numBouncesField.getNumber()

        # First fall
        total = height

        # Bounces
        for _ in range(numBounces):
            height = height * bIndex
            total += 2 * height

        # Display result
        self.outputField.setNumber(total)


def main():
    BouncyGUI().mainloop()


if __name__ == "__main__":
    main()
