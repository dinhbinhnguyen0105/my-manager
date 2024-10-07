import os, sys, datetime, random
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout
from .images import Images
from .type import Type
from .location import Location

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
        self.location_widget = Location(self)
        self.type_widget = Type(self)
        self.type_widget.current_type_event.connect(self.handle_set_id)
        self.id_widget = QLabel(self)
        self.id_widget.setAlignment(Qt.AlignCenter)
        self.id_widget.setProperty("class", "content__id")
        main_layout.addWidget(self.images_widget)
        main_layout.addWidget(self.location_widget)
        main_layout.addWidget(self.type_widget)
        main_layout.addWidget(self.id_widget)
        main_layout.addWidget(QLabel("RE"))
        

    def handle_set_id(self, current_type_widget):
        current_type = current_type_widget.property("user-data")[0].upper()
        now = datetime.datetime.now()
        randint = random.randint(0, 100)
        self.product_id = f"RE.{current_type}.{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
        self.id_widget.setText(self.product_id)

# option_type_date