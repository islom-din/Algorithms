"""
	Класс myStack описывает классический stack с функциями: 
	push(element), pop(), top(), isEmpty(), length(), hasElem(element).
"""

class myStack:

	#Создание пустого списка при инициализации объекта исходного класса
	def __init__(self):
		self.L = []

	#Вставка элемента поверх других
	def push(self, element):
		self.L.append(element)

	#Удаление самого верхнего элемента
	def pop(self):
		self.L.pop()

	#Вернуть самый верхний элемент	
	def top(self):
		length = len(self.L)
		return self.L[length - 1]

	#Проверка на пустоту стека	
	def isEmpty(self):
		if len(self.L) == 0:
			return True
		else:
			return False

	#Вернуть длину стека
	def length(self):
		return len(self.L)

	#Проверка на наличие данного элемента в стеке
	def hasElem(self, element):
		for elem in self.L:
			if elem == element:
				return True
		return False
