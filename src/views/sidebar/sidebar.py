from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QStackedWidget,
    QPushButton,
    QSizePolicy
)
from PyQt5.QtCore import Qt

class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "sidebar")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.store_btn_widget = QPushButton("Store", self)
        self.store_btn_widget.setProperty("class", "button btn-store")
        self.robot_btn_widget = QPushButton("Robot", self)
        self.robot_btn_widget.setProperty("class", "button btn-robot")
        self.robot_btn_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Đặt chính sách kích thước

        self.robot_btn_widget.clicked.connect(lambda : print("Clicked"))
        main_layout.setAlignment(Qt.AlignTop)

        main_layout.addWidget(self.store_btn_widget)
        main_layout.addWidget(self.robot_btn_widget)