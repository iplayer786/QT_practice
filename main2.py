from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton , QLineEdit
import sys

#After OOP

def main():
    app = QApplication([])
    win = main_window()
    
    sys.exit(app.exec())
    
#Object
class main_window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,480,320)
        self.setWindowTitle("This is a window")
        self.ui_elements()
       
    def ui_elements(self):
        self.label = QLabel("This is a label")
        self.textline = QLineEdit("This is a text line")
        self.button = QPushButton("A button")
        self.button.clicked.connect(self.check_button)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textline)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.show()
  
    
    def check_button(self):
        print("clicked")

if __name__ == "__main__":
    main()