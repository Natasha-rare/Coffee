import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.params = {'id': 'id', 'сорт': 'сорт', 'степень обжарки': 'степень обжарки',
                       'форма': 'форма', 'вкус': 'вкус', 'цена': 'цена', 'объем упаковки': 'объем упаковки'}
        self.con = sqlite3.connect("coffee.db")
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.comboBox.addItems(list(self.params.keys()))
        self.save.clicked.connect(self.save_results)
        self.modified = {}
        self.load.clicked.connect(self.load_result)
        self.titles = None
        self.tableWidget.setColumnCount(7)
        head = []
        for i in range(7):
            head.append(self.con.cursor().execute("SELECT * FROM Coffee").description[i][0])
        self.tableWidget.setHorizontalHeaderLabels(head)

    def load_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        req = "SELECT * FROM Coffee WHERE {} = {}".format(self.params.get(self.comboBox.currentText()),
                                                         self.lineEdit.text())
        if ("LIKE" in self.lineEdit.text().upper() or "BETWEEN" in self.lineEdit.text().upper() or
                "IN" in self.lineEdit.text().upper() or
                '<' in self.lineEdit.text() or '>' in self.lineEdit.text()):
            req = f"SELECT * FROM Coffee WHERE {self.params.get(self.comboBox.currentText())} {self.lineEdit.text()}"
        result = cur.execute(req).fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE Coffee SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += f"WHERE {self.params.get(self.comboBox.currentText())} = {self.lineEdit.text()}"
            cur.execute(que)
            self.con.commit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())