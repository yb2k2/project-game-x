import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, QSpacerItem,
                             QSizePolicy)
from PyQt5.QtCore import Qt

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Màn Hình Chơi Game")

        # Create widgets
        self.title_label = QLabel("Chào Mừng Đến Với Trò Chơi!")
        self.info_label = QLabel("Thông tin về trò chơi sẽ được hiển thị ở đây.")
        self.buttons = [QPushButton(f"Ô {i+1}") for i in range(9)]
        self.start_button = QPushButton("Bắt Đầu")
        self.pause_button = QPushButton("Tạm Dừng")
        self.end_button = QPushButton("Kết Thúc")

        # Set font for labels
        font = self.title_label.font()
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)
        self.info_label.setFont(font)

        # Create layouts
        hbox = QHBoxLayout()
        for i in range(3):
            hbox.addWidget(self.buttons[i * 3 + i], alignment=Qt.AlignCenter)
        for i in range(1, 3):
            vbox = QVBoxLayout()
            for j in range(3):
                vbox.addWidget(self.buttons[i * 3 + j], alignment=Qt.AlignCenter)
            hbox.addLayout(vbox)

        vbox = QVBoxLayout()
        vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        vbox.addWidget(self.title_label, alignment=Qt.AlignCenter)
        vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        vbox.addWidget(self.info_label, alignment=Qt.AlignCenter)
        vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        vbox.addLayout(hbox)
        vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        vbox.addWidget(self.start_button, alignment=Qt.AlignCenter)
        vbox.addWidget(self.pause_button, alignment=Qt.AlignCenter)
        vbox.addWidget(self.end_button, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWidget()
    window.show()
    sys.exit(app.exec_())