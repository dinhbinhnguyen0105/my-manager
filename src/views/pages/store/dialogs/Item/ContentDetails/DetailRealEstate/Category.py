import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.utils.custom_error import CustomError
from views.components.combobox import Combobox

class Category(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("real-estate__category")
        self.setProperty("class", "real-estate__category content")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.category_widget = Combobox({
            "label": "Category: ",
            "options": []
        })
        main_layout.addWidget(self.category_widget)

    def set_categories(self, product_type):
        self.category_widget.remove_items()
        if product_type == "sell":
            categories = [
                ("House", "category_house"),
                ("Shophouse", "category_shophouse"),
                ("Villa", "category_villa"),
                ("Apartment", "category_apartment"),
                ("Homestay", "category_homestay"),
                ("Hotel", "category_hotel"),
                ("Land", "category_land"),
            ]
        elif product_type == "rent":
            categories = [
                ("House", "category_house"),
                ("Shophouse", "category_shophouse"),
                ("Villa", "category_villa"),
                ("Apartment", "category_apartment"),
                ("Homestay", "category_homestay"),
                ("Hotel", "category_hotel"),
                ("Land", "category_land"),
                ("Retail space", "category_retailspace"),
                ("Workshop", "category_workshop"),
                ("Coffee house", "category_coffeehouse"),
            ]
        elif product_type == "assignment":
            categories = [
                ("Homestay", "category_homestay"),
                ("Hotel", "category_hotel"),
                ("Retail space", "category_retailspace"),
                ("Workshop", "category_workshop"),
                ("Coffee house", "category_coffeehouse"),
            ]
        else: categories = []
        for category in categories:
            self.category_widget.combobox_widget.addItem(category[0], category[1])

    def set_value(self, value):

        pass

    def get_value(self):
        return {
            "category": self.category_widget.get_value()
        }