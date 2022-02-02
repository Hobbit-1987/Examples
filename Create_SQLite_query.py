# Программа для тестирования SQL запросов
import sqlite3

# Список с примерами запросов
examples_query=[
	"CREATE TABLE IF NOT EXISTS 'table_name'('clmn_name1' INTEGER, 'clmn_name2' TEXT)",
	"INSERT INTO 'table_name' (clmn_name1, clmn_name2) VALUES('val_1', 'val_2')",
	"SELECT * FROM 'table_name'",
	"DROP TABLE 'table_name'"
	]

# функция выполнения запроса, complete_msg принимает строку соответствующую выполняемому 
# запросу, агрумент show необязательный
def my_query(complete_msg, show = ''): 
	try:
		with sqlite3.connect('data.db') as db: 
			print('connect with data base ...') 
			cursor = db.cursor() # создание курсора
			cursor.execute(sql_query) # вставка введенного запроса в курсор
			db.commit() # подтверждение

			if show: # показать содержимое таблицы, если передано любое значение в show
				print(complete_msg) # сообщение о выполнении запроса
				print(cursor.fetchall())
			else:
				print(complete_msg)
	except sqlite3.OperationalError: # исключение если не правильный ввод 
		print('ERROR: incomplete input')

# цикл для ввода запросов
while quit != 'q':
	print(' ')
	print('``' * 5 + 'Hallo, this is a program for testing SQLite queryes' + '``' * 5)
	print('``' * 5 + 'For show examples query enter "help" ' + '``' * 5)
	sql_query = input("Enter your query or 'q' for quit: >>  ") # запрос ввода
	# если ввод начинается с 'create', то функции my_query передается строка 
	# соответствующая выполненному запросу
	if sql_query.lower().startswith('create'):
		my_query('Great, the new table created succesfully !')
	elif sql_query.lower().startswith('insert'):
		my_query('Great, yor data added succesfully !')
	elif sql_query.lower().startswith('select'):
		my_query('Your table', 1) # аргумент 1 для инициализации вывода таблицы
	elif sql_query.lower().startswith('drop'):
		my_query('Your table deleted succesfully !')
	# если введен help, на экране перебиратся список examples_query
	elif sql_query.lower().startswith('help'): 
		for val in examples_query:
			print(val)
	elif sql_query.lower().startswith('q'): # выход
		quit = 'q'
