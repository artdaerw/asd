import telebot, random, time

bot = telebot.TeleBot('7659043896:AAElYsiYcdI-_GJaNPV-jcri5nCK74UH4T4')
global botS
def suefa(message):
    global botS
    suefabot = ["камень", "ножницы", "бумага"]
    botS = random.choice(suefabot).upper()
    time.sleep(2)
    bot.send_message(message.chat.id, '1')
    time.sleep(2)
    bot.send_message(message.chat.id, '2')
    time.sleep(2)
    bot.send_message(message.chat.id, "3!")
    time.sleep(2)

    bot.send_message(message.chat.id, botS)
    erc(message)

@bot.message_handler()
def erc(message):

    global botS
    print(botS, message.text.lower())
    if botS.lower() == message.text.lower():
        bot.send_message(message.chat.id, "Ну... Что же, как вижу: Ничья! Давайте же переиграем!")
    elif botS.lower() == "камень" and message.text.lower() == "ножницы" or botS.lower() == "ножницы" and message.text.lower() == "бумага" or botS.lower() == "бумага" and message.text.lower() == "камень":
        bot.send_message(message.chat.id, "А вы говорили, что хорошо играете в суефа!")
    elif botS.lower() == "ножницы" and message.text.lower() == "камень" or botS.lower() == "бумага" and message.text.lower() == "ножницы" or botS.lower() == "камень" and message.text.lower() == "бумага":
        bot.send_message(message.chat.id, "Ох, я расслабился! Требую реванша!")