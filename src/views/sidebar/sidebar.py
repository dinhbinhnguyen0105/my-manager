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

from ..utils import selector

class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "sidebar")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.current_btn_index = 0
        self.home_btn_widget = QPushButton(self)
        self.home_btn_widget.setProperty("class", "button activated btn-store")
        self.home_btn_widget.setObjectName("btn-store")
        self.home_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "home.svg")))
        self.home_btn_widget.setIconSize(QSize(26, 26))

        self.store_btn_widget = QPushButton(self)
        self.store_btn_widget.setProperty("class", "button btn-store")
        self.store_btn_widget.setObjectName("btn-store")
        self.store_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "store.svg")))
        self.store_btn_widget.setIconSize(QSize(26, 26))

        self.robot_btn_widget = QPushButton(self)
        self.robot_btn_widget.setProperty("class", "button btn-robot")
        self.store_btn_widget.setObjectName("btn-robot")
        self.robot_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "robot.svg")))
        self.robot_btn_widget.setIconSize(QSize(26, 26))

        self.store_btn_widget.clicked.connect(lambda : self.handle_click(self.home_btn_widget))
        self.store_btn_widget.clicked.connect(lambda : self.handle_click(self.store_btn_widget))
        self.robot_btn_widget.clicked.connect(lambda : self.handle_click(self.robot_btn_widget))

        main_layout.addWidget(self.home_btn_widget)
        main_layout.addWidget(self.store_btn_widget)
        main_layout.addWidget(self.robot_btn_widget)


        with open(f"{MY_DIR}/sidebar.styles.qss", "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)
    
    def handle_click(self, current_btn_widget):
        button_widgets = selector.find_widgets_by_class(self, QPushButton, "button")
        activated_button_widget = selector.find_widgets_by_class(self, QPushButton, "activated")[0]
        selector.remove_class(activated_button_widget, "activated")
        
        for index, button_widget in enumerate(button_widgets):
            if button_widget != current_btn_widget: selector.remove_class(button_widget, "activated")
            else:
                selector.add_class(button_widget, "activated")
                self.current_btn_index = index

        self.setStyleSheet(self.my_styles)

