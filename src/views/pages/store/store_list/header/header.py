import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

from .options.options import Options
from .search.search import Search

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local.products import info_write

class Header(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list__header")
        self.setObjectName("store__list__header")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.options_widget = Options(self)
        self.options_widget.current_option_widget_event.connect(self.set_search_ext_content)
        
        main_layout.addWidget(self.options_widget)

    def set_search_ext_content(self, option_widget):
        option = option_widget.property("user-data")
        if hasattr(self, "search_widget"):
            self.search_widget.setParent(None)
            self.search_widget.deleteLater()
        self.search_widget = Search(option, self)
        self.layout().addWidget(self.search_widget)
