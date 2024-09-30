import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
)
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))

class OptionSytem(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","robot__setting__option robot__setting__system")
        self.setObjectName("robot__setting__system")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        delay_error_label = QLabel("Delay when error", self)
        delay_error_label.setProperty("class", "label")
        delay_error_input = QLineEdit(self)
        delay_error_input.setProperty("class", "input")
        delay_error_input.setObjectName("setting__error_input")
        delay_new_cycle_label = QLabel("Delay start new cycle", self)
        delay_new_cycle_label.setProperty("class", "label")
        delay_new_cycle_input = QLineEdit(self)
        delay_new_cycle_input.setProperty("class", "input")
        delay_new_cycle_input.setObjectName("setting__new_cycle_input")
        delay_switch_account_label = QLabel("Delay switch account", self)
        delay_switch_account_label.setProperty("class", "label")
        delay_switch_account_input = QLineEdit(self)
        delay_switch_account_input.setProperty("class", "input")
        delay_switch_account_input.setObjectName("setting__switch_account_input")
        shutdown_label = QLabel("Shutdown when finish (Type shutdown)", self)
        shutdown_label.setProperty("class", "label")
        shutdown_input = QLineEdit(self)
        shutdown_input.setProperty("class", "input")
        shutdown_input.setObjectName("setting__shutdown")


        
        main_layout.addWidget(delay_error_label)
        main_layout.addWidget(delay_error_input)
        main_layout.addWidget(delay_new_cycle_label)
        main_layout.addWidget(delay_new_cycle_input)
        main_layout.addWidget(delay_switch_account_label)
        main_layout.addWidget(delay_switch_account_input)
        main_layout.addWidget(shutdown_label)
        main_layout.addWidget(shutdown_input)

        with open(os.path.join(os.path.join(MY_DIR, os.path.pardir, os.path.pardir), "robot.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)
