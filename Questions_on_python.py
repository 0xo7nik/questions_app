import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from random import randint, shuffle
from time import sleep


questions = {
    'В каком году был создан язык программирования Python?': ('1990', '1984', '2007', '2016'),
    'Кто был основателем языка Python?': ('Гвидо ван Россум', 'Киану Ривз', 'Сунь-цзы', 'Андрей Черников'),
    'Что такое GitHub?': ('Сайт', 'Игра', 'Мессенджер', 'Соц. сеть'),
    'Что такое Visual Studio Code?': ('Редактор кода', 'Блокнот', 'Приложение', 'Игра'),
    'Что такое диспетчер задач в Windows?': ('Менеджер программ', 'Вирус', 'Редактор кода', 'Антивирус')
}
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
    global buttons, question
    answer12 = QLabel()
    answer12.setFont(QFont('Arial', 20))
    correct_answer = False
    for button in buttons:
        if button.isChecked() and button.isTrue:
            correct_answer = True
    if correct_answer:
        answer12.setText('Правильно!')
        answer12.setStyleSheet('color: rgb(17, 186, 53);'
                                        'font: bold italic 20pt "Arial";'
                                        )
    else:
        answer12.setText('Неправильно!')
        answer12.setStyleSheet('color: rgb(168, 10, 29);'
                                        'font: bold italic 20pt "Arial";'
                                        )
    dlg = QDialog()
    dlg.resize(200, 100)
    dlg.setWindowTitle("Ответ")
    dlg.setLayout(v)
    v.addWidget(answer12, alignment=Qt.AlignCenter)
    h.addWidget(dlg_btn, alignment=Qt.AlignBottom)
    dlg.exec_()

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Вопросы')
mw.resize(700, 500)

vert_main = QVBoxLayout()
question = QLabel('Вопрос!')
question.setFont(QFont('Arial', 20))

group = QGroupBox('Варианты ответов')
group.setFont(QFont('Arial', 14))

v = QVBoxLayout()
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

dlg_btn = QDialogButtonBox()
dlg_btn.setFont(QFont('Arial', 12))

vert_main.addWidget(question, alignment=Qt.AlignCenter)
vert_main.addWidget(group)
vert_main.addWidget(button)

set_new_questions()

mw.setLayout(vert_main)
mw.show()
app.exec_()
