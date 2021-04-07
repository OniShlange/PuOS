#Настройки
username = "puser"
#Конец настроек
import time
import datetime
import subprocess
import random
import os
import requests
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
    def plus(x, y):
        try:
            print(f"Результат: {int(x) + int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def minus(x, y):
        try:
            print(f"Результат: {int(x) - int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def delenie(x, y):
        try:
            print(f"Результат: {int(x) / int(y)}")
        except ValueError:
            print("Введено неверное число!")
        except ZeroDivisionError:
            print("Результат: 0")
    def umnozhenie(x, y):
        try:
            print(f"Результат: {int(x) * int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def stepen(x, y):
        try:
            print(f"Результат: {int(x) ** int(y)}")
        except ValueError:
            print("Введено неверное число!")
    def random(x, y):
        try:
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
version = "v0.0.4a"
debug = False

print(f""" _____           _____    _____
|     |         |     |  |
|     |         |     |  |
|_____|  |   |  |     |  |_____
|        |   |  |     |        |
|        |___|  |_____|  ______| 
{version} by oni

Для помощи по поводу команд, пишите "help"
Запущено по пути {os.path.abspath(os.path.dirname(__file__))}
Имя пользователя: {username}
""")

while True:
    q = input(f"{username}*PuOS{version} >>>")
    ql = q.split(" ")
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
    elif ql[0] == "math":
        try:
            if ql[1] == "+":
                math.plus(ql[2], ql[3])
            elif ql[1] == "-":
                math.minus(ql[2], ql[3])
            elif ql[1] == "/":
                math.delenie(ql[2], ql[3])
            elif ql[1] == "*":
                math.umnozhenie(ql[2], ql[3])
            elif ql[1] == "**":
                math.stepen(ql[2], ql[3])
            elif ql[1] == "random":
                math.random(ql[2], ql[3])
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует.")
    elif ql[0] == "game":
        try:
            if ql[1] == "clicker":
                game.clicker()
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует.")
    elif ql[0] == "console":
        try:
            if ql[1] == "python":
                print("Для выхода нажмите Ctrl+Z или напишите exit()")
                print()
                time.sleep(3)
                subprocess.call("python", shell=True)
            elif ql[1] == "shell":
                print("Сейчас откроется новое окно. Для выхода просто закройте окно.")
                print()
                time.sleep(3)
                subprocess.call("start", shell=True)
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует.")
    elif ql[0] == "net":
        try:
            if ql[1] == "download":
                try:
                    f = open("puos_download", "wb")
                    ufr = requests.get(ql[2])
                    f.write(ufr.content)
                    f.close()
                    print("Попробуйте открыть puos_download через нужный редактор для просмотра содержимого.")
                except Exception:
                    print("Произошла ошибка при скачивании!")
            elif ql[1] == "sitecode":
                try:
                    r = requests.post(ql[2])
                    print(r.text)
                except Exception:
                    print("Произошла ошибка при отображении!")
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует")
    elif q == "date":
        print(datetime.datetime.now())
    elif q == "info":
        print(f"Имя: {username}, система: PuOS, версия системы: {version}")
    elif q == "help":
        print("""
        console [python|shell] - консоль
        date = время и дата
        exit = отключение системы
        game [clicker] = игры
        info = информация о сессии
        math [+|-|/|*|**|random] [number1] [number2] = математика
        net [download|sitecode] [site] - интернет
        sleep = сон
        """)
    else:
        print(f"Команды {q} не существует. Используйте команду 'help', чтобы получить доступные команды.")
