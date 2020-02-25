"""
	Алгоритм Краскала для нахождения минимального остовного дерева.
"""

import sort

def main():
	G = [[0,0,0,1,4,0],
	     [0,0,11,0,3,0],
	     [0,11,0,7,0,2],
	     [1,0,7,0,15,0],
	     [4,3,0,15,0,0],
	     [0,0,2,0,0,0]]
	edges = getEdges(G)
	print(edges)

#Вернуть все рёбра и инцидентные им вершины
def getEdges(G):
	edges = {}
	tmp = []
	for i in range(0, len(G)):
		for j in range(0, len(G)):
			if G[i][j] > 0:
				tmp.append(j)
				tmp.append(i)
				edges[G[i][j]] = tmp
				tmp = []
	return sort_1(edges)

#Сортировка по индексам словаря
def sort_1(edges):
	indexes = []
	result = {}
	for k, v in edges.items():
		indexes.append(k)
	sort.merge_sort(indexes)
	for i in indexes:
		for k, v in edges.items():
			if i == k:
				result[i] = v
	return result

if __name__ == "__main__":
	main()