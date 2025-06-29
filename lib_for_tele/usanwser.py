import telebot
import random

bot = telebot.TeleBot('7659043896:AAElYsiYcdI-_GJaNPV-jcri5nCK74UH4T4') #!!!!!чтобы проверить, пожалуйста, не испоьзуйте этот токен, так как он рабочий, настроен на бота для проекта, создайте своего бота в бот фазер
b = 0
a = 0
r = 0
def us_anws(message):
    global b,a,r
    if b == 0:
        r = 0
        b = random.randint(1, 100)
        bot.send_message(message.chat.id, "🎲")
        bot.send_message(message.chat.id, "я загадал число от 1 до 100, предлагайте свои варианты!")
    if a == message.text.lower():
        us_anws(message)
    a = message.text.lower()
    if int(a) > b:
        bot.send_message(message.chat.id, "у тебя число больше, чем у меня")
        r += 1
        us_anws(message)

    elif int(a) < b:
        bot.send_message(message.chat.id, "у тебя число меньше, чем у меня")
        r += 1
        us_anws(message)
    elif int(a) == b:
        b = 0
        bot.send_message(message.chat.id, f"Ты угадал!!! Потратив на это {r+1} попытки")