import sqlite3
import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 481, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(30, 50, 481, 31))
        self.load.setObjectName("load")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(30, 90, 481, 31))
        self.change_btn.setObjectName("change_btn")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 11, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 10, 371, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
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
        self.load.setText(_translate("MainWindow", "Загрузить"))
        self.change_btn.setText(_translate("MainWindow", "Изменить"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(523, 419)
        self.textBrowser_4 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(30, 120, 121, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 80, 121, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 121, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 160, 121, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 200, 121, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.change_btn = QtWidgets.QPushButton(Form)
        self.change_btn.setGeometry(QtCore.QRect(410, 40, 75, 81))
        self.change_btn.setObjectName("change_btn")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 240, 121, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(410, 130, 75, 81))
        self.add.setObjectName("add")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 0, 121, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.id = QtWidgets.QLineEdit(Form)
        self.id.setGeometry(QtCore.QRect(180, 0, 191, 31))
        self.id.setObjectName("id")
        self.sort = QtWidgets.QLineEdit(Form)
        self.sort.setGeometry(QtCore.QRect(180, 40, 191, 31))
        self.sort.setObjectName("sort")
        self.value = QtWidgets.QLineEdit(Form)
        self.value.setGeometry(QtCore.QRect(180, 80, 191, 31))
        self.value.setObjectName("value")
        self.form = QtWidgets.QLineEdit(Form)
        self.form.setGeometry(QtCore.QRect(180, 120, 191, 31))
        self.form.setObjectName("form")
        self.taste = QtWidgets.QLineEdit(Form)
        self.taste.setGeometry(QtCore.QRect(180, 160, 191, 31))
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setGeometry(QtCore.QRect(180, 200, 191, 31))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(Form)
        self.volume.setGeometry(QtCore.QRect(180, 240, 191, 31))
        self.volume.setObjectName("volume")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Форма</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Сепень обжарки</p></body></html>"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Сорт</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Вкус</p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Цена</p></body></html>"))
        self.change_btn.setText(_translate("Form", "Изменить"))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Объем упаковки</p></body></html>"))
        self.add.setText(_translate("Form", "Добавить"))
        self.textBrowser_8.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">id</p></body></html>"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.params = ['id', 'сорт', 'степень обжарки',
                       'форма', 'вкус', 'цена', 'объем упаковки']
        self.con = sqlite3.connect("data/coffee.db")
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


class Changing(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.add_new)
        self.change_btn.clicked.connect(self.change)
        self.show()
        self.con = sqlite3.connect("data/coffee.db")
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
        cur.execute(que)
        self.con.commit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())