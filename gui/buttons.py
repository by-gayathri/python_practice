import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 700, 700)
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Welcome😀", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_clicked)

        self.label.setGeometry(150, 300, 300, 450)
        self.label.setStyleSheet("font-size: 50px")

    def on_clicked(self):
        print("Button Clicked")
        # self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.label.setText("Goodbye🙄")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
