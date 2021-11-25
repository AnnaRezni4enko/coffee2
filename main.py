import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Информация')
        title = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена',
                 'объем упаковки']
        self.table.setColumnCount(len(title))
        self.table.setHorizontalHeaderLabels(title)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM characteristics""")
        for i in result:
            self.table.setRowCount(self.table.rowCount() + 1)
            for j in range(7):
                self.table.setItem(self.table.rowCount() - 1, j, QTableWidgetItem(str(i[j])))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())