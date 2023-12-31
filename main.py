import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog

from add_ui import Ui_DialogAddDevice
from main_ui import Ui_MainWindow


class EditCoffee(QDialog, Ui_DialogAddDevice):
    def __init__(self):
        self.setupUi(self)
        super(EditCoffee, self).__init__()

    def accept(self) -> None:
        con = sqlite3.connect('data/coffee.sqlite')
        con.cursor().execute('INSERT INTO coffee(sort, stepen, v_zernah, vkus, price, volume) VALUES (?,?,?,?,?,?)',
                             (self.SortEdit.text(),
                              self.StepenEdit.text(),
                              self.FormatEdit.text(),
                              self.VkusEdit.text(),
                              self.PriceEdit.text(),
                              self.VolumeEdit.text()))
        con.commit()
        con.close()
        self.done(0)

    def reject(self) -> None:
        self.done(0)


class Espresso(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Espresso, self).__init__()
        self.setupUi(self)
        self.load_coffee()
        self.addCoffee.clicked.connect(self.add_cofee)

    def load_coffee(self):
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        data = cur.execute(f"""SELECT sort, stepen, v_zernah, vkus, price, volume FROM coffee""").fetchall()

        self.tableWidget.setColumnCount(len(data[0]))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(["Сорт", "Степень", "Формат", "Вкус", "Цена", "Объем"])
        for i, stroka in enumerate(data):
            for j, stolbec in enumerate(stroka):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(stolbec)))
        con.close()

    def add_cofee(self) -> None:
        EDB = EditCoffee()
        EDB.show()
        EDB.exec()
        self.load_coffee()


app = QApplication(sys.argv)
win = Espresso()
win.show()
sys.exit(app.exec())
