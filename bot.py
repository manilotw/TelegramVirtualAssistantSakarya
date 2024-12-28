from telebot import TeleBot
import os
import sys
from environs import Env

from helpers import start_keyboard, back_keyboard
from chatgpt import get_chatgpt_response


env = Env()
env.read_env()

bot = TeleBot(env.str('BOT_TOKEN'))

def main():

    @bot.message_handler(commands=['start'])
    def send(message):
        keyboard = start_keyboard(message)
        bot.reply_to(message, 'Здравствуйте! Здесь должно быть описание!',reply_markup = keyboard)

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message, 'Здесь будет информация о командах.')

    @bot.message_handler(func=lambda message: message.text == 'Чат с ИИ')
    def send_ai(message):
        bot.reply_to(message, 'Начинайте чат', reply_markup=back_keyboard(message))

        @bot.message_handler(func=lambda m: m.chat.id == message.chat.id)  
        def chat_with_ai(user_message):
            answer = get_chatgpt_response(user_message.text)  
            bot.send_message(user_message.chat.id, answer)  

    @bot.message_handler(func=lambda message: message.text == 'Вернуться назад')
    def send_back(message):
        send(message)

    @bot.message_handler(func=lambda message: message.text == 'Связаться с поддержкой')
    def send_support(message):
        bot.reply_to(message, 'На данный момент эта функция не доступна', reply_markup = back_keyboard(message))
        
    @bot.message_handler(func=lambda message: message.text == 'Написать жалобу')
    def send_complain(message):
        bot.reply_to(message, 'На данный момент эта функция не доступна', reply_markup = back_keyboard(message))

    @bot.message_handler(func=lambda message: message.text == 'Больше о проекте')
    def send_about_project(message):
        bot.reply_to(message, 'На данный момент эта функция не доступна', reply_markup = back_keyboard(message))

    @bot.message_handler(func=lambda message: message.text == 'Найти на сайте')
    def send_find(message):
        bot.reply_to(message, 'На данный момент эта функция не доступна', reply_markup = back_keyboard(message))

    @bot.message_handler(func=lambda message: message.text == 'F.A.Q')
    def send_faq(message):
        bot.reply_to(message, 'На данный момент эта функция не доступна', reply_markup = back_keyboard(message))

if __name__ == "__main__":
    main()
    print("Бот запущен")
    bot.polling()