import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.utils.custom_error import CustomError

class DetailRealEstate(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("content__detail-real-estate")
        self.setProperty("class", "content__detail-real-estate")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
