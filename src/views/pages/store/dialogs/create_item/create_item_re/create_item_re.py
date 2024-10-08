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
        self.id_widget = QLabel(self)
        self.id_widget.setAlignment(Qt.AlignCenter)
        self.id_widget.setProperty("class", "content__id")
        self.category_widget = Category(self)
        self.buildingline_widget = Buildingline(self)
        self.detail_widget = Detail(self)
        self.description_widget = QPlainTextEdit(self)
        self.description_widget.setProperty("class", "content__description")
        self.savebutton_widget = QPushButton("Save", self)
        self.savebutton_widget.setProperty("class", "content__save-btn")
        self.savebutton_widget.clicked.connect(self.handle_clicked)

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
        main_layout.addWidget(self.savebutton_widget)
    
    def handle_clicked(self):
        self.detail_widget.get_value()
    
    def get_value(self):

        pass

    def handle_set_id(self, current_type_widget):
        current_type = current_type_widget.property("user-data")[0].upper()
        now = datetime.datetime.now()
        randint = random.randint(0, 100)
        self.product_id = f"RE.{current_type}.{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
        self.id_widget.setText(self.product_id)
    
    def handle_set_category_options(self, current_type_widget):
        self.category_widget.set_categories(current_type_widget.property("user-data"))
