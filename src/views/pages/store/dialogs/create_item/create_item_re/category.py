import os, sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.components.combobox import Combobox

class Category(QFrame):
    current_category_event = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__category")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        self.category_widget = Combobox({
            # "class": "",
            "label": "Category: ",
            "options": []
        }, self)
        self.category_widget.current_option_event.connect(lambda e: self.current_category_event.emit(e))
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

    def get_value(self):
        return {
            "category": self.category_widget.get_value()
        }