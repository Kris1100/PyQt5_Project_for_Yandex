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
        self.timer = QTimer()
        self.timer1 = QTimer()
        self.timer2 = QTimer()
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
            self.label_3.setText('Прошло:')
            help_for_now = time.asctime().split()[3]
            self.now = int(help_for_now.split(':')[0]) * 3600 + int(help_for_now.split(':')[1]) * 60 + int(
                help_for_now.split(':')[2])
            self.timer1.timeout.connect(self.how_much)
            self.timer1.start(60)

        if okBtnPressed and i == 'Часы':
            self.label_3.setText('')
            self.label_2.setText('')
            self.timer1.stop()
            self.timer2.stop()


    def how_much(self):
        help_for_now = int(time.asctime().split()[3].split(':')[0]) * 3600 + int(
            time.asctime().split()[3].split(':')[1]) * 60 + int(time.asctime().split()[3].split(':')[2])
        self.label_2.setText(str(help_for_now - self.now))

    def timeit(self):
        help_for_now = int(time.asctime().split()[3].split(':')[0]) * 3600 + int(
            time.asctime().split()[3].split(':')[1]) * 60 + int(time.asctime().split()[3].split(':')[2])
        k = str(self.i - (help_for_now - self.now))
        self.label_2.setText(k)
        if k <= '0':
            self.timer2.stop()
            self.w.show()




app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())