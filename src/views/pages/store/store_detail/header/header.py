import os
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))

class Header(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__detail__header")
        self.setObjectName("store__detail__header")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.add_btn_widget = QPushButton(self)
        self.add_btn_widget.setObjectName("detail__header__add-btn")
        self.add_btn_widget.setProperty("class", "detail__header__btn detail__header__add-btn")
        self.add_btn_widget.setProperty("user-data", "add")
        add_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "add.svg")))
        self.add_btn_widget.setIcon(add_icon)
        self.add_btn_widget.clicked.connect(self.on_add_btn_clicked)
        
        self.edit_btn_widget = QPushButton(self)
        self.edit_btn_widget.setObjectName("detail__header__edit-btn")
        self.edit_btn_widget.setProperty("class", "detail__header__btn detail__header__edit-btn")
        self.edit_btn_widget.setProperty("user-data", "edi")
        edit_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "edit.svg")))
        self.edit_btn_widget.setIcon(edit_icon)
        self.edit_btn_widget.clicked.connect(self.on_edit_icon_clicked)
        
        self.status_btn_widget = QPushButton(self)
        self.status_btn_widget.setObjectName("detail__header__status-btn")
        self.status_btn_widget.setProperty("class", "detail__header__btn detail__header__status-btn")
        self.status_btn_widget.setProperty("user-data", "block")
        block_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "block.svg")))
        self.status_btn_widget.setIcon(block_icon)
        self.status_btn_widget.clicked.connect(self.on_status_btn_clicked)
        
        self.delete_btn_widget = QPushButton(self)
        self.delete_btn_widget.setObjectName("detail__header__delete-btn")
        self.delete_btn_widget.setProperty("class", "detail__header__btn detail__header__delete-btn")
        self.delete_btn_widget.setProperty("user-data", "delete")
        delete_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "remove.svg")))
        self.delete_btn_widget.setIcon(delete_icon)
        self.delete_btn_widget.clicked.connect(self.on_delete_btn_clicked)

        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        v_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(self.add_btn_widget)
        main_layout.addItem(QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addWidget(self.edit_btn_widget)
        main_layout.addWidget(self.status_btn_widget)
        main_layout.addWidget(v_line)
        main_layout.addWidget(self.delete_btn_widget)        
    
    def on_add_btn_clicked(self): pass
    def on_edit_icon_clicked(self): pass
    def on_delete_btn_clicked(self): pass
    def on_status_btn_clicked(self): pass