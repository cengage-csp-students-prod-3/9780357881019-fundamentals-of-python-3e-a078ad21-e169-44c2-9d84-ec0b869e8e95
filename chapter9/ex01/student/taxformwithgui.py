# Write your code here
"""
File: taxformwithgui.py
GUI-based tax calculator.
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")
        
        # Input fields
        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value=0, row=1, column=1)

        # Compute button
        self.addButton(text="Compute", row=2, column=0, columnspan=2, command=self.computeTax)

        # Output field
        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value=0.0, row=3, column=1, state="readonly")

    def computeTax(self):
        """
        Computes the total tax.
        Tax formula used in the book:
        TAX = (grossIncome - dependents * 3000) * 0.20
        """
        income = self.incomeField.getNumber()
        dependents = self.depField.getNumber()
        
        taxableIncome = income - dependents * 3000
        tax = taxableIncome * 0.20
        
        if tax < 0:
            tax = 0.0
        
        self.taxField.setNumber(tax)

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()
