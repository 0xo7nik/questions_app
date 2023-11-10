from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from random import randint, shuffle
from time import sleep
import json


questions = {}
with open('b.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

def set_new_questions():
    global questions, buttons, question
    headers = list(questions.keys())
    text_question = headers[randint(0, len(headers) - 1)]
    question.setText(text_question)
    answers = list(questions[text_question])
    new_answers = answers.copy()
    shuffle(new_answers)
    for i in range(4):
        buttons[i].setText(new_answers[i])
        if new_answers[i] == answers[0]:
            buttons[i].isTrue = True
        else:
            buttons[i].isTrue = False
            
def check_answer():
    global buttons, question, dlg, btn_dlg, btn_dlg1, v
    answer12 = QLabel()
    answer12.setFont(QFont('Arial', 20))
    correct_answer = False
    btn_dlg = QPushButton()
    btn_dlg1 = QPushButton()
    btn_dlg.setFont(QFont('Arial', 14))
    btn_dlg1.setFont(QFont('Arial', 14))
    v = QVBoxLayout()
    for button in buttons:
        if button.isChecked() and button.isTrue:
            correct_answer = True
    if correct_answer:
        answer12.setText('Правильно!')
        answer12.setStyleSheet('color: rgb(17, 186, 53);'
                                        'font: bold italic 20pt "Arial";'
                                        )
        btn_dlg.setText('Следущий вопрос')
        btn_dlg1.hide()
    else:
        answer12.setText('Неправильно!')
        answer12.setStyleSheet('color: rgb(168, 10, 29);'
                                        'font: bold italic 20pt "Arial";'
                                        )
        btn_dlg1.setText('Заново')
        btn_dlg.hide()
    dlg = QDialog()
    dlg.resize(200, 100)
    dlg.setWindowTitle("Ответ")
    dlg.setLayout(v)
    btn_dlg.clicked.connect(next_question)
    btn_dlg1.clicked.connect(previous_question)
    v.addWidget(answer12, alignment=Qt.AlignCenter)
    v.addWidget(btn_dlg, alignment=Qt.AlignBottom)
    v.addWidget(btn_dlg1, alignment=Qt.AlignBottom)
    dlg.show()
    dlg.exec()

def next_question():
    dlg.close()
    set_new_questions()

def previous_question():
    dlg.close()

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Вопросы')
mw.resize(700, 500)

vert_main = QVBoxLayout()
question = QLabel('Вопрос!')
question.setFont(QFont('Arial', 20))

group = QGroupBox('Варианты ответов')
group.setFont(QFont('Arial', 14))

h = QHBoxLayout()
h_group = QHBoxLayout()
l_v_group = QVBoxLayout()
r_v_group = QVBoxLayout()

buttons = [
    QRadioButton('Ответ 1'),
    QRadioButton('Ответ 2'),
    QRadioButton('Ответ 3'),
    QRadioButton('Ответ 4'),
]

l_v_group.addWidget(buttons[0])
l_v_group.addWidget(buttons[1])
r_v_group.addWidget(buttons[2])
r_v_group.addWidget(buttons[3])

h_group.addLayout(l_v_group)
h_group.addLayout(r_v_group)
group.setLayout(h_group)

button = QPushButton('Ответить!')
button.clicked.connect(check_answer)
button.setFont(QFont('Arial', 12))

vert_main.addWidget(question, alignment=Qt.AlignCenter)
vert_main.addWidget(group)
vert_main.addWidget(button)

set_new_questions()

mw.setLayout(vert_main)
mw.show()
app.exec_()
