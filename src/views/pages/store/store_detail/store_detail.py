import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QLabel
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from views.components.lineedit import LineEdit
from views.components.plaintext import Plaintext
from logic.db.local.products import info_write

class StoreDetail(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__detail")
        self.setObjectName("store__list")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.header_widget = QLabel("Detail", self)
        self.header_widget.setProperty("class", "store__detail__header")
        self.header_widget.setAlignment(Qt.AlignCenter)

        self.title_widget = LineEdit({
            "class": "store__detail__title",
            "label": "Title: ",
            "id": "store__detail__title"
        })
        self.title_widget.lineedit_widget.setDisabled(True)

        self.description_widget = Plaintext({
            "class": "store__detail__description",
            "id": "store__detail__description",
            "label": "Description: "
        })
        self.description_widget.plaintext_widget.setDisabled(True)

        main_layout.addWidget(self.header_widget)
        main_layout.addWidget(self.title_widget)
        main_layout.addWidget(self.description_widget)
    
    def set_details(self, payload):
        self.title_widget.lineedit_widget.setText(payload["title"])
        self.description_widget.plaintext_widget.setPlainText(payload["description"])