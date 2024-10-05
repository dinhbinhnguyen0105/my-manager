import platform, os, subprocess
from pathlib import Path
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMouseEvent, QCloseEvent, QWheelEvent


class ImageBox(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.prev_point, self.curr_point, self.slide, self.images_count, self.image_folder, self.urls = 0, 0, 0, 0, None, []
        self.setProperty("class", "image-box")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)
        self.main_widget = QStackedWidget(self)
        # self.main_widget.setProperty("class", "image-box__container")
        self.main_widget.setContentsMargins(0,0,0,0)
        main_layout.addWidget(self.main_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.resize(400, 200)
        

    def set_images(self, urls):
        self.img_count = len(urls)
        self.urls = urls
        for url in self.urls:
            img = Image(url, self)
            self.main_widget.addWidget(img)
        self.main_widget.setCurrentIndex(0)
    
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        return super().closeEvent(a0)
    
    def wheelEvent(self, a0: QWheelEvent) -> None:
        self.curr_point += a0.pixelDelta().y()
        if self.curr_point < self.prev_point:
            self.slide -= 1
        elif self.curr_point > self.prev_point:
            self.slide += 1
        self.prev_point = self.curr_point
        if self.slide < 1:
            self.slide = 1
        if self.slide > self.img_count:
            self.slide = self.img_count
        self.main_widget.setCurrentIndex(self.slide)

class Image(QLabel):
    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.url = url
        self.setProperty("class", "image")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pixmap = QPixmap(url)
        self.pixmap = self.pixmap.scaled(
            self.parent().size(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(self.pixmap)

    def getImage(self):
        return self.url
    
    def mousePressEvent(self, ev: QMouseEvent | None) -> None:
        if self.url == None: return
        else:
            url = Path(self.url)
        if platform.system() == "Windows":
            os.startfile(url.parent)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", url.parent])
        else:
            subprocess.Popen(["xdg-open", url.parent])

# class Image(QLabel):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setProperty("class", "image")
#         main_layout = QVBoxLayout()
#         main_layout.setContentsMargins(0,0,0,0)
#         main_layout.setSpacing(0)
#         self.setLayout(main_layout)
#         self.url = None
    
#     def set_image(self, url):
#         self.url = url
#         label = QLabel(self)
#         pixmap = QPixmap(url)
#         pixmap = pixmap.scaled(
#             400, 200,
#             aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
#             transformMode=Qt.TransformationMode.SmoothTransformation
#         )
#         label.setPixmap(pixmap)
#         self.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.layout().addWidget(label)

    

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    imgbox = ImageBox()
    imgbox.show()
    imgbox.set_images([
        "/Users/dinhbinh/REImgs/re_3/1I93347RG_99MRDO.jpg",
        "/Users/dinhbinh/REImgs/re_3/1I93347TV_99MRDO.jpg",
        "/Users/dinhbinh/REImgs/re_3/1I93347TH_99MRDO.jpg",
    ])
    sys.exit(app.exec_())