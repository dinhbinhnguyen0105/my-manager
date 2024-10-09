import os, sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame, QStackedWidget, QPushButton
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))

from create_item_options import CreateItem_Options
from create_item_re.create_item_re import CreateItemRe
from create_item_fashion.create_item_fashion import CreateItemFashion
from create_item_food.create_item_food import CreateItemFood
from create_item_travel.create_item_travel import CreateItemTravel
from create_item_miscellaneous.create_item_miscellaneous import CreateItemMiscellaneous
sys.path.append(MAIN_DIR)
from views.utils import handle_widget
from logic.db.local.products import info_write

class CreateItem(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog create-item")
        self.setObjectName("create-item")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.options_widget = CreateItem_Options(self)
        self.options_widget.current_option_event.connect(self.handle_set_option_page)
        
        self.re_page_widget = CreateItemRe(self)
        self.fashion_page_widget = CreateItemFashion(self)
        self.food_page_widget = CreateItemFood(self)
        self.travel_page_widget = CreateItemTravel(self)
        self.miscellaneous_page_widget = CreateItemMiscellaneous(self)

        self.savebutton_widget = QPushButton("Save", self)
        self.savebutton_widget.setProperty("class", "content__save-btn")
        self.savebutton_widget.clicked.connect(self.handle_clicked)
        
        self.create_container_widget = QStackedWidget(self)
        self.create_container_widget.setProperty("class", "create-item__container")
        self.create_container_widget.addWidget(self.re_page_widget)
        self.create_container_widget.addWidget(self.fashion_page_widget)
        self.create_container_widget.addWidget(self.food_page_widget)
        self.create_container_widget.addWidget(self.travel_page_widget)
        self.create_container_widget.addWidget(self.miscellaneous_page_widget)

        main_layout.addWidget(self.options_widget)
        main_layout.addWidget(self.create_container_widget)
        main_layout.addWidget(self.savebutton_widget)

        with open(os.path.join(MY_DIR, "create_item.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)

    def handle_set_option_page(self, current_button_widget):
        current_option_index = current_button_widget.property("option-index")
        options_page_widgets = handle_widget.find_widgets_by_class(self, QFrame, "content")
        for options_page_widget in options_page_widgets:
            option_index = options_page_widget.property("option-index")
            if option_index == current_option_index: self.create_container_widget.setCurrentIndex(option_index)
    
    def handle_clicked(self):
        current_option = self.options_widget.get_value()
        if current_option["option"] == "real-estate":
            _ = {**current_option, **self.re_page_widget.get_value()}
            write_result = info_write(_)
            return write_result
        elif current_option["option"] == "fashion": pass
        elif current_option["option"] == "food": pass
        elif current_option["option"] == "travel": pass
        elif current_option["option"] == "miscellaneous":
            _ = { **current_option, **self.miscellaneous_page_widget.get_value()}
            write_result = info_write(_)
            print(write_result)
            return write_result
        self.close()

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])

    window = CreateItem()
    window.show()

    sys.exit(app.exec_())