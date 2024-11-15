from GUI.password_window import PasswordWindow
from PyQt6.QtWidgets import QApplication
from Logics.database_work import connect_to_bd

if __name__ == "__main__":
    app = QApplication([])
    
    start = PasswordWindow()
    connect_to_bd()
    
    app.exec()