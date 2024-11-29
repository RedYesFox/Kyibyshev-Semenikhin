import sys
import random

from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem, QGraphicsScene
from Ul_ui import Ui_MainWindow as UiMainWindow


class MyWidget(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QBrush(QColor(red, green, blue)))
        self.scene.addItem(ellipse)

    def paintEvent(self, event):
        super().paintEvent(event)
        self.graphicsView.viewport().update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())