from breezypythongui import EasyFrame
from tkinter import messagebox

class ATMView(EasyFrame):
    def __init__(self, model):
        EasyFrame.__init__(self, title="ATM")
        self.model = model
        self.failures = 0  # Başarısız giriş sayacı

        # GUI bileşenleri
        self.addLabel("Name", row=0, column=0)
        self.nameField = self.addTextField("", row=0, column=1)

        self.addLabel("PIN", row=1, column=0)
        self.pinField = self.addTextField("", row=1, column=1)

        self.statusLabel = self.addLabel("Status", row=2, column=0, columnspan=2)

        # Login butonu
        self.loginButton = self.addButton(text="Login", row=3, column=0, columnspan=2, command=self.login)

    def login(self):
        name = self.nameField.getText()
        pin = self.pinField.getText()

        if self.model.checkLogin(name, pin):
            self.statusLabel["text"] = "Login successful!"
            self.failures = 0  # Başarılı girişte sayaç sıfırlanır
        else:
            self.failures += 1
            self.statusLabel["text"] = f"Login failed ({self.failures} of 3)"
            if self.failures >= 3:
                messagebox.showwarning("Alert", "Three successive login failures! The police will be called.")
                self.loginButton["state"] = "disabled"  # Butonu devre dışı bırak
