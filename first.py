import sys
import random

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem, QGraphicsScene


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ul.ui', self)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)

        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QBrush(Qt.GlobalColor.yellow))
        self.scene.addItem(ellipse)

    def paintEvent(self, event):
        super().paintEvent(event)
        self.graphicsView.viewport().update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()  # меняем название класса
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())