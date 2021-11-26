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
        self.btn.clicked.connect(self.click)
        self.change()
        self.w2 = SecondWidget()
        self.w2.show()

    def change(self):
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
        con.close()

    def click(self):
        self.change()


class SecondWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Редактирование')
        self.move(0, 200)
        self.btn_add.clicked.connect(self.change)
        self.btn_edit.clicked.connect(self.change)

    def change(self):
        text = self.sender().text()
        name = self.name.text()
        degree = self.degree.text()
        type = self.type.text()
        taste = self.taste.text()
        cost = self.cost.text()
        amount = self.amount.text()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        if text == 'Добавить':
            cur.execute("""INSERT INTO characteristics(name, 'degree of roasting', 'ground/beans', taste, cost, amount)
            VALUES(?, ?, ?, ?, ?, ?)""", (name, degree, type, taste, cost, amount))
        elif text == 'Редактировать':
            cur.execute("""UPDATE characteristics
            SET 'degree of roasting' = ?,
            'ground/beans' = ?,
            taste = ?,
            cost = ?,
            amount = ?
            WHERE name = ?""", (degree, type, taste, cost, amount, name))
        con.commit()
        con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())