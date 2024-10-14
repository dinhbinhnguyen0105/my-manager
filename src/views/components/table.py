
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange, QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor

# MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
# SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir))
# sys.path.append(SRC_DIR)
# from views.utils import handle_widget
# from logic.db.local import products

class Table(QFrame):
    target_cell_data_event = pyqtSignal(dict)
    target_row_data_event = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "table")
        self.setObjectName("table")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.target_column = None
        self.prev_cell = None

        self.table_widget = QTableWidget(self)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.table_widget.cellClicked.connect(self.on_cell_clicked)
        main_layout.addWidget(self.table_widget)

    def match_filters(self, data, filters):
        for f in filters:
            for key, value in f.items():
                if value == "": continue
                if value not in str(data.get(key)):
                    return False
        return True

    def render_table(self, payload):
        _filters = []
        _data = []
        if "filter" in payload.keys():
            if payload["filter"] != [] or payload["filter"]:
                _filters = payload["filter"]
        if "data" in payload.keys():
            if payload["data"] != [] or payload["data"]:
                _data = payload["data"]
        self.data = [item for item in _data if self.match_filters(item, _filters)]
        self.table_widget.setRowCount(len(self.data))
        if not self.data: return False
        if self.data[0]["option"] == "real-estate":
            self.table_widget.setColumnCount(10)
            header_dict = {
                "id": "ID",
                "type": "Type",
                "category": "Category",
                "ward": "Ward",
                "street": "Street",
                "area": "Area",
                "price": "Price",
                "legal": "Legal",
                "building_line": "Building line",
                "furniture": "Furniture",
            }
            self.table_widget.setHorizontalHeaderLabels(header_dict.values())
            for i, key in enumerate(header_dict.keys()):
                _header = self.table_widget.horizontalHeaderItem(i)
                _header.setData(Qt.UserRole, { "value": header_dict[key]})
            for row, product in enumerate(self.data):
                if "status" in product.keys() and product["status"] == "unavailable":
                    _status = False
                else: _status = True
                if "is_uploaded" in product.keys() and product["is_uploaded"] == True:
                    pass
                for col, header in enumerate(header_dict.keys()):
                    if header in product.keys():
                        value = str(product[header])
                        if header == "id" or\
                            header == "type" or\
                            header == "legal" or\
                            header == "building_line" or\
                            header == "furniture": value = value.upper()
                        else:
                            value = value.title()
                        item = QTableWidgetItem(value)
                        if not _status: item.setBackground(QColor(253, 116, 29))
                        self.table_widget.setItem(row, col, item)
        elif self.data[0]["option"] == "miscellaneous":
            self.table_widget.setColumnCount(3)
            header_dict = {
                "id": "ID",
                "title": "Title",
                "description": "Description",
            }
            self.table_widget.setHorizontalHeaderLabels(header_dict.values())
            for i, key in enumerate(header_dict.keys()):
                _header = self.table_widget.horizontalHeaderItem(i)
                _header.setData(Qt.UserRole, { "value": header_dict[key]})
            for row, product in enumerate(self.data):
                for col, header in enumerate(header_dict.keys()):
                    if header in product.keys():
                        value = str(product[header])
                        if header == "id": value = value.upper()
                        item = QTableWidgetItem(value)
                        self.table_widget.setItem(row, col, item)
