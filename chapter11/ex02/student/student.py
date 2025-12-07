"""
File: studentview.py
The view for editing and analyzing student scores.
"""

from breezypythongui import EasyFrame

class StudentView(EasyFrame):

    def __init__(self, model):
        EasyFrame.__init__(self)
        self.setSize(500, 200)
        self.model = model

        # Labels
        self.addLabel("Mean", row=0, column=0)
        self.addLabel("Median", row=1, column=0)
        self.addLabel("Mode", row=2, column=0)
        self.addLabel("Standard deviation", row=3, column=0)

        # Number fields
        self.meanFld   = self.addFloatField(0.0, row=0, column=1, precision=2)
        self.medianFld = self.addFloatField(0.0, row=1, column=1, precision=2)
        self.modeFld   = self.addFloatField(0.0, row=2, column=1, precision=1)
        self.stdFld    = self.addFloatField(0.0, row=3, column=1, precision=4)

        # Text area
        self.addLabel("Data", row=0, column=2, sticky="NEW")
        self.scoreArea = self.addTextArea("", row=1, column=2, width=12, rowspan=3)

        # Buttons
        bp = self.addPanel(row=4, column=0, columnspan=3, background="black")
        bp.addButton("Edit score", row=0, column=0, command=self.editScore)
        bp.addButton("Add score", row=0, column=1, command=self.addScore)
        bp.addButton("Delete score", row=0, column=2, command=self.deleteScore)
        bp.addButton("Randomize scores", row=0, column=3, command=self.randomizeScores)

        self.refreshData()

    def refreshData(self):
        self.setTitle(self.model.getName() + "'s Scores")
        self.meanFld.setNumber(self.model.getMean())
        self.medianFld.setNumber(self.model.getMedian())
        self.modeFld.setNumber(self.model.getMode())
        self.stdFld.setNumber(self.model.getStd())
        self.scoreArea.setText(str(self.model))

    # -----------------------------------
    # COMPLETED EVENT HANDLER METHODS
    # -----------------------------------

    def editScore(self):
        """Gets a position & new score from the user and updates the model."""
        position = self.prompterBox("Edit Score", "Position to edit:")
        newScore = self.prompterBox("Edit Score", "New score:")
        if position is not None and newScore is not None:
            self.model.editScore(int(position), int(newScore))
            self.refreshData()

    def addScore(self):
        """Gets a score from user, adds it, updates the view."""
        score = self.prompterBox("Add Score", "Enter new score:")
        if score is not None:
            self.model.addScore(int(score))
            self.refreshData()

    def randomizeScores(self):
        """Gets count, low, high from user and randomizes model scores."""
        count = self.prompterBox("Randomize", "How many scores?")
        low   = self.prompterBox("Randomize", "Lowest possible score?")
        high  = self.prompterBox("Randomize", "Highest possible score?")
        if count and low and high:
            self.model.randomizeScores(int(count), int(low), int(high))
            self.refreshData()

    def deleteScore(self):
        position = self.prompterBox("Delete score",
                                    "Position of the score:")
        if position is not None:
            self.model.deleteScore(int(position))
            self.refreshData()
