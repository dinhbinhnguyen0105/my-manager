from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QLineEdit

class LineEdit(QFrame):
    current_text_event = pyqtSignal(str)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): _class = payload["class"]
        else: _class = None
        if "label" in payload.keys(): label = payload["label"]
        else: label = False
        if "place_holder" in payload.keys(): place_holder = payload["place_holder"]
        else: place_holder = False
        if "id" in payload.keys(): id = payload["id"]
        else: id = False
        if "user-data" in payload.keys(): user_data = payload["user-data"]
        else: user_data = False
        
        self.setProperty("class", _class)
        if id: self.setObjectName(id)
        if user_data: self.setProperty("user-data", payload["user-data"])
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        if label:
            self.label_widget = QLabel(label, self)
            self.label_widget.setProperty("class", "label")
            main_layout.addWidget(self.label_widget)
            main_layout.addWidget(self.label_widget)
        self.lineedit_widget = QLineEdit(self)
        self.lineedit_widget.setProperty("class", "lineedit")
        if place_holder:
            self.lineedit_widget.setPlaceholderText(place_holder)
        self.lineedit_widget.textChanged.connect(self.handle_lineedit_changed)
    
        main_layout.addWidget(self.lineedit_widget)

    def handle_lineedit_changed(self, e):
        # for Hint
        pass
    
    def get_value(self):
        current_text = self.lineedit_widget.text()
        return current_text