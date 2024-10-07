import os, sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.components import dropbox, imagebox

class Images(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content__images")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.drop_widget = dropbox.Dropbox(self)
        self.drop_widget.e_dropped_urls.connect(self.handle_dropped_imgs)

        main_layout.addWidget(self.drop_widget)

    def handle_dropped_imgs(self, e):
        self.drop_widget.hide()
        self.img_box = imagebox.ImageBox(self)
        self.img_box.set_images(e)
        self.layout().addWidget(self.img_box)