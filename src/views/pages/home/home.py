import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget, QLabel

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

class Home(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","page home")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        
        label = QLabel("Home")
        main_layout.addWidget(label)

        
        with open(os.path.join(MY_DIR, "home.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)