import os, sys, datetime, random
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QScrollArea, QPlainTextEdit, QSizePolicy, QPushButton
from .images import Images
from .type import Type
from .location import Location
from .category import Category
from .buildingline import Buildingline
from .detail import Detail

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget
from views.components.plaintext import Plaintext
from views.components.lineedit import LineEdit
from views.components.combobox import Combobox

class CreateItemRe(QFrame):
    current_option_event = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_option = None

        self.setProperty("class", "content real-estate")
        self.setProperty("user-data", "real-estate")
        self.setProperty("option-index", 0)
        self.setObjectName("real-estate")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.images_widget = Images(self)
        self.images_widget.resize(400, 200)

        self.scroll_area = QScrollArea(self)

        self.scroll_widget = QFrame(self)
        self.scroll_area.setWidgetResizable(True)
        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(0,0,0,0)
        scroll_layout.setSpacing(0)
        scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_widget.setLayout(scroll_layout)
        self.scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.location_widget = Location(self)
        self.location_widget.provide_widget.setDisabled(True)
        self.location_widget.district_widget.setDisabled(True)
        self.type_widget = Type(self)
        self.type_widget.current_type_event.connect(self.handle_set_id)
        self.type_widget.current_type_event.connect(self.handle_set_category_options)
        self.type_widget.current_type_event.connect(self.handle_set_detail_deps_type)
        self.id_widget = QLabel(self)
        self.id_widget.setAlignment(Qt.AlignCenter)
        self.id_widget.setProperty("class", "content__id")
        self.category_widget = Category(self)
        self.category_widget.current_category_event.connect(self.handle_set_detail_deps_category)
        self.buildingline_widget = Buildingline(self)
        self.detail_widget = Detail(self)
        self.description_widget = Plaintext({
            "class": "content__description",
            "label": "Description: "
        }, self)

        main_layout.addWidget(self.images_widget) 
        scroll_layout.addWidget(self.id_widget)
        scroll_layout.addWidget(self.location_widget)
        scroll_layout.addWidget(self.type_widget)
        scroll_layout.addWidget(self.category_widget)
        scroll_layout.addWidget(self.buildingline_widget)
        scroll_layout.addWidget(self.detail_widget)
        scroll_layout.addWidget(self.description_widget)
        self.scroll_area.setWidget(self.scroll_widget)
        
        main_layout.addWidget(self.scroll_area)
    
    def get_value(self):
        values = {
            **self.images_widget.get_value(),
            **{ "id" : self.id_widget.text(), },
            **self.location_widget.get_value(),
            **self.type_widget.get_value(), 
            **self.category_widget.get_value(), 
            **self.buildingline_widget.get_value(), 
            **self.detail_widget.get_value(), 
            **{ "description" : self.description_widget.get_value(), },
        }
        if "images" in values.keys() and values["images"] == []: values["images"] = False
        if "street" in values.keys() and not values["street"]: values["street"] = False
        if "construction" in values.keys() and not values["construction"]: values["construction"] = False
        if "function" in values.keys() and not values["function"]: values["function"] = False
        if "furniture" in values.keys() and not values["furniture"]: values["furniture"] = False
        return values

    def handle_set_id(self, current_type_widget):
        current_type = current_type_widget.property("user-data")[0].upper()
        now = datetime.datetime.now()
        randint = random.randint(0, 100)
        self.product_id = f"RE.{current_type}.{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
        self.id_widget.setText(self.product_id)
    
    def handle_set_category_options(self, current_type_widget):
        self.category_widget.set_categories(current_type_widget.property("user-data"))
    def handle_set_detail_deps_type(self, current_type):
        if current_type.property("user-data") == "sell":
            for content_detail_widget in handle_widget.find_widgets_by_class(self.detail_widget, QFrame, "content__detail"):
                content_detail_widget.setDisabled(False)
        elif current_type.property("user-data") == "rent":
            for content_detail_widget in handle_widget.find_widgets_by_class(self.detail_widget, QFrame, "content__detail"):
                content_detail_widget.setDisabled(False)
            self.detail_widget.area_widget.lineedit_widget.setText("0")
            self.detail_widget.area_widget.setDisabled(True)
            self.detail_widget.legal_widget.setDisabled(True)
        elif current_type.property("user-data") == "assignment":
            for content_detail_widget in handle_widget.find_widgets_by_class(self.detail_widget, QFrame, "content__detail"):
                content_detail_widget.setDisabled(False)
            self.detail_widget.area_widget.lineedit_widget.setText("0")
            self.detail_widget.area_widget.setDisabled(True)
            self.detail_widget.legal_widget.setDisabled(True)

    def handle_set_detail_deps_category(self, current_category): 
        print("current_category: ", current_category)