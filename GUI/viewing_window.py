from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

class ViewWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Окно просмотра")
        self.setWindowIcon(QIcon(r"image\icon.png"))
        
        
        self.show()