#Настройки
username = "puser"
#Конец настроек
import time
import datetime
import subprocess
import random
import os
from sys import platform
# проверка системы
if platform == "win32":
    pass
else:
    print("""К сожалению, наша программа не оптимизирована под вашу систему. Что это значит? Это значит то, что некоторые функции могут не работать. Постараемся исправить это в будущих обновлениях.
""")
# функции
class system:
    def sleep():
        print("Вы вошли в режим сна, чтобы выйти, пропишите exit")
        time.sleep(5)
        while True:
            print(" " * 8800)
            print(f"Сейчас дата и время: {datetime.datetime.now()}")
            x = input()
            if x == "exit":
                break
class math:
    def plus():
        try:
            x = input("Введите первое число: ")
            y = input("Введите второе число: ")
            print(f"Результат: {int(x) + int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def minus():
        try:
            x = input("Введите первое число: ")
            y = input("Введите второе число: ")
            print(f"Результат: {int(x) - int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def delenie():
        try:
            x = input("Введите первое число: ")
            y = input("Введите второе число: ")
            print(f"Результат: {int(x) / int(y)}")
        except ValueError:
            print("Введено неверное число!")
        except ZeroDivisionError:
            print("Результат: 0")
    def umnozhenie():
        try:
            x = input("Введите первое число: ")
            y = input("Введите второе число: ")
            print(f"Результат: {int(x) * int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def stepen():
        try:
            x = input("Введите первое число: ")
            y = input("Введите второе число: ")
            print(f"Результат: {int(x) ** int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def random():
        try:
            x = input("Введите первое число: ")
            y = input("Введите второе число: ")
            print(f"Результат: {random.randint(int(x), int(y))}")
        except ValueError:
            print("Введено неверное число!")
class game:
    def clicker():
        print("Это кликер! Чтобы кликать, вам нужно нажимать Enter. Чтобы выйти из игры, напишите exit и нажмите Enter. Пожалуйста, кликайте честно, а не зажимайте!")
        y = 0
        while True:
            x = input()
            y +=1
            if x == "exit":
                return y
                break
            else:
                print(f"Вы накликали: {y}")
# нет функций
version = "v0.0.3"
debug = False

print(f""" _____           _____    _____
|     |         |     |  |
|     |         |     |  |
|_____|  |   |  |     |  |_____
|        |   |  |     |        |
|        |___|  |_____|  ______| 
{version} by oni.py

Для помощи по поводу команд, пишите "help"
Запущено по пути {os.path.abspath(os.path.dirname(__file__))}
Имя пользователя: {username}
""")

while True:
    q = input(f"{username}*PuOS{version} >>>")
    if q == "exit":
        print("Отключение...")
        time.sleep(1)
        break
    elif q == "":
        pass
    elif q == "debug":
        x = input("password: ")
        if x == "makemedebuger":
            debug = True
            backup_username = username
            username = "debug"
            print("дебаг включён")
        elif x == "unmakemedebuger":
            debug = False
            username = backup_username
            print("дебаг выключен")
        else:
            print("доступ запрещён")
    elif q == "sleep":
        system.sleep()
    elif q == "math":
        print("Нет необходимых аргументов. Проверьте 'help'")
    elif q == "math +":
        math.plus()
    elif q == "math -":
        math.minus()
    elif q == "math /":
        math.delenie()
    elif q == "math *":
        math.umnozhenie()
    elif q == "math **":
        math.stepen()
    elif q == "math random":
        math.random()
    elif q == "game":
        print("Нет необходимых аргументов. Проверьте 'help'")
    elif q == "game clicker":
        print(f"Всего было накликано {game.clicker() - 1}!")
    elif q == "console":
        print("Нет необходимых аргументов. Проверьте 'help'")
    elif q == "console python":
        print("Для выхода нажмите Ctrl+Z или напишите exit()")
        print()
        subprocess.call("python", shell=True)
    elif q == "date":
        print(datetime.datetime.now())
    elif q == "info":
        print(f"Имя: {username}, система: PuOS, версия системы: {version}")
    elif q == "help":
        print("""
        console [python] - консоль
        date = время и дата
        exit = отключение системы
        game [clicker] = игры
        info = информация о сессии
        math [+|-|/|*|**|random] = математика
        sleep = сон
        """)
    else:
        print(f"Команды {q} не существует. Используйте команду 'help', чтобы получить доступные команды.")
        
