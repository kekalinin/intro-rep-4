import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class Espresso(QMainWindow):
    def __init__(self):
        super(Espresso, self).__init__()
        uic.loadUi("main.ui", self)
        self.load_coffee()

    def load_coffee(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute(f"""SELECT sort, stepen, v_zernah, vkus, price, volume FROM coffee""").fetchall()

        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(["Сорт", "Степень", "Формат", "Вкус", "Цена", "Объем"])
        for i, stroka in enumerate(data):
            for j, stolbec in enumerate(stroka):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(stolbec)))
        con.close()


app = QApplication(sys.argv)
win = Espresso()
win.show()
sys.exit(app.exec())
