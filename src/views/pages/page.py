from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget, QLabel

class Page(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","page")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        label = QLabel("Pages")
        main_layout.addWidget(label)