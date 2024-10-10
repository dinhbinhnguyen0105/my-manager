import os, sys
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local import products
from views.components.lineedit import LineEdit

class SearchBase(QFrame):
    ext_button_event = pyqtSignal(bool)
    base_filter_event = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "list__header__search_base")
        self.setObjectName("list__header__search_base")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.id_filter_widget = LineEdit({
            "class": "header__search-input",
            "place_holder": "ID ...",
            "id": "header__input-id",
            "user-data": "id",
        }, self)
        self.id_filter_widget.lineedit_widget.textChanged.connect(\
            lambda e: self.base_filter_event.emit({ "id": e }))

        self.current_ext_status = False
        self.ext_button_widget = QPushButton(self)
        self.ext_button_widget.setProperty("class", "header__search-ext-button")
        self.ext_button_widget.setObjectName("header__search-ext-button")
        self.ext_button_widget.clicked.connect(self.handle_ext_button_pressed)

        main_layout.addWidget(self.id_filter_widget)
        main_layout.addWidget(self.ext_button_widget)
    
    def showEvent(self, e):
        self.ext_button_event.emit(self.current_ext_status)
        icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "arrow-down.svg")))
        self.ext_button_widget.setIcon(icon)

    def handle_ext_button_pressed(self):
        self.current_ext_status = not self.current_ext_status
        if not self.current_ext_status:
            icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "arrow-down.svg")))
        else:
            icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "arrow-up.svg")))
        self.ext_button_widget.setIcon(icon)
        self.ext_button_event.emit(self.current_ext_status)

    # def handle_filter_change(self, payload)