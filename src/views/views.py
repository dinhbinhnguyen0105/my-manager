import os
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QStackedWidget
from PyQt5.QtCore import QFile, QIODevice, QTextStream, Qt

from .pages.page import Page
from .sidebar.sidebar import Sidebar

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

class View(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("view")

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        # self.page = Page(self)
        self.sidebar = Sidebar(self)
        main_layout.addWidget(self.sidebar)
        main_layout.setAlignment(Qt.AlignLeft)
        # main_layout.addWidget(self.page)

        with open(f"{MY_DIR}/views.styles.qss", "r") as f:
            styles = f.read()
        self.setStyleSheet(styles)