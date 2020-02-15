import sort

def main():
	gen(2)

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
	(7)
	"""
	if a == b:
		return a
	elif a > b:
		return gcd1(a - b, b)
	else: #a < b
		return gcd1(b - a, a)

def gcd2(a,b):
	"""Расширенный алгоритм Евклида
	(7)
	"""
	return a if b == 0 else gcd2(b, a%b)

def pow(a:float,n:int):
	"""Быстрое возведение в степень
	(7)
	"""
	if n == 0:
		return 1
	elif n%2 == 0:
		return pow(a**2,n//2)
	else:
		return pow(a,n-1)*a

def generate_number(N:int, M:int, prefix=None):
	"""Генерация всех чисел (с лидирующими незначащими нулями)
	в N-ричной системе счисления (N <= 10)
	"""
	prefix = prefix or []
	if M == 0:
		print(prefix)
		return
	for digit in range(N):
		prefix.append(digit)
		generate_number(N, M-1, prefix)
		prefix.pop()

#Генерация только для двоичной системы счисления
def gen(M,prefix=""):
	if M == 0:
		print(prefix)
	else:
		gen(M-1,prefix + "0")
		gen(M-1,prefix + "1")

def generate_permutation(N:int, M:int=-1, prefix=None):
	"""Генерация всех перестановок N чисел в M позиция,
	   с префиксом prefix
	   (8)
	"""
	if M == -1:
		M = N #По умолчанию N чисел в N позициях
	prefix = prefix or []
	if M == 0:
		print(*prefix)
		return
	for number in range(1,N+1):
		if find(number, prefix):
			continue
		prefix.append(number)
		generate_permutation(N,M-1,prefix)
		prefix.pop()

def find(number, A):
	"""(Вспомогательная функция для generate_permutation)
	   Поиск x в A. Вернуть true, если такой есть 
	   False, если такого нет
	"""
	for x in A:
		if number == x:
			return True
	return False


if __name__ == "__main__":
	main()