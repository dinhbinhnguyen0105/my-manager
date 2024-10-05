import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget

class CreateItem_Options(QFrame):
    current_option_event = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("dialog__create-item__options")
        self.setProperty("class", "dialog__create-item__options")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.current_option = "option_re"

        option_re_widget = QPushButton(self)
        option_re_widget.setObjectName("option_re")
        option_re_widget.setProperty("class", "option activated")
        option_re_widget.setText("Real estate")
        option_re_widget.clicked.connect(lambda : self.handle_option_clicked(option_re_widget))
        option_fashion_widget = QPushButton(self)
        option_fashion_widget.setObjectName("option_fashion")
        option_fashion_widget.setProperty("class", "option")
        option_fashion_widget.setText("Fashion")
        option_fashion_widget.clicked.connect(lambda : self.handle_option_clicked(option_fashion_widget))
        option_food_widget = QPushButton(self)
        option_food_widget.setObjectName("option_food")
        option_food_widget.setProperty("class", "option")
        option_food_widget.setText("Food")
        option_food_widget.clicked.connect(lambda : self.handle_option_clicked(option_food_widget))
        option_travel_widget = QPushButton(self)
        option_travel_widget.setObjectName("option_travel")
        option_travel_widget.setProperty("class", "option")
        option_travel_widget.setText("Travel")
        option_travel_widget.clicked.connect(lambda : self.handle_option_clicked(option_travel_widget))
        option_miscellaneous_widget = QPushButton(self)
        option_miscellaneous_widget.setObjectName("option_miscellaneous")
        option_miscellaneous_widget.setProperty("class", "option")
        option_miscellaneous_widget.setText("Miscellaneous")
        option_miscellaneous_widget.clicked.connect(lambda : self.handle_option_clicked(option_miscellaneous_widget))

        main_layout.addWidget(option_re_widget)
        main_layout.addWidget(option_fashion_widget)
        main_layout.addWidget(option_food_widget)
        main_layout.addWidget(option_travel_widget)
        main_layout.addWidget(option_miscellaneous_widget)
    
    def showEvent(self, a0: QShowEvent | None) -> None:
        self.current_option_event.emit(self.current_option)
        return super().showEvent(a0)
    
    def handle_option_clicked(self, current_widget):
        activated_button_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            handle_widget.remove_class(activated_button_widgets[0], "activated")
        handle_widget.add_class(current_widget, "activated")
        self.current_option = current_widget.objectName()
        self.current_option_event.emit(self.current_option)
        self.setStyleSheet(self.parent().styleSheet())