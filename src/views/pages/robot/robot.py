import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget, QWidget, QLabel

from .content.content import Content
from .actions.actions import Actions
from .settings.settings import Settings

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

class Robot(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","page robot")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        # main_layout.setAlignment(Qt.AlignRight)
        self.setLayout(main_layout)
        
        self.content = Content(self)
        self.actions = Actions(self)
        self.settings = Settings(self)

        main_layout.addWidget(self.content)
        main_layout.addWidget(self.actions)
        main_layout.addWidget(self.settings)
        
        with open(os.path.join(MY_DIR, "robot.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)
    
    # def resizeEvent(self, event):
    #     self.content.resize(int(self.width() * 0.7), self.height())
    #     self.actions.resize(int(self.width() * 0.15), self.height())
    #     self.settings.resize(int(self.width() * 0.15), self.height())