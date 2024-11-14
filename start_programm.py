from GUI.password_window import PasswordWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    
    start = PasswordWindow()
    
    app.exec()