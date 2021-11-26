import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 160, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 20, 160, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.name.setObjectName("name")
        self.verticalLayout_2.addWidget(self.name)
        self.degree = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.degree.setObjectName("degree")
        self.verticalLayout_2.addWidget(self.degree)
        self.type = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.type.setObjectName("type")
        self.verticalLayout_2.addWidget(self.type)
        self.taste = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.taste.setObjectName("taste")
        self.verticalLayout_2.addWidget(self.taste)
        self.cost = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.cost.setObjectName("cost")
        self.verticalLayout_2.addWidget(self.cost)
        self.amount = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.amount.setObjectName("amount")
        self.verticalLayout_2.addWidget(self.amount)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(110, 240, 93, 28))
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(220, 240, 131, 28))
        self.btn_edit.setObjectName("btn_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "название"))
        self.label_3.setText(_translate("MainWindow", "степень прожарки"))
        self.label_4.setText(_translate("MainWindow", "молотый/в зернах"))
        self.label_5.setText(_translate("MainWindow", "описание вкуса"))
        self.label_6.setText(_translate("MainWindow", "цена"))
        self.label_7.setText(_translate("MainWindow", "объем упаковки"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
        self.btn_edit.setText(_translate("MainWindow", "Редактировать"))


class Ui_MainWindow1(object):
    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 20, 931, 521))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(860, 550, 93, 28))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Обновить"))


class MyWidget(QMainWindow, Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi1(self)
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


class SecondWidget(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)
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