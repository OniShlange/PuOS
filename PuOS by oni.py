#Настройки
username = "puser"
logs = False
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
            subprocess.call("cls", shell=True)
            print(f"Сейчас дата и время: {datetime.datetime.now()}")
            x = input()
            if x == "exit":
                break
class math:
    def plus(x, y, z1, z2):
        try:
            print(f"Результат: {float(x) + float(y)}")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} слаживает {x} + {y}, это должно дать {float(x) + float(y)}\n")
        except ValueError:
            print("Введено неверное число!")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} пытался сложить {x} + {y}, это и вызвало ошибку.\n")
    def minus(x, y, z1, z2):
        try:
            print(f"Результат: {float(x) - float(y)}")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} вычитает {x} - {y}, это должно дать {float(x) - float(y)}\n")
        except ValueError:
            print("Введено неверное число!")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} пытался вычесть {x} - {y}, это и вызвало ошибку.\n")
    def delenie(x, y, z1, z2):
        try:
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} делит {x} / {y}, это должно дать {float(x) / float(y)}\n")
            print(f"Результат: {float(x) / float(y)}")
        except ValueError:
            print("Введено неверное число!")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} пытался поделить {x} / {y}, это и вызвало ошибку.\n")
        except ZeroDivisionError:
            print("Результат: 0")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} делит {x} / 0, это дало 0\n")
    def umnozhenie(x, y, z1, z2):
        try:
            print(f"Результат: {float(x) * float(y)}")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} умножает {x} * {y}, это должно дать {float(x) * float(y)}\n")
        except ValueError:
            print("Введено неверное число!")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} пытался умножить {x} * {y}, это и вызвало ошибку.\n")
    def stepen(x, y, z1, z2):
        try:
            print(f"Результат: {float(x) ** float(y)}")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} остепенить {x} ** {y}, это должно дать {float(x) ** float(y)}\n")
        except ValueError:
            print("Введено неверное число!")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} пытался остепенить {x} ** {y}, это и вызвало ошибку\n")
    def random(x, y, z1, z2):
        try:
            print(f"Результат: {random.randint(int(x), int(y))}")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} рандомизирует от {x} до {y}\n")
        except ValueError:
            print("Введено неверное число!")
            if z1:
                z2.write(f"[{datetime.datetime.now()}] {username} пытался рандомизировать от {x} до {y}, это и вызвало ошибку\n")
class game:
    def clicker(z1, z2):
        print("Это кликер! Чтобы кликать, вам нужно нажимать Enter. Чтобы выйти из игры, напишите exit и нажмите Enter. Пожалуйста, кликайте честно, а не зажимайте!")
        y = 0
        while True:
            x = input()
            y +=1
            if x == "exit":
                if z2:
                    z1.write(f"[{datetime.datetime.now()}] {username} накликал {y}\n")
                return y
                break
            else:
                print(f"Вы накликали: {y}")
# нет функций
version = "v0.0.5"
debug = False
logfile = False

print(f"""  ____         ___  ____  
 |  _ \ _   _ / _ \/ ___| 
 | |_) | | | | | | \___ \ 
 |  __/| |_| | |_| |___) |
 |_|    \__,_|\___/|____/  {version} by oni

Для помощи по поводу команд, пишите "help"
Запущено по пути {os.path.abspath(os.path.dirname(__file__))}
Имя пользователя: {username}
""")
if logs:
    logfile = open(f"pulogs_{random.randint(100000, 999999)}.txt", "w", encoding='utf-8')
    logfile.write(f"[{datetime.datetime.now()}] Система запущена. Имя пользователя: {username}, версия системы: {version}, запущено по пути {os.path.abspath(os.path.dirname(__file__))}\n")
while True:
    q = input(f"{username}*PuOS{version} >>>")
    ql = q.split(" ")
    if logs:
        logfile.write(f"[{datetime.datetime.now()}] {username} использовал команду {q}\n")
    if ql[0] == "exit":
        try:
            if ql[1] != True:
                print("Неизвестный аргумент, пропускаем")
        except IndexError:
            pass
        print("Отключение...")
        time.sleep(1)
        if logs:
            logfile.write(f"[{datetime.datetime.now()}] {username} отключил систему.\n")
        logfile.close()
        break
    elif q == "":
        pass
    elif ql[0] == "debug":
        try:
            if ql[1] != True:
                print("Неизвестный аргумент, пропускаем")
        except IndexError:
            pass
        x = input("password: ")
        if x == "makemedebuger":
            debug = True
            backup_username = username
            username = "debug"
            print("дебаг включён")
            if logs:
                logfile.write(f"[{datetime.datetime.now()}] {username} стал дебаггером\n")
        elif x == "unmakemedebuger":
            debug = False
            username = backup_username
            print("дебаг выключен")
            if logs:
                logfile.write(f"[{datetime.datetime.now()}] {username} перестал быть дебаггером\n")
        else:
            print("доступ запрещён")
            if logs:
                logfile.write(f"[{datetime.datetime.now()}] {username} ввёл неправильный пароль для дебага\n")
    elif ql[0] == "sleep":
        try:
            if ql[1] != True:
                print("Неизвестный аргумент, пропускаем")
        except IndexError:
            pass
        if logs:
            logfile.write(f"[{datetime.datetime.now()}] {username} вошёл в сон\n")
        system.sleep()
    elif ql[0] == "math":
        try:
            if ql[2] == "+":
                math.plus(ql[1], ql[3], logs, logfile)
            elif ql[2] == "-":
                math.minus(ql[1], ql[3], logs, logfile)
            elif ql[2] == "/":
                math.delenie(ql[1], ql[3], logs, logfile)
            elif ql[2] == "*":
                math.umnozhenie(ql[1], ql[3], logs, logfile)
            elif ql[2] == "**":
                math.stepen(ql[1], ql[3], logs, logfile)
            elif ql[2] == "random":
                math.random(ql[1], ql[3], logs, logfile)
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует.")
    elif ql[0] == "game":
        try:
            if ql[1] == "clicker":
                if logs:
                    logfile.write(f"[{datetime.datetime.now()}] {username} запустил игру clicker\n")
                game.clicker(logfile, logs)
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует.")
    elif ql[0] == "console":
        try:
            if ql[1] == "python":
                if logs:
                    logfile.write(f"[{datetime.datetime.now()}] {username} запустил консоль python\n")
                print("Для выхода нажмите Ctrl+Z или напишите exit()")
                print()
                time.sleep(3)
                subprocess.call("python", shell=True)
            elif ql[1] == "shell":
                if logs:
                    logfile.write(f"[{datetime.datetime.now()}] {username} запустил консоль shell\n")
                print("Сейчас откроется новое окно. Для выхода просто закройте окно.")
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
                    if logs:
                        logfile.write(f"[{datetime.datetime.now()}] {username} скачал файл с сайта {ufr}\n")
                    f.close()
                    print("Попробуйте открыть puos_download через нужный редактор для просмотра содержимого.")
                except Exception:
                    print("Произошла ошибка при скачивании! Убедитесь в правильности ссылки, наличии интернета и скачивается ли с сайта файл")
                    if logs:
                        logfile.write(f"[{datetime.datetime.now()}] {username} пытался скачать файл с {ufr}, это вызвало ошибку\n")
            elif ql[1] == "sitecode":
                try:
                    r = requests.post(ql[2])
                    print(r.text)
                    if logs:
                        logfile.write(f"[{datetime.datetime.now()}] {username} запросил код сайта {r}")
                except Exception:
                    print("Произошла ошибка при отображении!")
                    if logs:
                        logfile.write(f"[{datetime.datetime.now()}] {username} пытался получить код сайта {r}, это вызвало ошибку\n")
            elif ql[1] == "apiget":
                try:
                    ufr = requests.get(ql[2])
                    apiget = ufr.json()
                    print(apiget)
                    if logs:
                        logfile.write(f"[{datetime.datetime.now()}] {username} отправил JSON запрос сайта {r}\n")
                except Exception:
                    print("Произошла ошибка при скачивании!")
                    if logs:
                        logfile.write(f"[{datetime.datetime.now()}] {username} пытался получить ответ на запрос от сайта {r}\n")
            else:
                print("Аргумент неверный. Проверьте команду в 'help'")
        except IndexError:
            print("Аргумент отсутствует")
    elif ql[0] == "date":
        try:
            if ql[1] != True:
                print("Неизвестный аргумент, пропускаем")
        except IndexError:
            pass
        print(datetime.datetime.now())
    elif ql[0] == "info":
        try:
            if ql[1] != True:
                print("Неизвестный аргумент, пропускаем")
        except IndexError:
            pass
        print(f"Имя: {username}, система: PuOS, версия системы: {version}")
    elif ql[0] == "help":
        try:
            if ql[1] != True:
                print("Неизвестный аргумент, пропускаем")
        except IndexError:
            pass
        print("""
        console [python|shell] - консоль
        date = время и дата
        exit = отключение системы
        game [clicker] = игры
        info = информация о сессии
        math [number1] [+|-|/|*|**|random] [number2] = математика
        net [download|sitecode|apiget] [site] - интернет
        sleep = сон
        """)
    else:
        print(f"Команды {q} не существует. Используйте команду 'help', чтобы получить доступные команды.")
