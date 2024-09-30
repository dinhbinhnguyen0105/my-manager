import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
)
from .select import Select
from .options.options import Options
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
UTILS_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, os.path.pardir, "utils"))

sys.path.insert(0, UTILS_DIR)
# from .handle_widget import find_widgets_by_class
import handle_widget

class Settings(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","robot__setting")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        label = QLabel("Settings")
        label.setAlignment(Qt.AlignCenter)
        label.setProperty("class", "robot__setting__title title")
        
        self.select_widget = Select(self)
        self.option_widget = Options(self)

        self.select_widget.setCurrentIndex(0)
        self.option_widget.option_system_widget.show()

        self.select_widget.activated.connect(self.handle_set_current_setting)

        main_layout.addWidget(label)
        main_layout.addWidget(self.select_widget)
        main_layout.addWidget(self.option_widget)
    
    def handle_set_current_setting(self, index):
        current_setting = self.select_widget.itemData(index)
        option_widgets = handle_widget.find_widgets_by_class(self, QFrame, "robot__setting__option")
        for option_widget in option_widgets:
            if option_widget.property("class") != "robot__setting__options":
                if current_setting in option_widget.property("class"):
                    _ = option_widget
                    option_widget.show()
                else:
                    option_widget.hide()
                