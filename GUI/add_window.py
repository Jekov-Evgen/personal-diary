from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from GUI.style_window import CONST_ADD_WINDOW
from datetime import date
from Logics.database_work import insert_to_bd

class AddWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(300, 300)
        self.setWindowTitle("Добавление записи")
        self.setStyleSheet(CONST_ADD_WINDOW)
        self.setWindowIcon(QIcon(r'image\icon.png'))
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        add_your_entry = QLabel("Добавление записи")
        self.record = QLineEdit()
        add_button = QPushButton("Добавить запись")
        
        control_UI.addWidget(add_your_entry, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.record)
        control_UI.addWidget(add_button)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def adding_an_entry(self):
        add_text = self.record.text()
        
        date_PC = None
        
        insert_to_bd(date_PC, add_text)