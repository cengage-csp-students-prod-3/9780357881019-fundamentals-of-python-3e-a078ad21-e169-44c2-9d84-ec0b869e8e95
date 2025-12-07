"""
File: hoopstatsview.py
The view for analyzing basketball stats with line plot support.
"""

from breezypythongui import EasyFrame
import matplotlib.pyplot as plt

class HoopStatsView(EasyFrame):
    
    def __init__(self, frame):
        """Creates the window and lays out components."""
        EasyFrame.__init__(self, title="Hoop Stats")
        self.frame = frame
        
        # Variable for radio buttons
        self.radioVar = self.addStringVar(value="PTS")  # Default column
        
        # Panel for radio buttons
        self.columnPanel = self.addPanel(row=0, column=0, columnspan=3)
        
        # Add a radio button for each column
        columns = list(frame.columns)
        for col in columns:
            self.columnPanel.addRadiobutton(text=col, value=col, variable=self.radioVar)
        
        # Button to analyze and plot selected column
        self.plotButton = self.addButton(text="Analyze & Plot",
                                         row=1, column=0,
                                         columnspan=3,
                                         command=self.analyzeAndPlot)
        
        # Text area to show summary data
        self.dataArea = self.addTextArea(text="Select a column and click 'Analyze & Plot'",
                                        row=2, column=0,
                                        columnspan=3,
                                        width=50, height=15)
    
    def analyzeAndPlot(self):
        """Analyze the selected column and show a line plot."""
        col = self.radioVar.get()
        data = self.frame[col].dropna()  # NaN değerleri çıkar
        
        # Calculate summary statistics
        mean_val = data.mean()
        median_val = data.median()
        mode_val = data.mode()[0] if not data.mode().empty else "N/A"
        std_val = data.std()
        
        # Display summary in text area
        summary = (f"Column: {col}\n"
                   f"Mean: {mean_val:.2f}\n"
                   f"Median: {median_val:.2f}\n"
                   f"Mode: {mode_val}\n"
                   f"Standard Deviation: {std_val:.2f}\n")
        self.dataArea.setText(summary)
        
        # Plot line graph
        plt.figure(figsize=(8,4))
        plt.plot(data.values, marker='o', linestyle='-')
        plt.title(f"Line Plot of {col}")
        plt.xlabel("Index")
        plt.ylabel(col)
        plt.grid(True)
        plt.show()
