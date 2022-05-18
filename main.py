from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QPushButton , QLineEdit
import sys

#Prior to OOP

def check_button():
    print("clicked")


app = QApplication([])


#Widget vs QMainWindow! Using Widget
#Win = Window
win = QWidget()
win.setGeometry(0,0,480,320)
win.setWindowTitle("This is a window")

label = QLabel("This is a label")
textline = QLineEdit("This is a text line")
button = QPushButton("A button")
button.clicked.connect(check_button)


layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(textline)
layout.addWidget(button)

win.setLayout(layout)
win.show()

sys.exit(app.exec())