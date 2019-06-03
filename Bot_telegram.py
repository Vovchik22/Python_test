import telebot

bot = telebot.TeleBot('801817243:AAHDdMydIS_oFZuGOhbTndnCEPRjqcPTeyw')

@bot.message_handler(content_types=['text'])

def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Привет, чем могу помочь")
    elif message.text('/help'):
        bot.send_message(message.from_user.id, 'Напиши привет')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)

name = ''
surname = ''
age = 0

@bot.message_handler(content_types=['text'])
def start (message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'What is your name')
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Write /reg')

def get_name (message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'What is your surname')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'How old are you')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
             keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
             key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
             keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
             key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
             keyboard.add(key_no)
             question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
             bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
