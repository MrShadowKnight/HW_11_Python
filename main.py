# TACK №1

name = input("Введіть своє ім'я: ")
age = int(input("Введвть свій вік: "))
if age < 0 and age > 130:
    print(f"Привіт, {name}! Твій вік — {age}.")
else:
    print("Помилка!")

# TACK №2.1

def hellow(name, age):
    print(f"Привіт, {name}! Твій вік — {age}.")

name = input("Введіть своє ім'я: ")
age = int(input("Введвть свій вік: "))

if age < 0 and age > 130:
    hellow(name, age)
else:
    print("Помилка!")

# TACK №2.2

def hellow(name, age):
    if age < 0 and age > 130:
        print(f"Привіт, {name}! Твій вік — {age}.")
    else:
        print("Помилка!")

name = input("Введіть своє ім'я: ")
age = int(input("Введвть свій вік: "))
hellow(name, age)

# TACK №3

try:
    my_list = []
    while True:
        num = int(input("Введіть додатнє число (або будь-яке від'ємне число для завершення): "))
        if num < 0:
            raise ValueError("Введено від'ємне число")
        my_list.append(num)
except ValueError as ve:
    print("Помилка:", ve)
finally:
    sum_of_numbers = sum(my_list)
    print("Сума всіх додатніх чисел:", sum_of_numbers)

# TACK №4.1

def removed(list):
    return sum(list)

try:
    my_list = []
    while True:
        num = int(input("Введіть додатнє число (або будь-яке від'ємне число для завершення): "))
        if num < 0:
            raise ValueError("Введено від'ємне число")
        my_list.append(num)
except ValueError as ve:
    print("Помилка:", ve)
finally:
    print("Сума всіх додатніх чисел:", removed(my_list))

# TACK №4.2

def main():
    numbers = []
    try:
        while True:
            num = float(input("Введіть додатнє число (або будь-що інше для завершення вводу): "))
            if num <= 0:
                raise ValueError("Введіть тільки додатні числа.")
            numbers.append(num)
    except ValueError as ve:
        print(f"Помилка: {ve}")

    if numbers:
        try:
            total_sum = sum(numbers)
            print(f"Сума всіх чисел: {total_sum}")
        except Exception as e:
            print(f"Помилка при розрахунку суми: {e}")

main()

import telebot
from telebot import types

bot = telebot.TeleBot("   ")

print("___ START BOT ______")


def simple_numbers(star_value, end_value):
    simple_num = []
    for i in range(star_value, end_value+1):
        flag = True
        for dil in range(star_value, end_value):
            if dil != 1 and dil < i:
                result = i % dil
                if result == 0:
                    flag = False
                    break
                if dil >= i:
                    break
        if flag:
            simple_num.append(i)
    return simple_num


def main_reply_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # itembtn1 = types.KeyboardButton('a')
    # itembtn2 = types.KeyboardButton('v')
    # itembtn3 = types.KeyboardButton('d')
    # markup.add(itembtn1, itembtn2, itembtn3)
    markup.row(types.KeyboardButton("Прості числа"), types.KeyboardButton("Курс валют"))
    return markup


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    cid = msg.chat.id
    bot.send_message(cid, "Hello!", reply_markup=main_reply_menu())
    # bot.reply_to(message, "Howdy, how are you doing?")
@bot.message_handler(func=lambda message: True)
def echo_all(msg):
    # bot.reply_to(message, message.text)
    cid = msg.chat.id
    if msg.text.lower() == "прості числа":
        numbers = simple_numbers(1, 100)
        temp_text = "Список простих чисел: \n\n"
        for num in numbers:
            temp_text += f"{num} "
        bot.send_message(cid, temp_text)
    elif msg.text.lower() == "курс валют":
        money_text = "Купівля                  Продаж\n37,21      Долар   37,35 \n41,15      Євро      41,48\n9,20        Злотий  9,35"
        bot.send_message(cid, money_text)

bot.infinity_polling()