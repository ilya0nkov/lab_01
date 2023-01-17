import csv, hashlib
from PyQt5 import QtWidgets, QtGui, QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 694))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1280, 694))
        self.tabWidget.setMaximumSize(QtCore.QSize(1280, 694))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("background-color: rgb(216, 228, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.Table = QtWidgets.QWidget()
        self.Table.setAcceptDrops(False)
        self.Table.setObjectName("Table")
        self.tableWidget = QtWidgets.QTableWidget(self.Table)
        self.tableWidget.setGeometry(QtCore.QRect(0, 210, 1280, 460))
        self.tableWidget.setStyleSheet("background-color: rgb(216, 228, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(179)
        self.frame = QtWidgets.QFrame(self.Table)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 210))
        self.frame.setMinimumSize(QtCore.QSize(1280, 210))
        self.frame.setMaximumSize(QtCore.QSize(1280, 210))
        self.frame.setStyleSheet("background-color: rgb(216, 228, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_oid = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_oid.setGeometry(QtCore.QRect(929, 109, 150, 22))
        self.lineEdit_oid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_oid.setObjectName("lineEdit_oid")
        self.lineEdit_cn = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cn.setGeometry(QtCore.QRect(160, 109, 190, 22))
        self.lineEdit_cn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cn.setObjectName("lineEdit_cn")
        self.lineEdit_cost = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cost.setGeometry(QtCore.QRect(740, 109, 160, 22))
        self.lineEdit_cost.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cost.setObjectName("lineEdit_cost")
        self.lineEdit_tin = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_tin.setGeometry(QtCore.QRect(380, 109, 170, 22))
        self.lineEdit_tin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_tin.setObjectName("lineEdit_tin")
        self.lineEdit_cid = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_cid.setGeometry(QtCore.QRect(20, 109, 110, 22))
        self.lineEdit_cid.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_cid.setObjectName("lineEdit_cid")
        self.label_cid = QtWidgets.QLabel(self.frame)
        self.label_cid.setGeometry(QtCore.QRect(30, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cid.setFont(font)
        self.label_cid.setObjectName("label_cid")
        self.label_cn = QtWidgets.QLabel(self.frame)
        self.label_cn.setGeometry(QtCore.QRect(190, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cn.setFont(font)
        self.label_cn.setObjectName("label_cn")
        self.label_tin = QtWidgets.QLabel(self.frame)
        self.label_tin.setGeometry(QtCore.QRect(460, 80, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_tin.setFont(font)
        self.label_tin.setObjectName("label_tin")
        self.label_Currency = QtWidgets.QLabel(self.frame)
        self.label_Currency.setGeometry(QtCore.QRect(610, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Currency.setFont(font)
        self.label_Currency.setObjectName("label_Currency")
        self.label_cost = QtWidgets.QLabel(self.frame)
        self.label_cost.setGeometry(QtCore.QRect(800, 80, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cost.setFont(font)
        self.label_cost.setObjectName("label_cost")
        self.label_oid = QtWidgets.QLabel(self.frame)
        self.label_oid.setGeometry(QtCore.QRect(970, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_oid.setFont(font)
        self.label_oid.setObjectName("label_oid")
        self.label_status = QtWidgets.QLabel(self.frame)
        self.label_status.setGeometry(QtCore.QRect(1150, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.label_enterText = QtWidgets.QLabel(self.frame)
        self.label_enterText.setGeometry(QtCore.QRect(20, 10, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_enterText.setFont(font)
        self.label_enterText.setObjectName("label_enterText")
        self.pushButton_add = QtWidgets.QPushButton(self.frame)
        self.pushButton_add.setGeometry(QtCore.QRect(440, 160, 90, 28))
        self.pushButton_add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_del = QtWidgets.QPushButton(self.frame)
        self.pushButton_del.setGeometry(QtCore.QRect(570, 160, 90, 28))
        self.pushButton_del.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_upd = QtWidgets.QPushButton(self.frame)
        self.pushButton_upd.setGeometry(QtCore.QRect(700, 160, 90, 28))
        self.pushButton_upd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_upd.setObjectName("pushButton_upd")
        self.comboBox_currency = QtWidgets.QComboBox(self.frame)
        self.comboBox_currency.setGeometry(QtCore.QRect(590, 109, 120, 22))
        self.comboBox_currency.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_currency.setObjectName("comboBox_currency")
        self.comboBox_currency.addItem("")
        self.comboBox_currency.setItemText(0, "")
        self.comboBox_currency.addItem("")
        self.comboBox_currency.addItem("")
        self.comboBox_currency.addItem("")
        self.comboBox_status = QtWidgets.QComboBox(self.frame)
        self.comboBox_status.setGeometry(QtCore.QRect(1110, 109, 140, 22))
        self.comboBox_status.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_status.setObjectName("comboBox_status")
        self.comboBox_status.addItem("")
        self.comboBox_status.setItemText(0, "")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.comboBox_status.addItem("")
        self.tabWidget.addTab(self.Table, "")
        self.Graphics = QtWidgets.QWidget()
        self.Graphics.setObjectName("Graphics")
        self.tabWidget.addTab(self.Graphics, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionOpen.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionServer = QtWidgets.QAction(MainWindow)
        self.actionServer.setObjectName("actionServer")
        self.actionServer_2 = QtWidgets.QAction(MainWindow)
        self.actionServer_2.setObjectName("actionServer_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionServer_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Assistant"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "company_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "company_name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "tin"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "currency"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "cost"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "order_id"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "status"))
        self.label_cid.setText(_translate("MainWindow", "company id"))
        self.label_cn.setText(_translate("MainWindow", "company name"))
        self.label_tin.setText(_translate("MainWindow", "tin"))
        self.label_Currency.setText(_translate("MainWindow", "currency"))
        self.label_cost.setText(_translate("MainWindow", "cost"))
        self.label_oid.setText(_translate("MainWindow", "order_id"))
        self.label_status.setText(_translate("MainWindow", "status"))
        self.label_enterText.setText(_translate("MainWindow", "Enter new lines in the fields below:"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_del.setText(_translate("MainWindow", "Delete"))
        self.pushButton_upd.setText(_translate("MainWindow", "Update"))
        self.comboBox_currency.setItemText(1, _translate("MainWindow", "RUB"))
        self.comboBox_currency.setItemText(2, _translate("MainWindow", "USD"))
        self.comboBox_currency.setItemText(3, _translate("MainWindow", "EUR"))
        self.comboBox_status.setItemText(1, _translate("MainWindow", "Awaiting confirm"))
        self.comboBox_status.setItemText(2, _translate("MainWindow", "Paid"))
        self.comboBox_status.setItemText(3, _translate("MainWindow", "On the way"))
        self.comboBox_status.setItemText(4, _translate("MainWindow", "Delivered"))
        self.comboBox_status.setItemText(5, _translate("MainWindow", "Cancelled"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Table), _translate("MainWindow", "Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Graphics), _translate("MainWindow", "Data Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setIconText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionServer.setText(_translate("MainWindow", "Server"))
        self.actionServer_2.setText(_translate("MainWindow", "Server"))


class Options():
    def __init__(self):
        #hashsum = self.hash_file()
        #self.hash_check(hashsum)
        #self.database_writer()
        #hashsum_new = self.hash_file()
        #self.hash_new(hashsum_new)
        self.export_filters()

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
        open("hashsum.txt", "w").write(hashsum_new)

    # вывод файла по заданному фильтру
    def export_filters(self):
        # ООО "АНКОР ФИНТЕК"
        filter = str(input("filter:\n"))
        with open("EXPORT.csv", "w", encoding="cp1251", newline="") as export:
            writer = csv.writer(export, delimiter=";")

            with open("DATABASE.csv", "r", encoding="cp1251", newline="") as data:
                reader = csv.DictReader(data, delimiter=";")

                for row in reader:
                    if str(row["company_name"]) == filter:
                        writer.writerow(str(row["company_id"]).split() + str(row["company_name"]).splitlines() +
                                        str(row["company_inn"]).split() + str(row["currency"]).split() +
                                        str(row["sum_total"]).split() + str(row["sum_nds"]).split() + str(row["order_status"]).splitlines())






if __name__ == "__main__":
    Options()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

