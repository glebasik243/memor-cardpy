
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox

from random import shuffle
# answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
# shuffle(answers)


app =  QApplication([])
main_win = QWidget()
main_win.setWindowTitle('memory card')
RadioGroupBox = QGroupBox("Варианты ответов")






question =  QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
button2 = QPushButton('Следующий вопрос')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')

layout_main = QVBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


layout_main.addWidget(question)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(button)


main_win.setLayout(layout_main)
main_win.show()
app.exec_()