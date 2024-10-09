import os, sys, datetime, random
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout
from .images import Images

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget
from views.components.lineedit import LineEdit
from views.components.plaintext import Plaintext

class CreateItemMiscellaneous(QFrame):
    current_option_event = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content miscellaneous")
        self.setProperty("user-data", "miscellaneous")
        self.setProperty("option-index", 4)
        self.setObjectName("miscellaneous")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        self.images_widget = Images(self)
        self.images_widget.resize(400, 200)

        self.id_widget = QLabel(self)
        self.handle_re_set_id()
        self.id_widget.setAlignment(Qt.AlignCenter)
        self.id_widget.setProperty("class", "content__id miscellaneous__id")

        self.title_widget = LineEdit({
            "class": "miscellaneous__title",
            "label": "Title: ",
        }, self)
        self.description_widget = Plaintext({
            "class": "miscellaneous__description",
            "label": "Description: "
        }, self)

        main_layout.addWidget(self.images_widget) 
        main_layout.addWidget(self.id_widget)
        main_layout.addWidget(self.title_widget)
        main_layout.addWidget(self.description_widget)
    
    def showEvent(self, e):
        self.handle_re_set_id()
    
    def get_value(self):
        if not self.title_widget.get_value(): title = False
        else: title = self.title_widget.get_value().lower()
        if not self.description_widget.get_value(): description = False
        else: description = self.description_widget.get_value().lower()

        return {
            **self.images_widget.get_value(),
            **{ "id": self.id_widget.text().lower() },
            **{ "title": title },
            **{ "description": description },
        }

    def handle_re_set_id(self):
        now = datetime.datetime.now()
        randint = random.randint(0, 100)
        product_id = f"MISC.{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
        self.id_widget.setText(product_id)
