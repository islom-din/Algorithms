def main():
	print(is_simple_number(5))

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

if __name__ == "__main__":
	main()