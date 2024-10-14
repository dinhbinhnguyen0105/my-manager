import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget

class ContentOption(QFrame):
    current_option_event = pyqtSignal(QPushButton)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("content__options")
        self.setProperty("class", "content__options content")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.option_re_widget = QPushButton(self)
        self.option_re_widget.setObjectName("option_re")
        self.option_re_widget.setProperty("class", "options__option option")
        self.option_re_widget.setProperty("user-data", "real-estate")
        self.option_re_widget.setProperty("option-index", 0)
        self.option_re_widget.setText("Real estate")
        self.option_re_widget.clicked.connect(lambda : self.on_option_clicked(self.option_re_widget))
        
        self.option_fashion_widget = QPushButton(self)
        self.option_fashion_widget.setObjectName("option_fashion")
        self.option_fashion_widget.setProperty("class", "options__option option")
        self.option_fashion_widget.setProperty("user-data", "fashion")
        self.option_fashion_widget.setProperty("option-index", 1)
        self.option_fashion_widget.setText("Fashion")
        self.option_fashion_widget.clicked.connect(lambda : self.on_option_clicked(self.option_fashion_widget))

        self.option_food_widget = QPushButton(self)
        self.option_food_widget.setObjectName("option_food")
        self.option_food_widget.setProperty("class", "options__option option")
        self.option_food_widget.setProperty("user-data", "food")
        self.option_food_widget.setProperty("option-index", 2)
        self.option_food_widget.setText("Food")
        self.option_food_widget.clicked.connect(lambda : self.on_option_clicked(self.option_food_widget))

        self.option_travel_widget = QPushButton(self)
        self.option_travel_widget.setObjectName("option_travel")
        self.option_travel_widget.setProperty("class", "options__option option")
        self.option_travel_widget.setProperty("user-data", "travel")
        self.option_travel_widget.setProperty("option-index", 3)
        self.option_travel_widget.setText("Travel")
        self.option_travel_widget.clicked.connect(lambda : self.on_option_clicked(self.option_travel_widget))
        
        self.option_miscellaneous_widget = QPushButton(self)
        self.option_miscellaneous_widget.setObjectName("option_miscellaneous")
        self.option_miscellaneous_widget.setProperty("class", "options__option option")
        self.option_miscellaneous_widget.setProperty("user-data", "miscellaneous")
        self.option_miscellaneous_widget.setProperty("option-index", 4)
        self.option_miscellaneous_widget.setText("Miscellaneous")
        self.option_miscellaneous_widget.clicked.connect(lambda : self.on_option_clicked(self.option_miscellaneous_widget))

        main_layout.addWidget(self.option_re_widget)
        main_layout.addWidget(self.option_fashion_widget)
        main_layout.addWidget(self.option_food_widget)
        main_layout.addWidget(self.option_travel_widget)
        main_layout.addWidget(self.option_miscellaneous_widget)

        self.set_value()
    
    def set_value(self, option="real-estate"):
        option_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "options__option")
        for option_widget in option_widgets:
            if option_widget.property("user-data") == option:
                handle_widget.add_class(option_widget, "activated")
                self.current_option_event.emit(option_widget)
                return True
    
    def on_option_clicked(self, current_widget):
        activated_button_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            handle_widget.remove_class(activated_button_widgets[0], "activated")
        handle_widget.add_class(current_widget, "activated")
        self.current_option_event.emit(current_widget)
        self.setStyleSheet(self.styleSheet())
    
    def get_value(self):
        option_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "content__option")
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                return {
                    "option": option_widget.property("user-data")
                }
        raise lambda : ("option_widget invalid activated")

class MyCustomError(Exception):
    pass