import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QComboBox, QLabel
# MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
# MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
# sys.path.append(MAIN_DIR)

class Combobox(QFrame):
    current_option_event = pyqtSignal(str)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): self._class = payload["class"]
        else: self._class = None
        if "label" in payload.keys(): self._label = payload["label"]
        else: self._label = "undefined"
        if "options" in payload.keys(): self._options = payload["options"]
        else: self._options = []

        self.setProperty("class", self._class)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        label_widget = QLabel(self._label, self)
        label_widget.setProperty("class", "label")
        self.combobox_widget = QComboBox(self)
        self.combobox_widget.setProperty("class", "combobox")
        for _option in self._options:
            self.combobox_widget.addItem(_option[0], _option[1])
        self.combobox_widget.currentIndexChanged.connect(self.handle_index_changed)
        
        main_layout.addWidget(label_widget)
        main_layout.addWidget(self.combobox_widget)
    
    def handle_index_changed(self):
        current_data_user = self.combobox_widget.currentData()
        self.current_option_event.emit(current_data_user)
    
    def remove_items(self):
        while self.combobox_widget.count() > 0:
            self.combobox_widget.removeItem(0)
    
    def showEvent(self, a0: QShowEvent | None) -> None:
        self.handle_index_changed()
        return super().showEvent(a0)
    
    def get_value(self):
        return self.combobox_widget.currentData()
    