from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
from GUI.style_window import CONST_MAIN_WINDOW
from GUI.add_window import AddWindow
from GUI.viewing_window import ViewWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Личный дневник")
        self.setFixedSize(500, 300)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon(r'image\icon.png'))
        
        self.add = None
        self.see = None
        
        central_widget = QWidget()
        control_UI = QVBoxLayout()
        
        greetings = QLabel(text="Приветсвую вас в приложении ведения секретного дневника")
        
        add_entry = QPushButton(text="Добавить запись")
        add_entry.clicked.connect(self.add_record)
        
        see_all_posts = QPushButton(text="Просмотреть все записи")
        see_all_posts.clicked.connect(self.see_all)
        
        control_UI.addWidget(greetings, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(add_entry)
        control_UI.addWidget(see_all_posts)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)
        
        self.show()
        
        
    def add_record(self):
        self.hide()
        self.add = AddWindow()
        
    def see_all(self):
        self.hide()
        self.see = ViewWindow()