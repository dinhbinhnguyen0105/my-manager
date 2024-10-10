import os, sys
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.join(__file__, os.path.pardir))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir))
sys.path.append(SRC_DIR)
from views.utils import handle_widget
from logic.db.local import products

class Options(QFrame):
    current_option_widget_event = pyqtSignal(QPushButton)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "list__header__options")
        self.setObjectName("list__header__options")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
        self.current_option_index = 0
        self.product_data = products.info_read()

        for index, option in enumerate(self.product_data.keys()):
            self.handle_create_option_widget(index, option)

    
    def handle_create_option_widget(self, index, option):
        option_widget = QPushButton(self)
        option_widget.setObjectName(f"option__{option}")
        option_widget.setProperty("class", f"list__header__option option__{option}")
        option_widget.setProperty("user-data", f"{option}")
        option_widget.setProperty("option-index", index)
        option_widget.clicked.connect(lambda : self.handle_option_clicked(option_widget))
        if option == "real-estate": option_widget.setText("Real estate")
        elif option == "miscellaneous": option_widget.setText("Miscellaneous")
        self.layout().addWidget(option_widget)
        
    def showEvent(self, e):
        option_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "list__header__option")
        self.current_option_index = 0
        handle_widget.add_class(option_widgets[0], "activated")
        self.current_option_widget_event.emit(option_widgets[0])
        self.setStyleSheet(self.styleSheet())
    
    def handle_option_clicked(self, current_option_widget):
        option_widgets = handle_widget.find_widgets_by_class(self, QPushButton, "list__header__option")
        activated_button_widget = handle_widget.find_widgets_by_class(self, QPushButton, "activated")[0]
        handle_widget.remove_class(activated_button_widget, "activated")
        
        for index, button_widget in enumerate(option_widgets):
            if button_widget != current_option_widget: handle_widget.remove_class(button_widget, "activated")
            else:
                handle_widget.add_class(button_widget, "activated")
                self.current_option_widget_event.emit(button_widget)

        self.setStyleSheet(self.styleSheet())