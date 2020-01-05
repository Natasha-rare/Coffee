import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.params = ['id', 'сорт', 'степень обжарки',
                       'форма', 'вкус', 'цена', 'объем упаковки']
        self.con = sqlite3.connect("coffee.db")
        self.comboBox.addItems(self.params)
        self.change_btn.clicked.connect(self.change)
        # self.tableWidget.itemChanged.connect(self.item_changed)
        self.load.clicked.connect(self.load_result)
        self.titles = None
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(self.params)

    def load_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        req = "SELECT * FROM Coffee WHERE {} = {}".format(self.comboBox.currentText(),
                                                         self.lineEdit.text())
        if ("LIKE" in self.lineEdit.text().upper() or "BETWEEN" in self.lineEdit.text().upper() or
                "IN" in self.lineEdit.text().upper() or
                '<' in self.lineEdit.text() or '>' in self.lineEdit.text()):
            req = f"SELECT * FROM Coffee WHERE {self.comboBox.currentText()} {self.lineEdit.text()}"
        result = cur.execute(req).fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.con.commit()

    def change(self):
        self.changes_form = Changing()
        self.changes_form.show()


class Changing(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add.clicked.connect(self.add_new)
        self.change_btn.clicked.connect(self.change)
        self.show()
        self.con = sqlite3.connect("coffee.sqlite3")
        self.titles = None

    def change(self):

        self.modified = {}
        if self.sort.text():
            self.modified['сорт'] = self.sort.text()
        if self.value.text():
            self.modified['[степень обжарки]'] = self.value.text()
        if self.form.text():
            self.modified['форма'] = self.form.text()
        if self.taste.text():
            self.modified['вкус'] = self.taste.text()
        if self.price.text():
            self.modified['цена'] = int(self.price.text())
        if self.volume.text():
            self.modified['[объем упаковки]'] = int(self.volume.text())
        que = "UPDATE Coffee SET\n"
        for key in self.modified.keys():
            que += "{}='{}',\n".format(key, self.modified.get(key))
        cur = self.con.cursor()
        que = que[:-2]
        que += f"WHERE id = {int(self.id.text())}"
        cur.execute(que)
        print('fff')
        self.con.commit()

    def add_new(self):
        cur = self.con.cursor()
        que = "INSERT "\
            "INTO "\
            "Coffee ("\
            "id,"\
            "сорт,"\
            "[степень обжарки],"\
            "форма,"\
            "вкус,"\
            "цена,"\
            "[объем упаковки]"\
            ") "\
            "VALUES ("\
            f"{int(self.id.text())},"\
            f"'{self.sort.text()}',"\
            f"'{self.value.text()}',"\
            f"'{self.form.text()}',"\
            f"'{self.taste.text()}',"\
            f"{int(self.price.text())},"\
            f"{int(self.volume.text())}"\
             ")"
        print(que)
        cur.execute(que)
        self.con.commit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())