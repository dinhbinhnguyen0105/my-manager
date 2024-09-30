import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget, QLabel

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

class Actions(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","robot__actions")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)
        label = QLabel("Actions", self)
        label.setAlignment(Qt.AlignCenter)
        label.setProperty("class", "robot__actions__title title")
        main_layout.addWidget(label)
        