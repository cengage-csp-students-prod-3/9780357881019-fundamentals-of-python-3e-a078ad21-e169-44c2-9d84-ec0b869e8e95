"""
File: hoopstatsview.py
The view for analyzing basketball stats with full radio button support.
"""

from breezypythongui import EasyFrame

class HoopStatsView(EasyFrame):
    
    def __init__(self, frame):
        """Creates the window and lays out components."""
        EasyFrame.__init__(self, title="Hoop Stats")
        self.frame = frame
        
        # Variable for radio buttons
        self.radioVar = self.addStringVar(value="PTS")  # Default column
        
        # Panel for radio buttons
        self.columnPanel = self.addPanel(row=0, column=0, columnspan=3)
        
        # List of all columns (after cleaning)
        columns = list(frame.columns)
        
        # Add a radio button for each column
        for idx, col in enumerate(columns):
            self.columnPanel.addRadiobutton(text=col, value=col, variable=self.radioVar)
        
        # Add plot button
        self.plotButton = self.addButton(text="Plot selected column",
                                         row=1, column=0,
                                         columnspan=3,
                                         command=self.plotColumn)
        
        # Text area for showing data (optional)
        self.dataArea = self.addTextArea(text=str(frame.head()),
                                        row=2, column=0,
                                        columnspan=3,
                                        width=50, height=15)
    
    # Example function triggered by plot button
    def plotColumn(self):
        col = self.radioVar.get()
        print(f"Plotting column: {col}")
        # Burada matplotlib ile plot edebilirsin:
        # self.frame[col].plot()
        # plt.show()
