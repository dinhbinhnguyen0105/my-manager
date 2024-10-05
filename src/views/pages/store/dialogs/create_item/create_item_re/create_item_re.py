import os, sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QShowEvent, QPixmap
from PyQt5.QtWidgets import QFrame, QDialog, QLabel, QScrollArea, QVBoxLayout, QSizePolicy, QWidget, QHBoxLayout, QPushButton
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
sys.path.append(MAIN_DIR)
from views.utils import handle_widget
from views.components import dropbox, imagebox

class CreateItemRe(QFrame):
    current_option_event = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "content real-estate")
        self.setProperty("user-data", "real-estate")
        self.setProperty("option-index", 0)
        self.setObjectName("real-estate")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.drop_widget = dropbox.Dropbox(self)
        self.drop_widget.e_dropped_urls.connect(self.handle_dropped_imgs)

        # self.img_box = QFrame(self)

        # self.image_box = imagebox.ImageBox(self)
        # self.image_box.setFixedSize(400, 200)
        # main_layout.addWidget(self.image_box)
        main_layout.addWidget(self.drop_widget)
        main_layout.addWidget(QLabel("RE"))
    

    
    def handle_dropped_imgs(self, e):
        self.img_box = imagebox.ImageBox(self)
        self.img_box.set_images(e)
        self.layout().addWidget(self.img_box)
        # for img in handle_widget.find_widgets_by_class(self, QLabel, "image"):
        #     img.pixmap = img.pixmap.scaled(
        #         self.size(),
        #         aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
        #         transformMode=Qt.TransformationMode.SmoothTransformation
        #     )
        #     img.setPixmap(img.pixmap)
