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

class SearchExt(QFrame):
    ext_button_event = pyqtSignal(bool)
    ext_filter_event = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "list__header__search_ext")
        self.setObjectName("list__header__search_ext")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.ext_filter = {}
    
    def set_filter_widgets(self, option):
        filters = []
        if option == "real-estate":
            filters = [
                { "class": "header__search-input", "place_holder": "Type ...", "id": "header__input-type", "user-data": "type"},
                { "class": "header__search-input", "place_holder": "Category ...", "id": "header__input-category", "user-data": "category"},
                { "class": "header__search-input", "place_holder": "Ward ...", "id": "header__input-ward", "user-data": "ward"},
                { "class": "header__search-input", "place_holder": "Street ...", "id": "header__input-street", "user-data": "street"},
                { "class": "header__search-input", "place_holder": "Area ...", "id": "header__input-area", "user-data": "area"},
                { "class": "header__search-input", "place_holder": "Price ...", "id": "header__input-price", "user-data": "price"},
                { "class": "header__search-input", "place_holder": "Legal ...", "id": "header__input-legal", "user-data": "legal"},
                { "class": "header__search-input", "place_holder": "Building line ...", "id": "header__input-building-line", "user-data": "building-line"},
                { "class": "header__search-input", "place_holder": "Furniture ...", "id": "header__input-furniture", "user-data": "furniture"},
            ]
            

        elif option == "miscellaneous":
            filters = [
                { "class": "header__search-input", "place_holder": "Title ...", "id": "header__input-title", "user-data": "title"},
                { "class": "header__search-input", "place_holder": "Description ...", "id": "header__input-description", "user-data": "description"},
                { "class": "header__search-input", "place_holder": "Tags ...", "id": "header__input-tags", "user-data": "tags"},
            ]
        for filter_payload in filters:
            self.set_filter_widget(filter_payload)
    
    def set_filter_widget(self, payload):
        filter_widget = LineEdit(payload, self)
        filter_widget.lineedit_widget.textChanged.connect(lambda e: self.handle_filter_change({
            filter_widget.property("user-data") : e
        }))
        self.layout().addWidget(filter_widget)


    def handle_filter_change(self, payload):
        self.ext_filter = { **self.ext_filter, **payload }
        self.ext_filter_event.emit(self.ext_filter)