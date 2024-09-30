from PyQt5.QtWidgets import (
    QComboBox,
)

class Select(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "robot__setting__select")
        self.setObjectName("robot__setting__select")

        self.addItem("System", "robot__setting__system")
        self.addItem("List in marketplace", "robot__setting__sell-marketplace")
        self.addItem("List in group", "robot__setting__sell-group")
        self.addItem("Discussion in group", "robot__setting__discussion-group")
        self.addItem("Take care", "robot__setting__takecare")
    