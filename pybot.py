import time
import requests
import telebot
import random
import json
import lib_for_tele
from telebot import types
emote = random.randint(1,4)
tr = 1
api = '3d9de74844d28377e81415151cbe6a66'
bot = telebot.TeleBot('7659043896:AAElYsiYcdI-_GJaNPV-jcri5nCK74UH4T4') #!!!!!чтобы проверить, пожалуйста, не испоьзуйте этот токен, так как он рабочий, настроен на бота для проекта, создайте своего бота в бот фазер
words = ['apple', 'beach', 'carry', 'dance', 'dress', 'event', 'field', 'glass', 'happy', 'money', 'crack', 'laugh',
         'magic', 'ocean', 'penny']
user_games = {}
def fil(message):
    with open(f'{message.chat.id}.txt','w') as file:
        pass
callb = None
nik = "123"
@bot.message_handler(commands=['start'])
def startcomm(message):
    global emote, nik,tr
    nik = message.from_user.first_name
    with open('niks.txt','w') as file:
        file.write(f"{nik}|{message.chat.id}")
    if tr == 1:
        bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} зашел в бота')
    fil(message)
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("Шаблон класса", callback_data="class")
    b2 = types.InlineKeyboardButton("Конвертер", url="https://www.programiz.com/online-compiler/5eYXDlZHv8Gru")
    b3 = types.InlineKeyboardButton("Создать класс", url='https://www.programiz.com/online-compiler/5eYXDlZHv8Gru')
    b4 = types.InlineKeyboardButton("Игры", callback_data="play")
    b5 = types.InlineKeyboardButton("Узнать температуру в городе", callback_data="temp")
    b6 = types.InlineKeyboardButton("Заметки", callback_data="notes")
    markup.add(b2, b1, b3, b4, b5, b6)
    if emote == 1:
        bot.reply_to(message, f'Здравствуй, {message.from_user.first_name}!', reply_markup=markup)
    elif emote == 2:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}', reply_markup=markup)
    elif emote == 3:
        bot.reply_to(message, f'Ну привет, {message.from_user.first_name}', reply_markup=markup)
    elif emote == 4:
        bot.reply_to(message, f'Приветики, {message.from_user.first_name}!', reply_markup=markup)

target = ''
x = 0
y = 0
field = []
res_n = None
def notes_us(message):
    global nik,tr
    if tr == 1:
        bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} открыл меню заметки')
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("Добавить заметку", callback_data="add_n")
    b2 = types.InlineKeyboardButton("Открыть заметки", callback_data="open_n")
    b3 = types.InlineKeyboardButton("Удалить заметку №", callback_data="del")
    markup.add(b1,b2,b3)
    bot.send_message(message.chat.id, 'Ваши заметки', reply_markup=markup)
def delete_note(message):
    global nik, tr
    if message.text != 'Ваши заметки':
        with open(f'{message.chat.id}.txt', 'r', encoding='utf-8') as file:
            a = None
            a = list(''.join(file.readlines()).split('|'))
            print(a)
            b = (a[0].split('|'))
            c = []
            wh = int(message.text.lower())+1
            if wh <= len(b)-1:
                b.pop(wh)
            else:
                a.pop(wh-len(b))
            for i in b:
                c.append(i)
            for i in a[1:]:
                c.append(i)
        while c.count('') != 0:
            c.pop(c.index(''))
        with open(f'{message.chat.id}.txt', 'w+', encoding='utf-8') as file:
            file.write(f'|{"|".join(c)}')
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} удалил заметку')
        notes_us(message)
def notes_open(message):
    global nik, tr
    if tr == 1:
        bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} открыл свои заметки')
    res_no = None
    bot.send_message(message.chat.id,message.chat.id)
    try:
        with open(f'{message.chat.id}.txt', 'r', encoding='utf-8') as file:
            a = None
            a = list(''.join(file.readlines()).split('|'))
    except Exception:
        a = None
        with open(f'{message.chat.id}.txt', 'w', encoding='utf-8') as file:
            print(1)
    print(a)
    b = '\n\n'.join(a[0].split('|'))
    c = []
    for i in b:
        c.append(f"№{b.index(i)}\n{i}")
    for i in a[1:]:
        c.append(f"№{len(b) + a.index(i)}\n{i}")
    res_no = '\n\n'.join(c)
    bot.send_message(message.chat.id, res_no)
    notes_us(message)
res_no = None
def notes_add(message):
    global nik, tr

    a = []
    if message.text != 'Ваши заметки':
        try:
            with open(f'{message.chat.id}.txt', 'r', encoding='utf-8') as file:
                a = None
                a = list(''.join(file.readlines()).split('|'))
            with open(f'{message.chat.id}.txt', 'w', encoding='utf-8') as file:
                a.append(message.text)
                file.write('|'.join(a))
        except Exception:
            a = []
            with open(f'{message.chat.id}.txt', 'w', encoding='utf-8') as file:
                file.write("|")
                a.append(message.text)
                file.write('|'.join(a))
        print(a)
        b = '\n\n'.join(a[0].split('|'))
        c = []
        for i in b:
            c.append(f"№{b.index(i)}\n{i}")
        for i in a[1:]:
            c.append(f"№{len(b)+a.index(i)}\n{i}")
        res_n = '\n\n'.join(c)
        bot.send_message(message.chat.id, "Заметка успешно добавлена!")
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} добавил заметку')
        notes_us(message)
def playgames(message):
    global nik, tr
    if tr == 1:
        bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} зашел в меню игры')
    markup = types.InlineKeyboardMarkup()
    c1 = types.InlineKeyboardButton("Камень-ножницы-бумага", callback_data="anim")
    c2 = types.InlineKeyboardButton("Верный ответ", callback_data="correct")
    c3 = types.InlineKeyboardButton("5 букв", callback_data="letters5")
    c4 = types.InlineKeyboardButton("Больше-Меньше", callback_data="mm")
    c5 = types.InlineKeyboardButton("Игра в слова", callback_data='words_game')
    markup.add(c2, c4, c3, c1, c5)
    bot.send_message(message.chat.id, "Выбор мини-игр:", reply_markup=markup)

def talk(message):
    us = message.text.lower()
    hi = ['Привет!',"Здравствуйте!","Рад приветствовать вас!","Доброго времени суток!","Здравствуйте, я бот для мини-игр и небольшой консультации в питоне","Приветствую, меня зовут PYBOT, или Паша, рад знакомству"]
    if us == "привет" or us == "пивет" or us == "приве" or us == "пр" or us == "здрасьте" or us == "здравствуйте" or us == "здраствуйте" or us == "хай":
        bot.send_message(message.chat.id, random.choice(hi))


@bot.callback_query_handler(func=lambda callback: True)
def callb(callback):
    global callb, wh
    if callback.data == "play":
        playgames(callback.message)
    elif callback.data == 'notes':
        notes_us(callback.message)
    elif callback.data == 'open_n':
        notes_open(callback.message)
    elif callback.data == 'add_n':
        callb = 'notes_add'
        handle_message(callback.message)
    elif callback.data == 'del':
        callb = 'del'
        handle_message(callback.message)
    elif callback.data == "w":
        wh = 1

    elif callback.data == "a":
        wh = 2

    elif callback.data == "s":
        wh = 3
    elif callback.data == "d":
        wh = 4
    elif callback.data == "class":
        with open(r'Mironenko/lib_for_tele/classhelp.py', 'r', encoding='utf-8') as file:
            o = ['class example():\n', '    def __init__(self):\n', '        first = input()   # это - переменная, она используется только в рамках этой функции\n', '        self.a = first   # это - переменная класса, она может использоваться везде\n', '        self.b = input()   # это тоже переменная класса\n', '        self.__c = 1   # это - закрытая переменная, ее можно достаь ТОЛЬКО через геттер и устуновить ТОЛЬКО через сеттер\n', '    def first_method(self):   # это - метод (подфункция)\n', '        print(self.a)   # выводим нашу переменную класса\n', '    def second_method(self):\n', '        print(self.b)\n', '    def setter(self, q):   # это и есть тот самый сеттер\n', '        self.__c = q\n', '    def getter(self):   # а это - геттер\n', '        return self.__c\n', 'object = example()   # создаем объект класса\n', 'print(object.b)   # достаем переменную класса\n', 'print(object.getter())   # достаем закрытую переменную класса\n', 'object.setter(3)      # назначаем закрытую переменную класса\n', 'print(object.getter())\n']
            bot.send_message(callback.message.chat.id, ''.join(o))
    elif callback.data == 'letters5':
        start_new_game(callback.message)
        callb = 'letters5'
        print(str(f'{callback.message.text.lower()}'))
    elif callback.data == 'words_game':
        callb = 'words_g'
        bot.send_message(callback.message.chat.id,
                         'Это игра в слова, пишите свое слово, а я вам буду писать свое, на последнюю букву вашего, и наоборот')
        handle_message(callback.message)
    elif callback.data == '' or callback.data == None:
        callb = ''
        talk(callback.message)
    elif callback.data == 'temp':
        callb = 'temp'
        bot.send_message(callback.message.chat.id, "Напишити на английском название города, в котором вы хотите узнать погоду")

        handle_message(callback.message)
    elif callback.data =="correct":
        callb = 'correct'
        handle_message(callback.message)
    elif callback.data =="mm":
        callb = 'mm'
        handle_message(callback.message)
    elif callback.data == 'anim':
        anim(callback.message)
res = None


@bot.message_handler()
def handle_message(message):
    global callb, res,tr,nik
    if callb == 'letters5':
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} начал игру 5 букв')
        process_guess(message)
    elif callb == 'del':
        delete_note(message)
    elif callb == 'notes_add':
        notes_add(message)
    elif callb == 'correct':
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} начал игру верный ответ')
        lib_for_tele.corrrect_a.correct(message)
    elif callb == 'mm':
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} начал игру больше-меньше')
        lib_for_tele.usanwser.us_anws(message)
    elif callb == "words_g":
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} начал игру слова')
        lib_for_tele.words.word(message)
    elif callb == 'temp':
        city = message.text.lower().capitalize()
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
        data = json.loads(res.text)
        temp = (f'Сейчас температура около {data["main"]["temp"]} градусов цельсия\n'
                f'Ощущается как {data["main"]["feels_like"]}\n'
                f'Скорость ветра - {data["wind"]["speed"]} метров в секунду')
        bot.send_message(message.chat.id, temp)
        if tr == 1:
            bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} узнал температуру города {city}')
    else:
        calendar(message)
        #talk(message)

def calendar(message):
    pass

def start_new_game(message):
    global nik, tr
    if tr == 1:
        bot.send_message(-1002637625997,f'Пользователь с id {message.chat.id}, ник {nik} зашел в игру 5 букв')
    user_id = message.chat.id
    user_games[user_id] = {
        'secret_word': random.choice(words),
        'attempts': 0
    }
    bot.send_message(message.chat.id,
                     'Начнём игру "Пять букв"!')
    time.sleep(2)
    bot.send_message(message.chat.id, 'У вас есть шесть попыток, чтобы отгадать случайное английское слово из пяти букв')
    time.sleep(3)
    bot.send_message(message.chat.id, 'Вы должны вводить свое английское слово, содержащее тоже пять букв')
    time.sleep(3)
    bot.send_message(message.chat.id, "После чего я вам отвечу, сколько у вас верных букв")
    time.sleep(2)
    bot.send_message(message.chat.id, "0 под пуквой означает, что в загаданном слове такой буквы нет,\n1 - то, что эта буква есть в слове, но стоит не на своем месте,\n2 значит, что буква есть в слове и стоит на своем месте,\nПЯТЬ ДВОЕК = ПОБЕДА")
def process_guess(message):
    user_id = message.chat.id
    game_state = user_games.get(user_id)

    if not game_state:
        return

    guess = message.text.lower()
    if len(guess) != 5:
        bot.send_message(message.chat.id, 'Ваше слово должно содержать ровно пять букв. Попробуйте ещё раз.')
        return

    result = ''
    for i in range(len(game_state['secret_word'])):
        if guess[i] == game_state['secret_word'][i]:
            result += '2'
        elif guess[i] in game_state['secret_word']:
            result += '1'
        else:
            result += '0'

    bot.send_message(message.chat.id, f'{message.text.lower()}\n{result}')
    game_state['attempts'] += 1

    if result == '22222':
        bot.send_message(message.chat.id, f'Ура! Вы угадали слово: {game_state["secret_word"]}')
        del user_games[user_id]
    elif game_state['attempts'] >= 6:
        bot.send_message(message.chat.id,
                         f'К сожалению, вы использовали все попытки. Загаданное слово было: {game_state["secret_word"]}')
        del user_games[user_id]
    else:
        bot.send_message(message.chat.id, f'Осталось попыток: {6 - game_state["attempts"]}')
x = 0
y = 0
filedqq = []
tick = 0
wha = 0
wh = 0
def anim(message):
    global nik, tr
    if tr == 1:
        bot.send_message(-1002637625997, f'Пользователь с id {message.chat.id}, ник {nik} включил anim')
    global x, y, fieldqq, tick, wha, wh
    if wha == 0:
        filed = filedqq
        wha = 1
        for i in range(10):
            field.append(['⬜️'] * 10)
        x, y = random.randint(0, 9), random.randint(0, 9)
        field[y][x] = '🚶'
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("w", callback_data="w")
    b2 = types.InlineKeyboardButton("a", callback_data="a")
    b3 = types.InlineKeyboardButton("s", callback_data="s")
    b4 = types.InlineKeyboardButton("d", callback_data="d")
    markup.row(b1)
    markup.add(b2, b3, b4)
    while True:
        a = 1
        if a == 1:
            xr = 1
            yr = random.randint(1, 9)
            field[yr][1] = '🔳'
            time.sleep(2)
            while xr != 9:
                e = random.randint(1, 4)
                if wh == 2:
                    field[y][x] = '⬜️'
                    x -= 1
                    field[y][x] = '🚶'
                    wh = 2
                elif wh == 4:
                    field[y][x] = '⬜️'
                    x += 1
                    field[y][x] = '🚶‍➡️'
                    wh = 4
                elif wh == 1:
                    field[y][x] = '⬜️'
                    y -= 1
                    wh = 0
                    field[y][x] = '🚶'
                elif wh == 3:
                    field[y][x] = '⬜️'
                    y += 1
                    field[y][x] = '🚶'
                    wh = 3
                time.sleep(1)
                field[yr][xr] = '⬜️'
                xr += 1
                field[yr][xr] = '🔳'
                bot.edit_message_text("\n".join(map(" ".join, field)),message.chat.id,message.message_id, reply_markup=markup)
            field[yr][xr] = '⬜️'

bot.infinity_polling()