import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from .images import Images
from views.utils import handle_widget

class Type(QFrame):
    current_type_event = pyqtSignal(QPushButton)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__type")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        type_sell_widget = QPushButton(self)
        type_sell_widget.setObjectName("type_sell")
        type_sell_widget.setProperty("class", "option activated")
        type_sell_widget.setProperty("user-data", "sell")
        type_sell_widget.setProperty("option-index", 0)
        type_sell_widget.setText("Sell")
        type_sell_widget.clicked.connect(lambda : self.handle_type_clicked(type_sell_widget))

        self.current_type = type_sell_widget
        
        type_rent_widget = QPushButton(self)
        type_rent_widget.setObjectName("type_rent")
        type_rent_widget.setProperty("class", "option")
        type_rent_widget.setProperty("user-data", "rent")
        type_rent_widget.setProperty("option-index", 0)
        type_rent_widget.setText("Rent")
        type_rent_widget.clicked.connect(lambda : self.handle_type_clicked(type_rent_widget))
        
        type_assignment_widget = QPushButton(self)
        type_assignment_widget.setObjectName("type_assignment")
        type_assignment_widget.setProperty("class", "option")
        type_assignment_widget.setProperty("user-data", "assignment")
        type_assignment_widget.setProperty("option-index", 0)
        type_assignment_widget.setText("Assignment")
        type_assignment_widget.clicked.connect(lambda : self.handle_type_clicked(type_assignment_widget))

        main_layout.addWidget(type_sell_widget)
        main_layout.addWidget(type_rent_widget)
        main_layout.addWidget(type_assignment_widget)

    def showEvent(self, a0: QShowEvent | None) -> None:
        self.current_type_event.emit(self.current_type)
        return super().showEvent(a0)
    
    def handle_type_clicked(self, current_widget):
        activated_button_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            handle_widget.remove_class(activated_button_widgets[0], "activated")
        handle_widget.add_class(current_widget, "activated")
        self.current_type = current_widget
        self.current_type_event.emit(self.current_type)

        self.setStyleSheet(self.parent().styleSheet())

    def get_value(self):
        return self.current_type