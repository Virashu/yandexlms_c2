from random import randint
import sys

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication

from ui import UI


class MyWidget(UI):
    def __init__(self):
        super().__init__()
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.update()

    def draw_circle(self, qp):
        qp.setPen(
            QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255), 255), 8)
        )
        qp.setBrush(QColor(0, 0, 0, 0))
        x, y, d = randint(0, 300), randint(0, 300), randint(10, 30)
        qp.drawEllipse(x, y, d, d)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
