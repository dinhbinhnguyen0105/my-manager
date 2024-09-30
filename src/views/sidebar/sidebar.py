import os
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
)
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIcon

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir))
ICONS_DIR = os.path.abspath(os.path.join(MAIN_DIR, "assets", "icons"))

from ..utils import handle_widget

class Sidebar(QFrame):
    current_page_index = pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "sidebar")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.home_btn_widget = QPushButton(self)
        self.home_btn_widget.setProperty("class", "button btn-home")
        self.home_btn_widget.setObjectName("btn-home")
        self.home_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "home.svg")))
        self.home_btn_widget.setIconSize(QSize(26, 26))

        self.store_btn_widget = QPushButton(self)
        self.store_btn_widget.setProperty("class", "button btn-store")
        self.store_btn_widget.setObjectName("btn-store")
        self.store_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "store.svg")))
        self.store_btn_widget.setIconSize(QSize(26, 26))

        self.robot_btn_widget = QPushButton(self)
        self.robot_btn_widget.setProperty("class", "button btn-robot activated")
        self.store_btn_widget.setObjectName("btn-robot")
        self.robot_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "robot.svg")))
        self.robot_btn_widget.setIconSize(QSize(26, 26))

        self.home_btn_widget.clicked.connect(lambda : self.handle_click(self.home_btn_widget))
        self.store_btn_widget.clicked.connect(lambda : self.handle_click(self.store_btn_widget))
        self.robot_btn_widget.clicked.connect(lambda : self.handle_click(self.robot_btn_widget))

        main_layout.addWidget(self.home_btn_widget)
        main_layout.addWidget(self.store_btn_widget)
        main_layout.addWidget(self.robot_btn_widget)


        with open(f"{MY_DIR}/sidebar.styles.qss", "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)
    
    def handle_click(self, current_btn_widget):
        button_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "button")
        activated_button_widget = handle_widget.find_widgets_by_class(self, QPushButton, "activated")[0]
        handle_widget.remove_class(activated_button_widget, "activated")
        
        for index, button_widget in enumerate(button_widgets):
            if button_widget != current_btn_widget: handle_widget.remove_class(button_widget, "activated")
            else:
                handle_widget.add_class(button_widget, "activated")
                self.current_page_index.emit(index)

        self.setStyleSheet(self.my_styles)

