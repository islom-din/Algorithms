#---------------------------------------------
#Квадратичные сортировки со сложностью O(n^2).
#---------------------------------------------
def insert_sort(A:list):
	"""Сортировка вставками."""
	N = len(A)
	length_of_sort_part = 0
	while A[length_of_sort_part] < A[length_of_sort_part + 1]:
		length_of_sort_part += 1
	for i in range(length_of_sort_part + 1, N):
		j = i
		while A[j] < A[j-1] and j > 1:
			A[j],A[j-1] = A[j-1],A[j]
			j -= 1
	return A

def choice_sort(A:list):
	"""Сортировка выбором."""
	N = len(A)
	for i in range(0,N):
		Min = A[i]
		pos = i
		for j in range(i,N):
			if A[j] < Min:
				Min = A[j]
				pos = j
		A[i],A[pos] = A[pos],A[i]
	return A

def bubble_sort(A:list):
	"""Сортировка пузырьком"""
	N = len(A)
	for bypass in range(1,N):
		for k in range(0, N-bypass):
			if A[k] > A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]

#---------------------------------------------
#Быстрые сортировки со сложностью O(n^2).
#---------------------------------------------

def merge_sort(A:list):
	"""Сортировка слиянием"""
	if len(A) <= 1:
		return A
	middle = len(A)//2
	L = [A[i] for i in range(0,middle)]
	R = [A[i] for i in range(middle,len(A))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L,R)
	for i in range(len(A)):
		A[i] = C[i]

def merge(A:list, B:list):
	"""Вспомогательная функция для сортировки слиянием.
	   Эта функция непосредственно склеивает две половины массива.
	"""
	C = [0]*(len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C

def hoar_sort(A):
	"""Сортировка Тони Хоара(Quick Sort)
	"""
	if len(A) <= 1:
		return
	L = [] 
	M = [] 
	R = []
	barrier = A[0]
	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
	hoar_sort(L)
	hoar_sort(R)
	k = 0
	for x in L+M+R:
		A[k] = x
		k += 1

