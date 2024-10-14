import os, sys
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))

class ContentActions(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("content__actions")
        self.setProperty("class", "content__actions content")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.save_btn_widget = QPushButton("Save", self)
        self.save_btn_widget.setProperty("class", "content__action content__action__save")

        main_layout.addWidget(self.save_btn_widget)

