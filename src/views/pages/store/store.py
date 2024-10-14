import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QHBoxLayout, QStackedWidget, QWidget, QLabel

from .store_list.store_list import StoreList
from .store_detail.store_detail import StoreDetail

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(SRC_DIR)
from logic.utils.product_handle import ProductHandle
from logic.utils.temp_handle import TemplateHandle


class Store(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class","page store")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        
        self.store_list = StoreList(self)
        self.store_list.body.double_clicked_data_event.connect(self.handle_show_detail_dialog)
        self.store_list.body.one_clicked_data_event.connect(self.handle_set_detail)
        self.store_detail = StoreDetail(self)

        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        v_line.setFrameShadow(QFrame.Sunken)

        main_layout.addWidget(self.store_list)
        main_layout.addWidget(v_line)
        main_layout.addWidget(self.store_detail)

        self.setLayout(main_layout)
        with open(os.path.join(MY_DIR, "store.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)
    
    def handle_show_detail_dialog(self, id):
        print(id)
    
    def handle_set_detail(self, id):
        product_info = ProductHandle.get_product_buy_id({ "option": self.store_list.option, **id})
        product = TemplateHandle.render_content({ "action": "default", "product_info": product_info})
        if "images" not in product_info.keys(): imgs_of_product_path = []
        else: imgs_of_product_path = ProductHandle.get_images_buy_path(product_info["images"])
        if "status" not in product_info.keys(): status = "available"
        else: status = product_info["status"]
        self.store_detail.set_details({
            **product,
            **{ "images" : imgs_of_product_path},
            **{ "status" : status}
        })