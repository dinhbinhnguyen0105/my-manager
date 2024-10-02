import os, sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout
MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
MAIN_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))

from create_item_options import CreateItem_Options
sys.path.append(MAIN_DIR)
from views.utils import handle_widget

class CreateItem(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog create-item")
        self.setObjectName("dialog__create-item")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        self.resize(400, 700)
        # main_layout.setAlignment(Qt.AlignTop)

        self.options_widget = CreateItem_Options(self)
        self.options_widget.current_option_event.connect(lambda e: print(e))
        main_layout.addWidget(self.options_widget)

        with open(os.path.join(MY_DIR, "create_item.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)

    def UI_realestate(self):

        pass
    
    

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])

    window = CreateItem()
    window.show()

    sys.exit(app.exec_())