import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from .search_base import SearchBase
from .search_ext import SearchExt

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local import products

class Search(QFrame):
    current_option_widget_event = pyqtSignal(QPushButton)
    filter_payload_event = pyqtSignal(dict)
    def __init__(self, option, parent=None):
        super().__init__(parent)
        self.option = option
        self.filter_payload = {}

        self.setProperty("class", "list__header__search")
        self.setObjectName("list__header__search")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.search_base_widget = SearchBase(self)
        self.search_base_widget.ext_button_event.connect(self.handle_show_search_ext)
        self.search_base_widget.base_filter_event.connect(self.handle_ext_payload)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)

        main_layout.addWidget(self.search_base_widget)
        main_layout.addWidget(h_line)
    
    def handle_show_search_ext(self, ext_status):
        if ext_status:
            self.search_ext_widget = SearchExt(self)
            self.search_ext_widget.set_filter_widgets(self.option)
            self.search_ext_widget.ext_filter_event.connect(self.handle_ext_payload)
            self.layout().addWidget(self.search_ext_widget)
        else:
            if hasattr(self, "search_ext_widget"):
                self.search_ext_widget.setParent(None)
                self.search_ext_widget.deleteLater()
    
    def handle_ext_payload(self, payload):
        self.filter_payload = { **self.filter_payload, **payload }
        self.filter_payload_event.emit(self.filter_payload)