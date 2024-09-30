from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
)

class OptionSellMarketplace(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","robot__setting__option robot__setting__sell-marketplace")
        self.setObjectName("robot__setting__sell-marketplace")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        label = QLabel("OptionSellMarketplace")
        main_layout.addWidget(label)