CONST_MAIN_WINDOW = """
            QMainWindow {
                background-color: #fbe8f9;
            }
            QLabel {
                color: #6a1b9a;
                font-size: 16px;
                font-family: 'Segoe UI', sans-serif;
                padding: 10px;
                text-align: center;
            }
            QPushButton {
                background-color: #e1bee7;
                color: #4a148c;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
                border: 1px solid #ba68c8;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #ce93d8; 
            }
            QPushButton:pressed {
                background-color: #ab47bc; 
            }
        """
        
CONST_PASSWORD_WINDOW = """
            QMainWindow {
                background-color: #fbe8f9;
            }
            QLabel {
                color: #6a1b9a;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
                padding: 5px;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ba68c8;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton {
                background-color: #e1bee7;
                color: #4a148c;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
                border: 1px solid #ba68c8;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #ce93d8;
            QPushButton:pressed {
                background-color: #ab47bc;
            }
        """
        
POP_UPS = """
    QMessageBox {
        background-color: #fbe8f9;
        color: #4a148c;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
        border: 1px solid #ba68c8;
        border-radius: 0px;
        padding: 10px;
    }
    QMessageBox QLabel {
        color: #6a1b9a;
        font-size: 14px;
    }
    QMessageBox QPushButton {
        background-color: #e1bee7;
        color: #4a148c; 
        border: 1px solid #ba68c8;
        border-radius: 0px;
        padding: 5px 10px;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
    }
    QMessageBox QPushButton:hover {
        background-color: #ce93d8;
    }
    QMessageBox QPushButton:pressed {
        background-color: #ab47bc;
    }
"""

CONST_ADD_WINDOW = """
            QMainWindow {
                background-color: #fbe8f9;
            }
            QLabel {
                color: #6a1b9a;
                font-size: 16px;
                font-family: 'Segoe UI', sans-serif;
                padding: 10px;
                text-align: center;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ba68c8;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton {
                background-color: #e1bee7;
                color: #4a148c;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
                border: 1px solid #ba68c8;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #ce93d8;
            }
            QPushButton:pressed {
                background-color: #ab47bc;
            }
        """
        
CONST_VIEW_WINDOW = """
    QMainWindow {
        background-color: #fbe8f9;
    }
    QLabel#dateLabel {
        color: #6a1b9a;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
        padding: 5px;
        background-color: #ffffff;
        border: 1px solid #ba68c8;
        border-radius: 5px;
        min-width: 100px; /* Фиксированная ширина для даты */
        max-width: 120px;
        text-align: center;
    }
    QLabel#textLabel {
        color: #6a1b9a;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
        padding: 10px;
        background-color: #ffffff;
        border: 1px solid #ab47bc;
        border-radius: 5px;
        min-width: 350px;
        max-width: 400px;
        min-height: 50px;
        text-align: left;
        word-wrap: true;
    }
    QScrollArea {
        background-color: #ffffff;
        border: 1px solid #ba68c8;
        border-radius: 5px;
    }
    QScrollBar:vertical {
        background: #e1bee7;
        width: 10px;
        margin: 0;
    }
    QScrollBar::handle:vertical {
        background: #ba68c8;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical:hover {
        background: #ab47bc;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;
    }
    QPushButton {
        background-color: #e1bee7;
        color: #4a148c;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
        border: 1px solid #ba68c8;
        border-radius: 5px;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #ce93d8;
    }
    QPushButton:pressed {
        background-color: #ab47bc;
    }
"""