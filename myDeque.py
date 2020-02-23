"""
	Класс myDeque описывает классическую очередь с функциями: 
	push(element), pop(), topL(), topR(), length().
"""

class myDeque:

	#Создание пустого списка при инициализации объекта исходного класса
	def __init__(self):
		self.L = []

	#Вставка элемента поверх других
	def push(self, element):
		self.L.append(element)

	#Удаление самого первого элемента
	def pop(self):
		result_list = []
		for i in range(1,len(self.L)):
			result_list.append(self.L[i])
		self.L = result_list

	#Напечатать все элементы очереди	
	def print_deque(self):
		for i in self.L:
			print(i)

