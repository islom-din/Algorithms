import sort

def main():
	A = sort.choice_sort([2,1,8,3,6,5,10,4,1])
	print(A)

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

def resheto(N):
	"""Алгоритм Решето-Эратосфена для нахождения
	   простых и составных чисел в пределах от 0 до N.
	"""
	A = [True]*N
	A[0] = A[1] = False
	for k in range(2,N):
		if A[k]:
			for m in range(2*k,N,k):
				A[m] = False
	for k in range(N):
		if A[k]:
			print(k,"- простое")
		else:
			print(k,"- составное")

def gcd1(a,b):
	"""Алгоритм Евклида для вычисления НОД.
	"""
	if a == b:
		return a
	elif a > b:
		return gcd1(a - b, b)
	else: #a < b
		return gcd1(b - a, a)

def gcd2(a,b):
	"""Расширенный алгоритм Евклида
	"""
	return a if b == 0 else gcd2(b, a%b)

if __name__ == "__main__":
	main()