import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QGridLayout
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget
from views.components.combobox import Combobox
from views.components.lineedit import LineEdit

class Detail(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__detail")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.area_widget = LineEdit({
            "class": "content__detail__area",
            "label": "Area: ",
        }, self)
        self.construction_widget = LineEdit({
            "class": "content__detail__construction",
            "label": "Construction: ",
        }, self)
        self.function_widget = LineEdit({
            "class": "content__detail__function",
            "label": "Function: ",
        }, self)
        self.furniture_widget = Combobox({
            "class": "content__location__furniture",
            "label": "Furniture: ",
            "options": [
                ("None", "none"),
                ("Basic", "basic"),
                ("Full", "full"),
            ]
        }, self)
        self.legal_widget = Combobox({
            "class": "content__location__legal",
            "label": "Legal: ",
            "options": [
                ("Không sổ", "none"),
                ("Sổ nông nghiệp chung", "snnc"),
                ("Sổ nông nghiệp phân quyền", "snnpq"),
                ("Sổ nông nghiệp riêng", "srnn"),
                ("Sổ xây dựng chung", "sxdc"),
                ("Sổ xây dựng phân quyền", "sxdpq"),
                ("Sổ xây dựng riêng", "srxd"),
            ]
        }, self)
        self.price_widget = LineEdit({
            "class": "content__detail__price",
            "label": "Price: ",
        }, self)

        main_layout.addWidget(self.area_widget, 0, 0, 1, 1)
        main_layout.addWidget(self.construction_widget, 0, 1, 1, 1)
        main_layout.addWidget(self.function_widget, 1, 0, 1, 1)
        main_layout.addWidget(self.furniture_widget, 1, 1, 1, 1)
        main_layout.addWidget(self.legal_widget, 2, 0, 1, 1)
        main_layout.addWidget(self.price_widget, 2, 1, 1, 1)