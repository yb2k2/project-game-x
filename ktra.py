import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pushbutton widgets (Yes or No)?")

        # Create two pushbuttons
        self.button1 = QPushButton("Bắt đầu game")
        self.button2 = QPushButton("Thoát Game")

        # Create a vertical layout and add the buttons
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Set the layout for the window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())