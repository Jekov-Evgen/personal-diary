from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
from GUI.style_window import CONST_MAIN_WINDOW

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Личный дневник")
        self.setFixedSize(500, 300)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        central_widget = QWidget()
        control_UI = QVBoxLayout()
        
        greetings = QLabel(text="Приветсвую вас в приложении ведения секретного дневника")
        add_entry = QPushButton(text="Добавить запись")
        see_all_posts = QPushButton(text="Просмотреть все записи")
        
        control_UI.addWidget(greetings, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(add_entry)
        control_UI.addWidget(see_all_posts)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)
        
        self.show()