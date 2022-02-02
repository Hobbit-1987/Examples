# Калькулятор градусов на фреймворке kivy.
# Производит сложение или вычитание.

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty


from kivy.core.window import Window
Window.size = (480, 853)

from kivy.config import Config
Config.set("kivy", "keyboard_mode", "systemanddoc")

# строка с макетами 
Builder.load_string('''
<Container>:
	rows: 4
	padding: 50


		# связь переменных из функции calc() c id форм ввода, id кнопки и id текстового 
		# поля result
	dgrs: dgrs
	mnts: mnts
	scnds: scnds
	dgrs2: dgrs2
	mnts2: mnts2
	scnds2: scnds2
	result: result

	BoxLayout:
		orientation:"vertical"

		BoxLayout:   # Макет с подписями над полями ввода.
			Label:
				multiline: False
				font_size: 30 # 
				text: "град"
			Label:
				multiline: False
				font_size: 30
				text: "мин"
			Label:
				multiline: False
				font_size: 30
				text: "сек"

		BoxLayout:   # Макет с полями ввода для первого значения.
			TextInput:
				size_hint: 0.6, 0.6 
				pos_hint: {"center_x": 0.1, "y": 0.3}
				id:dgrs
				multiline: False
				font_size: 30
				input_type: "number"
				input_filter: "int"
			TextInput:
				size_hint: 0.6, 0.6
				pos_hint: {"center_x": 0.1, "y": 0.3}
				id:mnts
				multiline: False
				font_size: 30
				input_type: "number"
				input_filter: "int"
			TextInput:
				size_hint: 0.6, 0.6
				pos_hint: {"center_x": 0.1, "y": 0.3}
				id:scnds
				multiline: False
				font_size: 30
				input_type: "number"
				input_filter: "int"

		BoxLayout:	# Макет с кнопками вычитания и сложения.	
			Button:   
				id: button_1
				size_hint: 0.5, 0.4
				text: "Вычесть"
				font_size: 30
				pos_hint: {"center_x": 0.1, "y": 0.3}

                  # Вызов функции после нажатия. Без аргумента функция произведет вычетание.
				on_release:  
					root.calc() 

			Button: 
				id: button_2
				size_hint: 0.5, 0.4
				text: "Сложить"
				font_size: 30
				pos_hint: {"center_x": 0.1, "y": 0.3}

				  # С аргументом функция произведет сложение.
				on_release:   
					root.calc(1) 
				
		BoxLayout:   # Макет с полями ввода для второго значения.
			TextInput:
				size_hint: 0.6, 0.6
				pos_hint: {"center_x": 0.1, "y": 0.3}
				id:dgrs2
				multiline: False
				font_size: 30
				input_type: "number"
				input_filter: "int"
			TextInput:
				size_hint: 0.6, 0.6
				pos_hint: {"center_x": 0.1, "y": 0.3}
				id:mnts2
				multiline: False
				font_size: 30
				input_type: "number"
				input_filter: "int"
			TextInput:
				size_hint: 0.6, 0.6
				pos_hint: {"center_x": 0.1, "y": 0.3}
				id:scnds2
				multiline: False
				font_size: 30
				input_type: "number"
				input_filter: "int"

		BoxLayout:   # текстовое поле для вывода результата  
			Label:
				id:result
				multiline: False
				font_size: 30
				text: "Результат"

		BoxLayout:   # текстовое поле с подписью
			Label: 
				multiline: False
				font_size: 10
				text: "by_Hobbit"
''')


class Container(BoxLayout):
		
	def calc(self, plus =''): # если в plus передать любой аргумент, функция 
	                          # сработает на вычитание 
	    # присвоение переменным в функции значений TextInput                      
		try: 
			dgrs = str(self.dgrs.text)
			mnts = str(self.mnts.text)
			scnds = str(self.scnds.text)

			dgrs2 = str(self.dgrs2.text)
			mnts2 = str(self.mnts2.text)
			scnds2 = str(self.scnds2.text)
		except:
			dgrs = float('')
			mnts = float('')
			scnds = float('')

			dgrs2 = float('')
			mnts2 = float('')		
			scnds2 = float('')

		# обработка введенных значений
		ss = float(scnds)/60
		ms = (float(mnts) + ss) /60 
		ds = float(dgrs) + ms

		ss2 = float(scnds2)/60
		ms2 = (float(mnts2) + ss2) / 60
		ds2 = float(dgrs2) + ms2

		# выбор: сложить или вычесть градусы
		if plus:
			grad = ds + ds2
		else:
			grad = ds - ds2

		mint = float('0' + str(grad)[str(grad).index('.'):])*60 # отделяю дробную часть от грудусов, умножаю на 60 и целую часть вывожу в минуты

		secns = float('0' + str(mint)[str(mint).index('.'):])*60 # отделяю дробную часть от минут, умножаю на 60 и целую часть вывожу в секунды

		x = (str(int(grad)) + '° ' + str(int(mint)) + '\'' + str(round(secns)) + '\"' ) # формирование ответа

		self.result.text = x # вывод результата в текстовое поле приложения 

class MyApp(App):
	def build(self):
		
		return Container()

if __name__=="__main__":
	MyApp().run()

