from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QTimer
from ui_file import Clocks
from Timeout import Ui_Form
import time
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtWidgets import QInputDialog


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWidget(QMainWindow, Clocks):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_6.hide()
        self.pushButton_7.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.checkBox_2.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.timer = QTimer()
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.timer3 = QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(60)
        self.pushButton.clicked.connect(self.choose_else)
        self.w = Example()

    def run(self):
        self.label.setText(time.asctime().split()[3])

    def choose_else(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выбрать другое",
            "Выбрите",
            ("Часы", "Секундомер", "Таймер"),
            0,
            False
        )
        if okBtnPressed and i == 'Таймер':
            self.checkBox_2.show()
            self.label_5.show()
            self.pushButton_5.show()
            self.pushButton_6.show()
            self.pushButton_7.show()
            if not self.checkBox.isChecked():
                self.label_4.hide()
                self.checkBox.hide()
                self.pushButton_2.hide()
                self.pushButton_3.hide()
                self.pushButton_4.hide()
            self.timer1.stop()
            self.label_3.setText('Осталось:')
            i, okBtnPressed = QInputDialog.getInt(
                self, "Время", "Введите время в секундах", 5, 0, 216000, 1
            )
            self.i = i
            help_for_now = time.asctime().split()[3]
            self.now = int(help_for_now.split(':')[0]) * 3600 + int(help_for_now.split(':')[1]) * 60 + int(
                help_for_now.split(':')[2])
            self.timer2.timeout.connect(self.timeit)
            self.timer2.start(60)

        if okBtnPressed and i == 'Секундомер':
            self.timer2.stop()
            self.label_4.show()
            self.checkBox.show()
            self.pushButton_2.show()
            self.pushButton_3.show()
            self.pushButton_4.show()
            self.label_3.setText('Прошло:')
            if not self.checkBox_2.isChecked():
                self.label_5.hide()
                self.checkBox_2.hide()
                self.pushButton_5.hide()
                self.pushButton_6.hide()
                self.pushButton_7.hide()
            else:
                self.timer3.timeout.connect(self.timeitwithsec)
                self.timer3.start(60)
            self.help_for_now1 = time.asctime().split()[3]
            if self.checkBox.isChecked():
                self.timer1.stop()
            else:
                self.now1 = int(self.help_for_now1.split(':')[0]) * 3600 + int(self.help_for_now1.split(':')[1]) * 60 + int(
                    self.help_for_now1.split(':')[2])
            self.timer1.timeout.connect(self.how_much)
            self.timer1.start(60)


        if okBtnPressed and i == 'Часы':
            if not self.checkBox_2.isChecked():
                self.label_5.hide()
                self.checkBox_2.hide()
            if not self.checkBox.isChecked():
                self.label_4.hide()
                self.checkBox.hide()
            self.label_3.setText('')
            self.label_2.setText('')
            self.timer2.stop()
            self.timer1.stop()

    def how_much(self):
        help_for_now1 = int(time.asctime().split()[3].split(':')[0]) * 3600 + int(
            time.asctime().split()[3].split(':')[1]) * 60 + int(time.asctime().split()[3].split(':')[2])
        self.pushButton_2.clicked.connect(self.t1)
        self.pushButton_3.clicked.connect(self.t1)
        self.pushButton_4.clicked.connect(self.t1)
        self.label_2.setText(str(help_for_now1 - self.now1))

    def t1(self):
        help_for_now1 = time.asctime().split()[3]
        self.now1 = int(help_for_now1.split(':')[0]) * 3600 + int(help_for_now1.split(':')[1]) * 60 + int(
                    help_for_now1.split(':')[2])



    def timeit(self):
        help_for_now = int(time.asctime().split()[3].split(':')[0]) * 3600 + int(
            time.asctime().split()[3].split(':')[1]) * 60 + int(time.asctime().split()[3].split(':')[2])
        k = str(self.i - (help_for_now - self.now))
        self.label_2.setText(k)
        if k <= '0':
            self.timer2.stop()
            self.w.show()

    def timeitwithsec(self):
        help_for_now = int(time.asctime().split()[3].split(':')[0]) * 3600 + int(
            time.asctime().split()[3].split(':')[1]) * 60 + int(time.asctime().split()[3].split(':')[2])
        k = str(self.i - (help_for_now - self.now))
        if k <= '0':
            self.timer3.stop()
            self.w.show()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
