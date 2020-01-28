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