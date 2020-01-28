def insert_sort(A:list):
	"""Сортировка вставками.
	   Сложность: O(n^2).
	   A - исходный неотсортированный массив.
	"""
	N = 0
	for elem in A:
		N += 1
	length_of_sort_part = 0
	while A[length_of_sort_part] < A[length_of_sort_part + 1]:
		length_of_sort_part += 1
	for i in range(length_of_sort_part + 1, N):
		j = i
		while A[j] < A[j-1]:
			A[j],A[j-1] = A[j-1],A[j]
			if j > 1:
				j -= 1
	return A

def choice_sort(A:list):
	"""Сортировка выбором.
	   Сложность: O(n^2).
	   A - исходный неотсортированный массив.
	"""
	N = 0
	for elem in A:
		N += 1
	for i in range(0,N):
		Min = A[i]
		pos = i
		for j in range(i,N):
			if A[j] < Min:
				Min = A[j]
				pos = j
		A[i],A[pos] = A[pos],A[i]
	return A