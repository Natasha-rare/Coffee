import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
import sqlite3

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.params = {"Год выпуска": "year", "Название": "title", "Продолжительность": "duration"}
        self.comboBox.addItems(list(self.params.keys()))
        self.con = sqlite3.connect("films.db")
        self.pushButton.clicked.connect(self.select)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)
        head = []
        for i in range(5):
            head.append(self.con.cursor().execute("SELECT * FROM Films").description[i][0])
        self.tableWidget.setHorizontalHeaderLabels(head)

    def select(self):
        req = "SELECT * FROM Films WHERE {} = {}".format(self.params.get(self.comboBox.currentText()),
                                                         self.lineEdit.text())
        cur = self.con.cursor()
        if ("LIKE" in self.lineEdit.text() or "BETWEEN" in self.lineEdit.text() or "IN" in self.lineEdit.text() or
                '<' in self.lineEdit.text() or '>' in self.lineEdit.text()):
            req = f"SELECT * FROM Films WHERE {self.params.get(self.comboBox.currentText())} {self.lineEdit.text()}"
        result = cur.execute(req).fetchone()
        for i, val in enumerate(result):
            self.tableWidget.setItem(0, i, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())