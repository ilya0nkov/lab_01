import sys, csv
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class Window():
    def __init__(self):
        self.application()

    def application(self):
        # создание окна
        app = QApplication(sys.argv)
        window = QMainWindow()

        app.setWindowIcon(QtGui.QIcon('icon.png'))

        # узнаем разрешение экрана
        screen = app.primaryScreen()
        size = screen.size()

        # задаем размеры окна в зависимости от разрешения экрана
        window_width = int(size.width()*0.6667)
        window_height = int(size.height()*0.6667)
        shift_width = int(window_width/4)
        shift_height = int(window_height/4)
        ## print(window_height, window_width, shift_height, shift_width)

        # устанавливаем параметры окна
        window.setWindowTitle("Database Assistant")
        window.setGeometry(shift_width, shift_height, window_width, window_height)

        # запуск и выключение
        window.show()
        sys.exit(app.exec_())


class Options():
    def __init__(self):
        self.write_csv()

    def write_csv(self):
        with open("DATABASE.csv", "w", newline=) as csvfile:
            line_write = csv.writer(csvfile, )











if __name__ == "__main__":
    Window()

