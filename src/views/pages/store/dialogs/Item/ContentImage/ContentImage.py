
import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.components import dropbox, imagebox

class ContentImage(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__image content")
        self.setObjectName("content__image")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)
        self.img_box = None
        self.drop_widget = dropbox.Dropbox(self)
        self.drop_widget.e_dropped_urls.connect(self.set_value)

        main_layout.addWidget(self.drop_widget)
    
    def set_value(self, urls):
        self.drop_widget.hide()
        self.img_box = imagebox.ImageBox(self)
        self.img_box.set_images(urls)
        self.layout().addWidget(self.img_box)
    
    def get_value(self):
        if self.img_box: return { "images": self.img_box.urls }
        return { "images" : []}