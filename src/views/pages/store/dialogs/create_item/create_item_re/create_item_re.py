import os, sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QDialog, QLabel, QScrollArea, QVBoxLayout, QSizePolicy, QWidget, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget
from views.components import dropbox, imagebox

class CreateItemRe(QFrame):
    current_option_event = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "create-item re")
        self.setObjectName("re")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        main_layout.addWidget(QLabel("RE"))
