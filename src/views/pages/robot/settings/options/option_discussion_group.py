from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
)

class OptionDiscussionGroup(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","robot__setting__option robot__setting__discussion-group")
        self.setObjectName("robot__setting__discussion-group")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        label = QLabel("OptionDiscussionGroup")
        main_layout.addWidget(label)