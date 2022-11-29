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
        self.database_writer()
        hashsum_new = self.hash_file()
        self.hash_new(hashsum_new)

    # контрольная сумма
    # проверка текущей хэш суммы
    def hash_file(self):
        h = hashlib.sha1()

        with open("DATABASE.csv", "rb") as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
        hashsum = h.hexdigest()
        return hashsum

    # сравнение текущей хэш суммы с предыдущей
    def hash_check(self, hashsum):
        hex_digest = hashsum
        ###print(hashsum, "2")
        last_hash = open("hashsum.txt", "r").readline()
        ###print(last_hash)
        if last_hash != hex_digest:
            print("Error. File was changed")

    # резервирование переменных под столбцы таблицы
    # company_id = int(input("company_id\n"))
    # запись в файл
    # utf-8 может конфликтовать в windows с текстом на латинице, поэтому cp1251
    def database_writer(self):
        database = "DATABASE.csv"
        company_name = str(input("company_name\n"))
        with open(database, "r", encoding="cp1251", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            max_company_id = 0
            for row in reader:
                if str(row["company_name"]) == company_name:
                    company_id = int(row["company_id"])
                    break
                elif max_company_id < int(row["company_id"]):
                    max_company_id = int(row["company_id"])
            else:
                company_id = max_company_id + 1

        company_inn = str(input("company_inn\n"))
        currency = {1: "RUB", 2: "USD", 3: "EUR"}
        currency_select = int(input("1: RUB, 2: USD, 3: EUR\n"))
        sum_total = int(input("sum_total\n"))
        sum_nds = sum_total * 0.87
        order_status = {1: "Awaiting confirmation", 2: "Paid",
                        3: "On the way", 4: "Delivered", 5: "Cancelled"}
        order_status_select = int(input("Order status:\n"
                                        "1: Awaiting confirmation, 2: Paid, \n"
                                        "3: On the way, 4: Delivered, 5: Cancelled\n"))
        print(f"name: {company_name}\t | currency: {currency[currency_select]}\n"
              f"sum: {sum_total}\t | sum with nds: {sum_nds}\n"
              f"order status: {order_status[order_status_select]}\n")

        with open(database, "a", encoding="cp1251", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [company_id,
                    company_name, company_inn, currency[currency_select],
                 sum_total, sum_nds, order_status[order_status_select]]
            )

    # запись новой хэш суммы
    def hash_new(self, hashsum_new):
        new_hash = open("hashsum.txt", "w").write(hashsum_new)

    def export_filters(self):
        filter = int(input(""))
        filters = {}











if __name__ == "__main__":
    Options()

