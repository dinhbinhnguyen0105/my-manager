from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QPlainTextEdit

class Plaintext(QFrame):
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
        self.plaintext_widget = QPlainTextEdit(self)
        self.plaintext_widget.setProperty("class", "plaintext")
        # self.plaintext_widget.showEvent = self.handle_plaintext_show
        # self.plaintext_widget.textChanged.connect(self.handle_text_changed)
    
        main_layout.addWidget(label_widget)
        main_layout.addWidget(self.plaintext_widget)
    
    # def handle_plaintext_show(self, e):
    #     if self.plaintext_widget.toPlainText() == "":
    #         self.plaintext_widget.textCursor().insertText("'\n+ ")

    # def handle_text_changed(self):
    #     current_text = self.plaintext_widget.toPlainText()
    #     if current_text and current_text[-1] == "\n":
    #         self.plaintext_widget.textCursor().insertText("+ ")
    
    def get_value(self):
        current_text = self.plaintext_widget.toPlainText().lower()
        return current_text