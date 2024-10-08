from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QLineEdit

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

        self.label_widget = QLabel(self._label, self)
        self.label_widget.setProperty("class", "label")
        self.lineedit_widget = QLineEdit(self)
        self.lineedit_widget.setProperty("class", "lineedit")
        self.lineedit_widget.textChanged.connect(self.handle_lineedit_changed)
    
        main_layout.addWidget(self.label_widget)
        main_layout.addWidget(self.lineedit_widget)

    def handle_lineedit_changed(self, e):
        # for Hint
        pass
    
    def get_value(self):
        current_text = self.lineedit_widget.text()
        return current_text