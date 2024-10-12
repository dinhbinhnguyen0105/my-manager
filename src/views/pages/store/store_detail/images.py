import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))

sys.path.append(SRC_DIR)
from views.components import dropbox, imagebox

class Images(QFrame):
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): _class = payload["class"]
        else: _class = None
        if "label" in payload.keys(): label = payload["label"]
        else: label = False
        if "place_holder" in payload.keys(): place_holder = payload["place_holder"]
        else: place_holder = False
        if "id" in payload.keys(): id = payload["id"]
        else: id = False
        if "user-data" in payload.keys(): user_data = payload["user-data"]
        else: user_data = False

        self.setProperty("class", _class)
        if id: self.setObjectName(id)
        if user_data: self.setProperty("user-data", payload["user-data"])

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(main_layout)
    
    def handle_set_imgs(self, img_paths):
        if hasattr(self, "img_box"):
            self.img_box.setParent(None)
            self.img_box.deleteLater()
        self.img_box = imagebox.ImageBox(self)
        self.img_box.set_images(img_paths)
        self.layout().addWidget(self.img_box)

    
    def get_value(self):
        if self.img_box: return { "images": self.img_box.urls }
        return { "images" : []}