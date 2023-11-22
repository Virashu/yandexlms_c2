from PyQt5.QtWidgets import QMainWindow, QPushButton


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 300)
        self.btn = QPushButton("Draw", self)
        self.btn.setGeometry(10, 10, 75, 25)
