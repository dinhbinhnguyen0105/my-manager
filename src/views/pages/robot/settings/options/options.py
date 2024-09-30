from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
)

from .option_system import OptionSytem
from .option_sell_maketplace import OptionSellMarketplace
from .option_sell_group import OptionSellGroup
from .option_discussion_group import OptionDiscussionGroup
from .option_takecare import OptionTakecare

class Options(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","robot__setting__options")
        self.setObjectName("robot__setting__options")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.option_system_widget = OptionSytem(self)
        self.option_sell_marketplace_widget = OptionSellMarketplace(self)
        self.option_sell_group = OptionSellGroup(self)
        self.option_discussion_group = OptionDiscussionGroup(self)
        self.option_takecare_group = OptionTakecare(self)

        self.option_sell_marketplace_widget.hide()
        self.option_sell_group.hide()
        self.option_discussion_group.hide()
        self.option_takecare_group.hide()


        main_layout.addWidget(self.option_system_widget)
        main_layout.addWidget(self.option_sell_marketplace_widget)
        main_layout.addWidget(self.option_sell_group)
        main_layout.addWidget(self.option_discussion_group)
        main_layout.addWidget(self.option_takecare_group)
        
