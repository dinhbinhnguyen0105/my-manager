import os, sys, datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame, QStackedWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local.products import info_write

class Item(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "item-dialog")
        self.setObjectName("item-dialog")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
        