import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QAbstractItemView
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from views.components.table import Table

class Body(QFrame):
    double_clicked_data_event = pyqtSignal(dict)
    one_clicked_data_event = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list__body")
        self.setObjectName("store__list__body")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.table_widget = Table(self)
        self.table_widget.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.handle_table_cell_doubleclick()
        self.handle_table_cell_click()

        main_layout.addWidget(self.table_widget)

    def handle_table_cell_doubleclick(self):
        table_widget = self.table_widget.table_widget
        table_widget.doubleClicked.connect(lambda e:\
            self.double_clicked_data_event.emit({
                "id" : table_widget.item(e.row(), 0).text()
            })
        )
    
    def handle_table_cell_click(self):
        table_widget = self.table_widget.table_widget
        table_widget.clicked.connect(lambda e:\
            self.one_clicked_data_event.emit({
                "id" : table_widget.item(e.row(), 0).text()
            })
        )