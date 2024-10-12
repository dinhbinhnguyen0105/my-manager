import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget

class Buildingline(QFrame):
    current_buildingline_event = pyqtSignal(QPushButton)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__buildingline")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        buildingline_motorbike_widget = QPushButton(self)
        buildingline_motorbike_widget.setObjectName("buildingline_motorbike")
        buildingline_motorbike_widget.setProperty("class", "option activated")
        buildingline_motorbike_widget.setProperty("user-data", "motorbike")
        buildingline_motorbike_widget.setProperty("option-index", 0)
        buildingline_motorbike_widget.setText("Motorbike")
        buildingline_motorbike_widget.clicked.connect(lambda : self.handle_buildingline_clicked(buildingline_motorbike_widget))
        
        self.current_buildingline = buildingline_motorbike_widget

        buildingline_car_widget = QPushButton(self)
        buildingline_car_widget.setObjectName("buildingline_car")
        buildingline_car_widget.setProperty("class", "option")
        buildingline_car_widget.setProperty("user-data", "car")
        buildingline_car_widget.setProperty("option-index", 1)
        buildingline_car_widget.setText("Car")
        buildingline_car_widget.clicked.connect(lambda : self.handle_buildingline_clicked(buildingline_car_widget))
        

        main_layout.addWidget(buildingline_motorbike_widget)
        main_layout.addWidget(buildingline_car_widget)

    def showEvent(self, a0: QShowEvent | None) -> None:
        self.current_buildingline_event.emit(self.current_buildingline)
        return super().showEvent(a0)
    
    def handle_buildingline_clicked(self, current_widget):
        activated_button_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            handle_widget.remove_class(activated_button_widgets[0], "activated")
        handle_widget.add_class(current_widget, "activated")
        self.current_buildingline = current_widget
        self.current_buildingline_event.emit(self.current_buildingline)
        self.setStyleSheet(self.parent().styleSheet())

    def get_value(self):
        return { "building_line": self.current_buildingline.property("user-data") }