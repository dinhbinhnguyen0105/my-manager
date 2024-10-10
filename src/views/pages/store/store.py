import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QHBoxLayout, QStackedWidget, QWidget, QLabel

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

from .store_list.store_list import StoreList
from .store_detail.store_detail import StoreDetail

class Store(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","page store")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        
        self.store_list = StoreList(self)
        self.store_detail = StoreDetail(self)

        main_layout.addWidget(self.store_list)
        main_layout.addWidget(self.store_detail)

        self.setLayout(main_layout)
        with open(os.path.join(MY_DIR, "store.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)