import threading

import time
import telebot
import random
from telebot import types

bot = telebot.TeleBot('7659043896:AAElYsiYcdI-_GJaNPV-jcri5nCK74UH4T4') #!!!!!чтобы проверить, пожалуйста, не испоьзуйте этот токен, так как он рабочий, настроен на бота для проекта, создайте своего бота в бот фазер


s = 0
p = 0
en = 50
global schTr, unTr, bal, det, pos
det = 0
bal = 550
schTr = False
unTr = False
bc = ["🔓"]
b = 0
c1 = 0
running = True
run = False
pos = 1
tc = ["🔒","🔒","🔒",]
bc = ["ТЦ","ТРЦ"]


def un():
    global bal
    if schTr == False:
        print("Вы не закончили школу!!!")
    else:
        print(f"На институт вам нужны деньги, а именно 1000 монет, списать? Ваш баланс после списания будет {bal - 1000}. Нажмите y усли согласны.")
        if input() == 'y':
            bal -= 1000
            if bal < 0:
                bal += 1000
                print("К сожалению, у вас недостатчно денег, но ресторану 'Бриз' сейчас как раз нужны официанты, можете устроиться на подработку!")
                print("Телепорт...")
                restaurant()

            else:
                print(f"Оплата прошла успешно, на балансе {bal}.")
                five_letters()
        else:
            print(f"Выход.")
def guess_the_number():
    secret_number = random.randint(1, 100)
    print("Я загадал число от 1 до 100.")
    while True:
        guess = int(input("Ваше предположение: "))
        if guess < secret_number:
            print("больше")
        elif guess > secret_number:
            print("меньше")
        else:
            print(f"Верно! Я загадал {secret_number}.")
            print('Вы закончили институт, а это значит, что вы можете открывать собственный бизнес!')
            break

def production():
    global bal
    print('Это - ваш бизнес, вы можете продать детали на площади!')
    print('Для сбора деталей напишите номер конвейера, для остановки и выхода - s')
    global c1, run, unTr
    if unTr == True:
        run = True
        while run:
            if bc[0] == "🔒":
                time.sleep(1)
                c1 += 1
                print(f"Произведено на конвейере 1: {c1}")
            else:
                print("Конвейер заблокирован")
                time.sleep(1)
    else:
        print('Вы не закончили институт!')


def inputing():
    global run, det, c1
    run = True
    while run:
        try:
            command = input()
            if command == '1':
                det += c1
                c1 = 0
                print(f"Собрано продукции: {det}")
            elif command == 's':
                run = False
            else:
                print("Неверная команда")
        except KeyboardInterrupt:
            run = False


def restaurant():
    global running, bal, schTr
    tr = 0
    if schTr == False:
        print("Вы не закончили школу!!!")
    else:
        print("Это - мини-игра, где вам нужно найти 1й ряд из 10 (каждая генерация отделяется), в котором все числа разные!")
        while tr == 0:
            r1 = []
            r2 = []
            r3 = []
            r4 = []
            r5 = []
            r6 = []
            r7 = []
            r8 = []
            r9 = []
            r10 = []
            r = 0
            tr = 0
            for i in range(0, 5):
                r1.append(random.randint(0, 5))
            if tr == 0:
                for i in r1:
                    if r1.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = '2'
            for i in range(0, 5):
                r2.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r2:
                    if r2.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "2"
            for i in range(0, 5):
                r3.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r3:
                    if r3.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "3"
            for i in range(0, 5):
                r4.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r4:
                    if r4.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "4"
            for i in range(0, 5):
                r5.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r5:
                    if r5.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "5"
            for i in range(0, 5):
                r6.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r6:
                    if r6.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "6"
            for i in range(0, 5):
                r7.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r7:
                    if r7.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "7"
            for i in range(0, 5):
                r8.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r8:
                    if r8.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "8"
            for i in range(0, 5):
                r9.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r9:
                    if r9.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "9"
            for i in range(0, 5):
                r10.append(random.randint(0, 5))
            if tr == 0:
                r = 0
                for i in r10:
                    if r10.count(i) == 1:
                        r += 1
                    else:
                        r = 0
                if r == 5:
                    tr = "10"
            a1 = "1    "
            a1 += " ".join(map(str, r1))
            a2 = "2    "
            a2 += " ".join(map(str, r2))
            a3 = "3    "
            a3 += " ".join(map(str, r3))
            a4 = "4    "
            a4 += " ".join(map(str, r4))
            a5 = "5    "
            a5 += " ".join(map(str, r5))
            a6 = "6    "
            a6 += " ".join(map(str, r6))
            a7 = "7    "
            a7 += " ".join(map(str, r7))
            a8 = "8    "
            a8 += " ".join(map(str, r8))
            a9 = "9    "
            a9 += " ".join(map(str, r9))
            a10 = "10   "
            a10 += " ".join(map(str, r10))
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(a5)
        print(a6)
        print(a7)
        print(a8)
        print(a9)
        print(a10)
        ryad = input()
        if ryad == tr:
            bal += 150
            print(bal)
            restaurant()
        elif ryad != 's' and ryad != tr:
            restaurant()

def saves():
    global schTr, unTr
    while True:
        with open("1235.txt", "r", encoding="utf-8") as file:
            saves = file.readlines()
        saves = saves[::2]
        for i in range(len(saves)):
            print(saves[i])
        q = int(input(f"Введите номер сохранения, в котором хотите что-то заменить (1 - {len(saves)}): ")) - 1
        e = 0
        for i in str(saves[q]):
            if i == "|":
                e += 1

        r = int(input(f"Введите номер ячейки, в которой хотите что-то заменить (1 - {e - 1}): "))
        i = []
        t = input()
        w = []
        if schTr == True:
            w.append(1)
        if unTr == True:
            w.append(2)
        w = "".join(w)
        sh = str(saves[q]).split("|")
        sh[r] = w
        print("\n".join(saves).replace(saves[q], f"{"|".join(sh)}"))
        saves = "\n".join(saves).replace(saves[q], f"{"|".join(sh)}")
        print()
        print("-----------------------------------------")
        print()
        with open("1235.txt", "w", encoding="utf-8") as file:
            file.write(saves)


def five_letters():
    print('Это игра "пять букв", \n в ней вы должны угадать рандомное английское слово из 5 букв,\n вводя свои варианты, если буква на месте - 2 \n если есть в слове - 1, а если нет - 0')
    global schTr, unTr
    words = ['apple', 'beach', 'carry', 'dance', 'dress', 'event', 'field', 'glass', 'happy', 'money', 'crack', 'laugh',
             'magic', 'ocean', 'penny']
    secret_word = random.choice(words)
    attempts = 0
    max_attempts = 6
    while attempts < max_attempts:
        guess = input(f'Попробуйте угадать слово ({max_attempts - attempts} попытки остались): ').lower()
        if len(guess) != 5:
            print('Ошибка: слово должно содержать ровно 5 букв.')
            continue
        result = ''
        for i in range(5):
            if guess[i] == secret_word[i]:
                result += '2'
            elif guess[i] in secret_word:
                result += '1'
            else:
                result += '0'
        print(result)
        if result == '22222':
            print('Поздравляем! Вы выиграли!')
            break
        attempts += 1
    if attempts == max_attempts:
        print(f'Вы проиграли. Правильное слово было "{secret_word}".')
    if schTr == False:
        schTr = True
        print('Вы закончили школу, поздравляю!')
        saves()
        return schTr
    else:
        unTr = True
        guess_the_number()
        saves()
        return unTr




def house():
    if tc[0] == "🔒":
        print("\033[37mВы - дома!")
        print('Сдесь в туристическом не очень интересно...')
    if bc[0] == "🔒":
        print("\033[37mВы - дома!")
        print('Вы можете поспать, ваш бизнесс продолжит работать!')


nam = ""
@bot.message_handler(commands=['start'])
def Start_tutor(message):
    global nam
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("map", callback_data="m")
    markup.row(b1)
    time.sleep(1)
    bot.send_message(message.chat.id,"Приветствую вас в моем удивительном городе, в нем каждый человек находит свое истинное предназначение!\n")
    time.sleep(1)
    bot.send_message(message.chat.id,"Для начала я познакомлю вас с правилами игры!")
    time.sleep(1)
    bot.send_message(message.chat.id,"Вы можете стать туристом и просто гулять по городу, взаимодействуя с окружением - для этого в любой момент игры вы можете нажать t,")
    time.sleep(1)
    bot.send_message(message.chat.id,"А также можете открыть свой бизнесс, нажав букву b (все буквы только строчные!)")
    time.sleep(1)
    bot.send_message(message.chat.id,"По умолчанию вы - турист")
    time.sleep(1)
    bot.send_message(message.chat.id,"Для вызова карты - m")
    time.sleep(1)
    bot.send_message(message.chat.id,"Для получения текущей информации о вас - a")
    time.sleep(1)
    bot.send_message(message.chat.id,"В начале вы находитесь на цифре 1 - в вашем доме!")
    time.sleep(1)
    bot.send_message(message.chat.id,"Удачной игры!", reply_markup=markup)
    time.sleep(1)
    nam = input("Ах, да! Совсем забыл? Как вас зовут?")
    return nam

def about():
    global nam, pos, bal, schTr, unTr
    print(f"\033[1;30;47mВас зовут {nam}")
    if tc[0] != "🔒":
        print(f"Вы - бизнесмен!")
    else:
        print("Вы - турист!")
    print(f"Вы находитесь на позиции {pos}")
    print(f"Ваш баланс {bal}")
    if tc[0] != "🔒":
        if schTr == False:
            print(f"Вы не закончили ни школу, ни институт и не открыли бизнес")
            if bal < 1000:
                print(f"Вам не хватает на институт")
        elif unTr == False:
            print(f"Вы закончили школу, но не закончили институт и не открыли бизнес")
            if bal < 1000:
                print(f"Вам не хватает на институт")
        else:
            print(f"Вы закончили школу и институт")



def square():
    global bal, det, prodmoney
    prodmoney = 5
    if tc[0] == "🔒":
        print('Здравствуйте, пока что временно работаем только с продавцами, закупем товар!')
    else:
        print('За каждую деталь мы готовы платить 5 монет, возможны торги. Торговаться? y/n')
        if input() == 'y':
            yn = 0
            while yn == 0:
                prodmoney = int(input("Эй, парень, предлагай цену, и быстро! Очередь! Ну, определился? Говори: "))
                if prodmoney <= 25:
                    yn = random.randint(0, 1)
                    print(f'Я подумаю...')
                else:
                    print(f'Я не согласен, цена слишком высока...')
            bal += det * prodmoney
            print(f'Вы получили {det * prodmoney} монет.')
        else:
            bal += det * prodmoney
            print(f'Вы получили {det * prodmoney} монет.')


def Map(tc, bc, p, bal,message):
    global pos
    print(1)
    lpos = pos
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("b", callback_data="b")
    b2 = types.InlineKeyboardButton("t", url="t")
    b3 = types.InlineKeyboardButton("a", url='a')
    b4 = types.InlineKeyboardButton("m", callback_data="m")
    markup.add(b2, b1, b3, b4)
    bot.send_message(
        message.chat.id,
        f"Здравствуй!\n"
        f"🏠1️⃣⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🏠⬜️⬜️⬜️  \n"
        f"⬜️⬜️⬜️⬜️⬜️☕️3️⃣⬜️⬜️⬜️📒4️⃣️⬜️⬜️⬜️⬜️⬜️⬜️  \n"
        f"⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️  \n"
        f"⬜️⬜️⬜️⬜️🎓2️⃣⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🏠⬜️⬜️⬜️  \n"
        f"⬜️⬜️⬜️⬜️⬜️🔲🔲🔲🔲🎪🔲🔲⬜️⬜️⬜️⬜️⬜️⬜️  \n"
        f"⬜️🏠⬜️⬜️🔲🔲🔲🎠🔲🔲🔲🔲🏠⬜️⬜️⬜️🏠⬜️\n"
        f"⬜️⬜️⬜️⬜️⬜️🔲🔲6️⃣🔲🔲🔲🔲🔲⬜️⬜️⬜️⬜️⬜  \n"
        f"⬜️⬜️⬜️⬜️⬜️🔲🔲🔲🔲🔲🔲🔲🔲⬜️⬜️⬜️⬜️⬜️  \n"
        f"⬜️⬜️👷5️⃣⬜️⬜️⬜️⬜️🔲🔲🔲🎡🔲⬜️⬜️⬜️7️⃣⬜️\n"
        f"⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n"
        f"⬜️⬜️⬜️⬜️⬜️⬜️🏠⬜️⬜️⬜️⬜️⬜️⬜️⬜️🏠⬜️⬜️⬜️\n"
        f"⬜️⬜️⬜️🏠⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n"
        f"⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🏠⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n"
        f"⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️8️⃣⬜️⬜️⬜️\n"
        f"⬜️⬜️⬜️⬜️🏠⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n"
        f"⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n"
        f"Y - Ваше положение на карте\n"
        f"1 - Ваш дом\n"
        f"2 - {tc[0]}\n"
        f"3 - Ресторан 'Бриз'\n"
        f"4 - {tc[1]}\n"
        f"5 - {tc[2]}\n"
        f"6 - Главная площадь (с ресторанами)\n"
        f"7 - {bc[0]}\n"
        f"8 - {bc[1]}\n"
        f"для вызова карты нажмите m",
        reply_markup=markup
    )
    print(f"_________________________________________________  Y - Ваше положение на карте\n"
          f"|     1    |~~~~~~~~~~~|        |               |  1 - Ваш дом\n"
          f"|__________|~~~~~~~~~~~|    3   |       4       |  2 - {tc[0]}\n"
          f"|~~~~~~~~̲̃ ̲̲̃̃ ̃    ~~|        |               |  3 - Ресторан 'Бриз'\n"
          f"|~~~~~~~~|     2    |̲̃|________|________       |  4 - {tc[1]}\n"
          f"|~~~~~~~~|     _____|~~~~~~~~       ~~~~|       |  5 - {tc[2]}\n"
          f"|~~~~~~~~|_____|         ~~~~~~     ~~~~|       |  6 - Главная площадь (с ресторанами)\n"
          f"|~~~~~~~~~~~~~~|         ~~6~~~~~~~~~~~~|_______|  7 - {bc[0]}\n"
          f"|̲̃ ̲̃ ̲̃ ̲̃ ̲̃|~~~~~~~~~~~~~~~      ~~~|       |  8 - {bc[1]}\n"
          f"|       5      |~~~~~~~~~~~~~~~      ~~~|   7   |\n"
          f"|______________|̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̃|       |  ~ - Улица (пустота)\n"
          f"|~~~~~~̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃~~~~~~̲̃ ̲̃ ̃ |_______|\n"
          f"|~~~~~~|                  |~~~~~~|           |~~|\n"
          f"|~~~~~~|_______           |̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ |           |~~|\n"
          f"|~~~~~~~~~~~~~|               8              |~~|\n"
          f"|~~~~~~~~~~~~~|______________________________|~~|\n"
          f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
          f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
          f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|  для вызова карты нажмите m")
    pos = int(input("Если вы хотите пойти куда - то, нажмите на кнопку с номером, если нет - то же число: "))
    l1 = 'Y' if pos == 1 else ' '
    l2 = 'Y' if pos == 2 and tc[0] != "🔒" else ' '
    l3 = 'Y' if pos == 3 else ' '
    l4 = 'Y' if pos == 4 and tc[1] != "🔒" else ' '
    l5 = 'Y' if pos == 5 and tc[2] != "🔒" else ' '
    l6 = 'Y' if pos == 6 else '~'
    l7 = 'Y' if pos == 7 and bc[0] != "🔒" else ' '
    l8 = 'Y' if pos == 8 and bc[0] != "🔒" else ' '
    print(f"_________________________________________________  Y - Ваше положение на карте")
    print(f"|     1 {l1}  |~~~~~~~~~~~|        |               |  1 - Ваш дом")
    print(f"|__________|~~~~~~~~~~~|    3 {l3} |       4 {l4}     |  2 - {tc[0]}")
    print(f"|~~~~~~~~̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ~~|        |               |  3 - Ресторан 'Бриз'")
    print(f"|~~~~~~~~|     2 {l2}  |̲̃ ̲̃ |________|________       |  4 - {tc[1]}")
    print(f"|~~~~~~~~|     _____|~~~~~~~~       ~~~~|       |  5 - {tc[2]}")
    print(f"|~~~~~~~~|_____|         ~~~~~~     ~~~~|       |  6 - Главная площадь (с ресторанами)")
    print(f"|~~~~~~~~~~~~~~|         ~~6~{l6}~~~~~~~~~~|_______|  7 - {bc[0]}")
    print(f"|̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ |~~~~~~~~~~~~~~~      ~~~|       |  8 - {bc[1]}")
    print(f"|       5 {l5}    |~~~~~~~~~~~~~~~      ~~~|   7 {l7} |")
    print(f"|______________|̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ |       |  ~ - Улица (пустота)")
    print(f"|~~~~~~̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ~~~~~~̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃|_______|")
    print(f"|~~~~~~|                  |~~~~~~|           |~~|")
    print(f"|~~~~~~|_______           |̲̃ ̲̃ ̲̃ ̲̃ ̲̃ ̲̃ |           |~~|")
    print(f"|~~~~~~~~~~~~~|               8 {l8}            |~~|")
    print(f"|~~~~~~~~~~~~~|______________________________|~~|")
    print(f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print(f"|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|  для вызова карты нажмите m")
    if pos > lpos:
        print("Идем...")
        time.sleep(pos - lpos)
    elif lpos > pos:
        print("Идем...")
        time.sleep(lpos - pos)
    if pos == 1:
        house()
    if pos == 2:
        if tc[0] != "🔒":
            un()
        else:
            print("Простите, но доступ открыт только на сложности бизнесмен")
    if pos == 3:
        restaurant()
    if pos == 4:
        if tc[0] != "🔒":
            five_letters()
        else:
            print("Простите, но доступ открыт только на сложности бизнесмен")
    if pos == 5:
        if tc[0] != "🔒":
                t1 = threading.Thread(target=production)
                t2 = threading.Thread(target=inputing)
                t1.start()
                t2.start()
                t2.join()
                t1.join()
        else:
            print("Простите, но доступ открыт только на сложности бизнесмен")
    if pos == 6:
        square()
    if pos == 7:
        if bc[0] != "🔒":
            print("ТЦ и ТРЦ временно закрыты")
        else:
            print("Простите, но доступ открыт только на сложности турист")
    if pos == 8:
        if bc[0] != "🔒":
            print("ТЦ и ТРЦ временно закрыты")
        else:
            print("Простите, но доступ открыт только на сложности турист")

@bot.callback_query_handler(func=lambda callback: True)
def callb(callback):
    global callb,tc,bc,p,bal
    if callback.data == "b":
        Map(tc, bc, p, bal, callback.message)
    elif callback.data == "a":
        Map(tc, bc, p, bal, callback.message)
    elif callback.data == "m":
        Map(tc,bc,p,bal,callback.message)
    elif callback.data == "t":
        Map(tc,bc,p,bal,callback.message)
bot.infinity_polling()

while True:
    anws = input()
    if anws == "t":
        tc = ["🔒", "🔒", "🔒", ]
        bc = ["ТЦ", "ТРЦ"]
        print("С этого момента вы - турист")
    if anws == "b":
        bc = ["🔒", "🔒", "🔒", ]
        tc = ["Институт (платный)", "Школа (бесплатная)", "Ваш бизнесс", ]
        print("Теперь вы - бизнесмен!")
    if anws == "m":
        Map(tc, bc, s, bal)
    if anws == "a":
        about()


print("\033[37m Приветствую вас в моем удивительном городе, в нем каждый человек находит свое истинное предназначение!")
