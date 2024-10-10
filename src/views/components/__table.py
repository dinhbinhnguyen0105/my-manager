import os, sys
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local import products

class Table(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "table")
        self.setObjectName("table")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        data = [['Apple', 'Red', 10],
                ['Banana', 'Yellow', 5],
                ['Orange', 'Orange', 8]]
        
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(len(data))
        self.table_widget.setHorizontalHeaderLabels(['Fruit', 'Color', 'Quantity'])
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.table_widget.setItem(i, j, item)
        
        main_layout.addWidget(self.table_widget)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec_())