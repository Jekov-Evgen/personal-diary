from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton
from Logics.database_work import get_data_bd
from GUI.style_window import CONST_VIEW_WINDOW

class ViewWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(600, 600)
        self.setWindowTitle("Окно просмотра")
        self.setStyleSheet(CONST_VIEW_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.png"))
        
        records = get_data_bd()
        
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        return_button = QPushButton("Вернуться на главное окно")
        return_button.clicked.connect(self.to_main)

        for record in records:
            field_layout = QHBoxLayout()
            
            date_label = QLabel(record[1])
            date_label.setObjectName("dateLabel")
            text_label = QLabel(record[2])
            text_label.setObjectName("textLabel")
            
            field_layout.addWidget(date_label)
            field_layout.addStretch(1)
            field_layout.addWidget(text_label)
            
            main_layout.addLayout(field_layout)

        scroll_area = QScrollArea()
        scroll_content = QWidget()
        scroll_content.setLayout(main_layout)
        
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        central_layout = QVBoxLayout()
        central_layout.addWidget(scroll_area)
        central_layout.addWidget(return_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.show()
        
    def to_main(self):
        from GUI.main_gui import MainWindow
        self.hide()
        self.main = MainWindow()
        self.main.show()