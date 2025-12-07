"""
File: studentview.py
Updated version with "Plot scores" button.
"""

from breezypythongui import EasyFrame
import matplotlib.pyplot as plt

class StudentView(EasyFrame):

    def __init__(self, model):
        EasyFrame.__init__(self)
        self.setSize(520, 230)
        self.model = model

        # Labels
        self.addLabel("Mean", row=0, column=0)
        self.addLabel("Median", row=1, column=0)
        self.addLabel("Mode", row=2, column=0)
        self.addLabel("Standard deviation", row=3, column=0)

        # Numeric fields
        self.meanFld   = self.addFloatField(0.0, row=0, column=1, precision=2)
        self.medianFld = self.addFloatField(0.0, row=1, column=1, precision=2)
        self.modeFld   = self.addFloatField(0.0, row=2, column=1, precision=1)
        self.stdFld    = self.addFloatField(0.0, row=3, column=1, precision=4)

        # Score list display
        self.addLabel("Data", row=0, column=2, sticky="NEW")
        self.scoreArea = self.addTextArea("", row=1, column=2, rowspan=3, width=12)

        # Button panel
        bp = self.addPanel(row=4, column=0, columnspan=3, background="black")

        bp.addButton("Edit score",       row=0, column=0, command=self.editScore)
        bp.addButton("Add score",        row=0, column=1, command=self.addScore)
        bp.addButton("Delete score",     row=0, column=2, command=self.deleteScore)
        bp.addButton("Randomize scores", row=0, column=3, command=self.randomizeScores)
        bp.addButton("Plot scores",      row=0, column=4, command=self.plotScores)

        self.refreshData()

    def refreshData(self):
        """Refreshes calculation + score list display."""
        self.setTitle(self.model.getName() + "'s Scores")
        self.meanFld.setNumber(self.model.getMean())
        self.medianFld.setNumber(self.model.getMedian())
        self.modeFld.setNumber(self.model.getMode())
        self.stdFld.setNumber(self.model.getStd())
        self.scoreArea.setText(str(self.model))

    # ------------------------------------------------------
    # EVENT HANDLERS
    # ------------------------------------------------------

    def editScore(self):
        pos = self.prompterBox("Edit Score", "Position to edit:")
        newScore = self.prompterBox("Edit Score", "New score:")
        if pos and newScore:
            self.model.editScore(int(pos), int(newScore))
            self.refreshData()

    def addScore(self):
        score = self.prompterBox("Add Score", "Enter new score:")
        if score:
            self.model.addScore(int(score))
            self.refreshData()

    def deleteScore(self):
        pos = self.prompterBox("Delete score", "Position of the score:")
        if pos:
            self.model.deleteScore(int(pos))
            self.refreshData()

    def randomizeScores(self):
        count = self.prompterBox("Randomize", "How many scores?")
        low   = self.prompterBox("Randomize", "Lowest possible score?")
        high  = self.prompterBox("Randomize", "Highest possible score?")
        if count and low and high:
            self.model.randomizeScores(int(count), int(low), int(high))
            self.refreshData()

    # ------------------------------------------------------
    # NEW METHOD: PLOT SCORES
    # ------------------------------------------------------
    def plotScores(self):
        """Displays a line plot of the student’s scores."""
        scores = self.model._scores
        if not scores:
            self.messageBox("Error", "No scores to plot.")
            return

        positions = list(range(1, len(scores) + 1))

        plt.figure(figsize=(7, 4))
        plt.plot(positions, scores, marker='o', linestyle='-', color='blue')
        plt.title(f"{self.model.getName()}'s Test Scores")
        plt.xlabel("Position")
        plt.ylabel("Score")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
