import logging
from xml.sax.saxutils import prepare_input_source

from pywebio.input import input as pw_input
from pywebio.input import PASSWORD as PW_PASSWORD
from pywebio.output import put_text, put_error, put_success, put_markdown

welcome = 'Дякуємо що вирішили зайти на нашу вікторину!'

put_text(welcome)

login = pw_input(label='Введіть свій логін')
password = pw_input(label='Введіть свій пароль', type=PW_PASSWORD)
password2 = pw_input(label='будь-ласка повторіть пароль', type=PW_PASSWORD, required=True,)

if password == password2:
    put_success('Вітаємо!')
else:
    put_error('Паролі не співпадають. Спробуйте ще раз.')

score = 0
total_questions = 5

planet_question = pw_input(label='Яка найбільша планета у сонячній системі?', required=True)
planet = 'Юпітер'
planet_question = planet_question.title()

if planet_question == planet:
    put_success('Правильно!')
    score += 1
else:
    put_error('Помилка!')

earth_question = pw_input(label='Скільк континентів на землі?', required=True)
earth = '7'

if earth_question == earth:
    put_success('Правильно!')
    score += 1
else:
    put_error('Помилка!')

france_question = pw_input(label='Як називаєтся столиця Франції?', required=True)
france = 'Париж'
france_question = france_question.title()

if france_question == france:
    put_success('Правильно!')
    score += 1
else:
    put_error('Помилка!')

metal_question = pw_input(label='Який метал є основним у виробництві алюмінієвої фольги?', required=True)
metal = 'Алюміній'
metal_question = metal_question.title()

if metal_question == metal:
    put_success('Правильно!')
    score += 1
else:
    put_error('Помилка!')

rainbow_question = pw_input(label='Скільки кольорів у веселці?', required=True)
rainbow = '7'

if rainbow_question == rainbow:
    put_success('Правильно!')
    score += 1
else:
    put_error('Помилка!')

percentage =(score / total_questions) * 100

put_markdown(f"# Вікторина завершена! Ваш рахунок: {score} з {total_questions} ({percentage:.2f}%).")