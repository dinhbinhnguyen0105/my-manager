import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal

from .header.header import Header
from .body.body import Body

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local import products

class StoreList(QFrame):
    re_render_table_event = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list")
        self.setObjectName("store__list")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
        self.option = None
        self.header = Header(self)
        self.header.options_widget.current_option_widget_event.connect(lambda option_widget: self.handle_option_changed(option_widget.property("user-data")))
        self.header.search_widget.search_base_widget.refresh_btn_clicked_event.connect(lambda : self.handle_re_render_table(self.option))
        self.body = Body(self)

        main_layout.addWidget(self.header)
        main_layout.addWidget(self.body)
    

    def handle_option_changed(self, option_widget):
        self.option = option_widget
        data_from_file = products.info_read()[self.option]
        self.data = []
        if self.option == "real-estate":
            for _data in data_from_file.values():
                for product in _data:
                    self.data.append(product)
        elif self.option == "miscellaneous":
            for key, value in data_from_file.items():
                self.data.append({
                    "id": key,
                    **value
                })
        self.body.table_widget.render_table({
            "data": self.data,
            "filter": [],
        })
        self.header.search_widget.filter_payload_event.connect( lambda payload: self.handle_filter(self.data, payload))
    
    def handle_re_render_table(self, option_widget):
        self.handle_option_changed(option_widget)
        self.re_render_table_event.emit()

    def handle_filter(self, data, filters):
        list_of_filter = []
        for key in filters.keys():
            list_of_filter.append({
                key: filters[key].lower()
            })
        self.body.table_widget.render_table({
            "data": data,
            "filter": list_of_filter,
        })

        #ERROR