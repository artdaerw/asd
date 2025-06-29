import telebot
import random

bot = telebot.TeleBot('7659043896:AAElYsiYcdI-_GJaNPV-jcri5nCK74UH4T4') #!!!!!чтобы проверить, пожалуйста, не испоьзуйте этот токен, так как он рабочий, настроен на бота для проекта, создайте своего бота в бот фазер

target = ''
field = []
def correct(message):
    global target, x,y, field, callb
    if message.text.lower().count(',') != 0:
        x, y = message.text.lower().split(',')
        print(123)
    else:
        x = 0
        y = 0
        targets = ['🧑', '😕', '🌇', '🌥', '👭', '😫']
        others = ['👨', '🙁', '🌆', '⛅️', '👫', '😩']
        target = random.choice(targets)
        other = others[targets.index(target)]
        field = []
        for i in range(10):
            field.append([other] * 10)
        tx, ty = random.randint(0, 9), random.randint(0, 9)
        field[ty][tx] = target
        print(field)
        bot.send_message(message.chat.id, 'Это игра "Найди лишний"!\nЯ присылаю вам поле 10х10,\nа вы должны найти выделяющегося смайлика,\nприслать мне его координаты в формате Х(1-10),У(1-10)!')
        bot.send_message(message.chat.id, f'{"\n".join(map(" ".join, field))}\n\n\nобычные смайлики - {other}\nцель - {target}')
    if field[10-int(y)][int(x)-1] == target:
        bot.send_message(message.chat.id, f"Попадание! Цель была на ({x},{y})")
    else:
        bot.send_message(message.chat.id, f"Нет цели на ({x},{y}), продолжаем искать...")