import os, sys
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.utils.custom_error import CustomError

class BuildingLine(QFrame):
    def __init__(self, parent=None):
        current_buildingline_event = pyqtSignal(QPushButton)
        super().__init__(parent)
        self.setObjectName("real-estate__building-line")
        self.setProperty("class", "real-estate__building-line content")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.motorbike_widget = QPushButton(self)
        self.motorbike_widget.setObjectName("buildingline_motorbike")
        self.motorbike_widget.setProperty("class", "building-line__option option")
        self.motorbike_widget.setProperty("user-data", "motorbike")
        self.motorbike_widget.setProperty("building-line__index", 0)
        self.motorbike_widget.setText("Motorbike")
        self.motorbike_widget.clicked.connect(lambda : self.on_buildingline_clicked(self.motorbike_widget))

        self.car_widget = QPushButton(self)
        self.car_widget.setObjectName("buildingline_car")
        self.car_widget.setProperty("class", "building-line__option option")
        self.car_widget.setProperty("user-data", "car")
        self.car_widget.setProperty("building-line__index", 1)
        self.car_widget.setText("Car")
        self.car_widget.clicked.connect(lambda : self.on_buildingline_clicked(self.car_widget))
        
        main_layout.addWidget(self.motorbike_widget)
        main_layout.addWidget(self.car_widget)
    
    def on_buildingline_clicked(self, current_widget):
        activated_button_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            handle_widget.remove_class(activated_button_widgets[0], "activated")
        handle_widget.add_class(current_widget, "activated")
        self.current_buildingline_event.emit(current_widget)
        self.setStyleSheet(self.styleSheet())
    
    def set_value(self, building_line="motorbike"):
        buildingline_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "content__building_line")
        for buildingline_widget in buildingline_widgets:
            if buildingline_widget.property("user-data") == building_line:
                handle_widget.add_class(buildingline_widget, "activated")
                self.current_buildingline_event.emit(buildingline_widget)
                return True
        
        raise CustomError("invalid building_line")
