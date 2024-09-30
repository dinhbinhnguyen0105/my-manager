import os
from PyQt5.QtWidgets import QFrame, QVBoxLayout

from .home.home import Home
from .store.store import Store
from .robot.robot import Robot
from ..utils import handle_widget

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

class Pages(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_page_index = 0

        self.setProperty("class","pages")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.home = Home(self)
        self.store = Store(self)
        self.robot = Robot(self)

        main_layout.addWidget(self.home)
        main_layout.addWidget(self.store)
        main_layout.addWidget(self.robot)

        self.handel_set_page(2)
        with open(f"{MY_DIR}/page.styles.qss", "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)
    
    def handel_set_page(self, page_index):
        page_widgets = handle_widget.find_widgets_by_class(self, QFrame, "page")
        for index, page_widget in enumerate(page_widgets):
            if index == page_index: page_widget.show()
            else: page_widget.hide()
