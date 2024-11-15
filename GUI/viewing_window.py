from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea
from Logics.database_work import get_data_bd

class ViewWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Окно просмотра")
        self.setWindowIcon(QIcon(r"image\icon.png"))
        
        records = get_data_bd()
        
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        for record in records:
            field_layout = QHBoxLayout()
            
            date_label = QLabel(text=record[1])
            text_label = QLabel(text=record[2])
            
            field_layout.addWidget(date_label)
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
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.show()