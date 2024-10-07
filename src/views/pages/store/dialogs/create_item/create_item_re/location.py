import os, sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QGridLayout, QVBoxLayout, QPushButton, QComboBox, QLabel, QLineEdit
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from .images import Images
from views.utils import handle_widget

PROVIDE_OPTIONS = [("Lâm Đồng", "lamdong")]
DISTRICT_OPTIONS = [("Đà Lạt", "dalat"), ("Đức Trọng", "ductrong")]
WARD_OPTIONS = [
    ("Ward 1", "ward_1"),
    ("Ward 2", "ward_2"),
    ("Ward 3", "ward_3"),
    ("Ward 4", "ward_4"),
    ("Ward 5", "ward_5"),
    ("Ward 6", "ward_6"),
    ("Ward 7", "ward_7"),
    ("Ward 8", "ward_8"),
    ("Ward 9", "ward_9"),
    ("Ward 10", "ward_10"),
    ("Ward 11", "ward_11"),
    ("Ward 12", "ward_12"),
    ("Ward Tà Nung", "ward_tanung"),
    ("Ward Trạm Hành", "ward_tramhanh"),
    ("Ward Xuân Trường", "ward_xuantruong"),
    ("Ward Xuân Thọ", "ward_xuantho"),
]

class Location(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__location")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.provide_widget = Combobox({
            "class": "content__location__provide",
            "label": "Provide: ",
            "options": [("Lâm Đồng", "lamdong")]
        }, self)
        self.provide_widget.current_option_event.connect(self.handle_provide_selected)
        self.district_widget = Combobox({
            "class": "content__location__district",
            "label": "District: ",
        }, self)
        self.district_widget.current_option_event.connect(self.handle_district_selected)
        self.ward_widget = Combobox({
            "class": "content__location__ward",
            "label": "Ward: ",
        }, self)

        self.street_widget = LineEdit({
            "class": "content__location__street",
            "label": "Street: "
        }, self)

        main_layout.addWidget(self.provide_widget, 0, 0, 1, 1)
        main_layout.addWidget(self.district_widget, 0, 1, 1, 3)
        main_layout.addWidget(self.ward_widget, 1, 0, 1, 1)
        main_layout.addWidget(self.street_widget, 1, 1, 1, 3)

    def handle_provide_selected(self, provide):
        if provide == "lamdong":
            self.district_widget.remove_items()
            for district_option in DISTRICT_OPTIONS :
                self.district_widget.combobox_widget.addItem(district_option[0], district_option[1])
        elif provide == "hochiminh":
            self.district_widget.remove_items()
      
    def handle_district_selected(self, district):
        if district == "dalat":
            self.ward_widget.remove_items()
            for ward_option in WARD_OPTIONS:
                self.ward_widget.combobox_widget.addItem(ward_option[0], ward_option[1])
        elif district == "ductrong":
            self.ward_widget.remove_items()

class LineEdit(QFrame):
    current_text_event = pyqtSignal(str)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): self._class = payload["class"]
        else: self._class = None
        if "label" in payload.keys(): self._label = payload["label"]
        else: self._label = "undefined"
        
        self.setProperty("class", self._class)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        label_widget = QLabel(self._label, self)
        label_widget.setProperty("class", "label")
        self.lineedit_widget = QLineEdit(self)
        self.lineedit_widget.setProperty("class", "lineedit")
        self.lineedit_widget.textChanged.connect(self.handle_lineedit_changed)
    
        main_layout.addWidget(label_widget)
        main_layout.addWidget(self.lineedit_widget)

    def handle_lineedit_changed(self, e):
        # for Hint
        pass
    
    def get_value(self):
        current_text = self.lineedit_widget.text().lower()
        return current_text

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
    