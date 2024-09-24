from PyQt5.QtWidgets import  QMainWindow
from PyQt5.QtCore import QSize
from .views.views import View

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("My manager")
        self.resize(QSize(1200, 600))
        self.main_widget = View(self)
        self.setCentralWidget(self.main_widget)
    