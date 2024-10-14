import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from .images import Images
from .header.header import Header
from .footer.footer import Footer
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))

sys.path.append(SRC_DIR)

from views.utils import handle_widget
from views.components.lineedit import LineEdit
from views.components.plaintext import Plaintext

class StoreDetail(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__detail")
        self.setObjectName("store__detail")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.setFixedWidth(300)

        self.header_widget = Header(self)
        self.header_widget.edit_btn_widget.setDisabled(True)
        self.header_widget.status_btn_widget.setDisabled(True)
        self.header_widget.delete_btn_widget.setDisabled(True)

        self.image_widget = Images({
            "class": "store__detail__images",
            "id": "store__detail__images"
        }, self)
        self.image_widget.setFixedSize(300, 200)

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

        self.footer_widget = Footer(self)
        self.footer_widget.default_btn_widget.setDisabled(True)
        self.footer_widget.random_btn_widget.setDisabled(True)

        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        h_line_1 = QFrame()
        h_line_1.setFrameShape(QFrame.HLine)
        h_line_1.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(self.header_widget)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.image_widget)
        main_layout.addWidget(self.title_widget)
        main_layout.addWidget(self.description_widget)
        main_layout.addWidget(h_line_1)
        main_layout.addWidget(self.footer_widget)

    
    def set_details(self, payload):
        self.title_widget.lineedit_widget.setText(payload["title"])
        self.description_widget.plaintext_widget.setPlainText(payload["description"])
        self.image_widget.handle_set_imgs(payload["images"])
        self.title_widget.lineedit_widget.setDisabled(False)
        self.description_widget.plaintext_widget.setDisabled(False)
        self.footer_widget.default_btn_widget.setDisabled(False)
        self.footer_widget.random_btn_widget.setDisabled(False)
        self.header_widget.edit_btn_widget.setDisabled(False)
        self.header_widget.status_btn_widget.setDisabled(False)
        if payload["status"] == "available":
            block_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "block.svg")))
            self.header_widget.status_btn_widget.setProperty("class", "detail__header__btn detail__header__block-btn")
            self.header_widget.status_btn_widget.setProperty("user-data", "block")
            self.header_widget.status_btn_widget.setIcon(block_icon)
        elif payload["status"] == "unavailable":
            self.header_widget.status_btn_widget.setProperty("class", "detail__header__btn detail__header__check-btn")
            check_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "check.svg")))
            self.header_widget.status_btn_widget.setIcon(check_icon)
        self.setStyleSheet(self.styleSheet())

        self.header_widget.delete_btn_widget.setDisabled(False)