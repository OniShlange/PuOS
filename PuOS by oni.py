#Настройки
username = "puser"
#Конец настроек
import time
import datetime
import subprocess
# функции
class system:
	def sleep():
		print("Вы вошли в режим сна, чтобы выйти, пропишите exit")
		time.sleep(5)
		while True:
			for i in range(1,50):
				print()
			print(f"Сейчас дата и время: {datetime.datetime.now()}")
			x = input()
			if x == "exit":
				break
class math:
	def plus():
		x = input("Введите первое число: ")
		y = input("Введите второе число: ")
		print(f"Результат: {int(x) + int(y)}")
	def minus():
		x = input("Введите первое число: ")
		y = input("Введите второе число: ")
		print(f"Результат: {int(x) - int(y)}")
	def delenie():
		x = input("Введите первое число: ")
		y = input("Введите второе число: ")
		print(f"Результат: {int(x) / int(y)}")
	def umnozhenie():
		x = input("Введите первое число: ")
		y = input("Введите второе число: ")
		print(f"Результат: {int(x) * int(y)}")
	def stepen():
		x = input("Введите первое число: ")
		y = input("Введите второе число: ")
		if x == 
		print(f"Результат: {int(x) ** int(y)}")
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
version = "v0.0.2b"
debug = False

print(f"""
|-----|         |-----|  |------
|     |         |     |  |
|-----|  |   |  |     |  |_____
|        |   |  |     |        |
|        |___|  |_____|  ______| 
{version} by oni.py

Для помощи по поводу команд, пишите "help"
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
	elif q == "game":
		print("Нет необходимых аргументов. Проверьте 'help'")
	elif q == "game clicker":
		print(f"Всего было накликано {game.clicker() - 1}!")
	elif q == "date":
		print(datetime.datetime.now())
	elif q == "info":
		print(f"Имя: {username}, система: PuOS, версия системы: {version}")
	elif q == "help":
		print("""
		date = время и дата
		exit = отключение системы
		game [clicker] = игры
		info = информация о сессии
		math [+|-|/|*] = математика
		sleep = сон
		""")
	else:
		print(f"Команды {q} не существует. Используйте команду 'help', чтобы получить доступные команды.")
		