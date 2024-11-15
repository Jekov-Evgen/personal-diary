from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from GUI.main_gui import MainWindow
from GUI.style_window import CONST_PASSWORD_WINDOW, POP_UPS

class PasswordWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ввод пароля")
        self.setFixedSize(300, 150)
        self.setStyleSheet(CONST_PASSWORD_WINDOW)
        self.setWindowIcon(QIcon(r'image\icon.png'))
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        self.error = None
        self.run = None
        
        label_entering_password = QLabel(text="Введите пароль для доступа")
        self.entering_password = QLineEdit()
        
        button_entering_password = QPushButton("Вход")
        button_entering_password.clicked.connect(self.login_verification)
        
        control_UI.addWidget(label_entering_password, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.entering_password)
        control_UI.addWidget(button_entering_password)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def login_verification(self):
        try:
            examination = self.entering_password.text()
        except:
               self.error = QMessageBox()
               self.error.setStyleSheet(POP_UPS)
               self.setWindowIcon(QIcon(r'image\icon.png'))
               self.error.setWindowTitle("Ошибка")
               self.error.setText("Ошибка считывания")
               self.error.show()
               
        res_ex = 0
        
        for i in range(len(examination)):
            res_ex += ord(examination[i])
        
        if res_ex == 700:
            self.hide()
            self.run = MainWindow()
        else:
            self.error = QMessageBox()
            self.error.setStyleSheet(POP_UPS)
            self.setWindowIcon(QIcon(r'image\icon.png'))
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Неверный пароль")
            
            self.error.show()