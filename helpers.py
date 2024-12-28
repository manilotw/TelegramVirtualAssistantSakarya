from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def start_keyboard(message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = KeyboardButton('Чат с ИИ')
    btn2 = KeyboardButton('Связаться с поддержкой')
    btn3 = KeyboardButton('Написать жалобу')
    btn4 = KeyboardButton('Добавить предложение')
    btn5 = KeyboardButton('Больше о проекте')
    btn6 = KeyboardButton('Найти на сайте')
    btn7 = KeyboardButton('F.A.Q')


    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    return keyboard

def back_keyboard(message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = KeyboardButton('Вернуться назад')

    keyboard.add(btn1)

    return keyboard