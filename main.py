def main():
	x = 996
	print("Проверка простоты числа",x,":",is_simple_number(x))
	print("Расклад числа",x,"на множители :")
	factorize_number(x)

def is_simple_number(x):
	""" Метод грубой силы.
		Определяет, является ли число простым.
		x - целое положительное число.
	    Если простое, то восвращает True,
	    а иначе - False
	"""
	divisor = 2
	while divisor < x:
		if x%divisor == 0:
			return False
		divisor += 1
	return True

def factorize_number(x):
	""" Раскладывает число на множители.
		Выводит на экран.
		х - целое положительное число.
	"""
	divisor = 2
	while x > 1:
		if x%divisor == 0:
			print(divisor)
			x //= divisor
		else:
			divisor += 1

if __name__ == "__main__":
	main()