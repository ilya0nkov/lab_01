import sys, csv, hashlib
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
        hashsum = self.hash_file()
        self.hash_check(hashsum)
        self.write_csv()
        hashsum_new = self.hash_file()
        self.hash_new(hashsum_new)

    ## контрольная сумма
    # проверка текущей хэш суммы
    def hash_file(self):
        h = hashlib.sha1()

        with open("DATABASE.csv", "rb") as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        hashsum = h.hexdigest()
        ###print(hashsum, "1")
        return hashsum

    # сравнение текущей хэш суммы с предыдущей
    def hash_check(self, hashsum):
        hex_digest = hashsum
        ###print(hashsum, "2")
        last_hash = open("hashsum.txt", "r").readline()
        ###print(last_hash)
        if last_hash != hex_digest:
            print("Error. File was changed")

    def write_csv(self):
        # резервирование переменных под столбцы таблицы
        company_id = int(input("company_id\n"))
        company_name = str(input("company_name\n"))
        company_inn = str(input("company_inn\n"))
        currency = {1: "RUB", 2: "USD", 3: "EUR"}
        currency_select = int(input("1: RUB, 2: USD, 3: EUR\n"))
        sum_total = int(input("sum_total\n"))
        sum_nds = sum_total * 0.87
        print(f"name: {company_name}\t | currency: {currency[currency_select]}\n"
              f"sum: {sum_total}\t | sum with nds: {sum_nds}")

        # запись в файл
        # utf-8 может конфликтовать в windows с текстом на латинице, поэтому cp1251
        with open("DATABASE.csv", "a", encoding="cp1251", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [company_id, company_name, company_inn,
                 currency[currency_select], sum_total, sum_nds]
            )

    # запись новой хэш суммы
    def hash_new(self, hashsum_new):
        new_hash = open("hashsum.txt", "w").write(hashsum_new)













if __name__ == "__main__":
    Options()

