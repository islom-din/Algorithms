"""
	Обход графа в ширину. Функция BFS возвращает словарь из пар {ключ : значение}, в котором 
	ключ - это вершина, значение - расстояние до этой вершины. Граф представляется в 
	виде матрицы смежности.
"""
from collections import deque

def main():
	G = [[0,1,1,0,0,0,0],
	     [1,0,0,1,0,1,0],
	     [1,0,0,1,0,0,0],
	     [0,1,1,0,1,0,0],
	     [0,0,0,1,0,1,1],
	     [0,1,0,0,1,0,0],
	     [0,0,0,0,1,0,0]]
	result = BFS(G)
	print(result)
	
#Обход графа в ширину
def BFS(G):
	Q = deque()
	level = 1
	tmp = 0
	L = {}

	Q.append(0)
	L[0] = 0

	while len(Q) != 0:
		i = Q[0]
		for j in range(0,len(G)):
			if G[i][j] == 1 and not in_dictionary(L,j):
				Q.append(j)
				L[j] = level
				tmp = 1
		if tmp == 1:
			level += 1
			tmp = 0
		Q.popleft()
	return L

#Функция для определения наличия индекса key в словаре dict
def in_dictionary(dict, key):
      try:
      	d = dict[key]
      	return True
      except LookupError:
      	return False


if __name__ == "__main__":
	main()