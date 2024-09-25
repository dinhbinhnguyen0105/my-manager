import os, sys
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir))
ICONS_DIR = os.path.abspath(os.path.join(MAIN_DIR, "assets", "icons"))

from ..logics import selector

class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "sidebar")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.store_btn_widget = QPushButton(self)
        self.store_btn_widget.setProperty("class", "button btn-store")
        self.store_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "home.svg")))
        self.store_btn_widget.setIconSize(QSize(26, 26))

        self.robot_btn_widget = QPushButton(self)
        self.robot_btn_widget.setProperty("class", "button btn-robot")
        self.robot_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "robot.svg")))
        self.robot_btn_widget.setIconSize(QSize(26, 26))

        self.robot_btn_widget.clicked.connect(lambda : print("Clicked"))



        # buttons = selector.find_widgets_by_class(self, QPushButton, "button")
        # print(buttons)

        main_layout.addWidget(self.store_btn_widget)
        main_layout.addWidget(self.robot_btn_widget)

        with open(f"{MY_DIR}/sidebar.styles.qss", "r") as f:
            styles = f.read()
        self.setStyleSheet(styles)
    
    def handle_click(self):
        pass

