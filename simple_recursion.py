"""Простые задачи на рекурсию"""

def rec(a,b):
	"""
	Даны два целых числа A и В (каждое в отдельной строке). 
	Выведите все числа от A до B включительно, в порядке 
	возрастания, если A < B, или в порядке убывания в противном случае. 
	"""
	if a == b:
		print(a)
	if a < b:
		rec(a, b-1)
		print(b)
	if a > b:
		print(a)
		rec(a-1, b)

def akkerman(m, n):
	"""
	Функция Аккермана A(m,n).
	Даны два целых неотрицательных числа m и n, каждое в отдельной строке. Выведите A(m,n).

	"""
	if m == 0:
		return n + 1
	if m > 0 and n == 0:
		return akkerman(m-1,1)
	if m > 0 and n > 0:
		return akkerman(m - 1, akkerman(m, n - 1))

def dv(n,k):
	"""
	Дано натуральное число N. 
	Выведите слово YES, если число N является точной 
	степенью двойки, или слово NO в противном случае.
	
	Операцией возведения в степень пользоваться нельзя!
	"""
	if n == k:
		return "Yes"
	if n < k:
		return "No"
	else:
		return dv(n,2*k)

def split(n):
	"""
	Дано натуральное число N. Выведите все его цифры по одной, 
	в обычном порядке, разделяя их пробелами или новыми строками.

	При решении этой задачи нельзя использовать строки, списки, 
	массивы (ну и циклы, разумеется). Разрешена только рекурсия 
	и целочисленная арифметика. 
	"""
	if n == 0:
		return
	split(n//10)
	print(n%10)

def sumOfNums(n):
	"""Сумма цифр числа"""
	if n == 0:
		return n
	return n%10 + sumOfNums(n//10)

print(sumOfNums(222))



