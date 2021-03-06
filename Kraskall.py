"""
	Алгоритм Краскала для нахождения минимального остовного дерева.
	Остовное дерево возвращается в виде списков смежности.
"""

import sort

def main():
	G = [[0,0,0,1,4,0],
	     [0,0,11,0,3,0],
	     [0,11,0,7,0,2],
	     [1,0,7,0,15,0],
	     [4,3,0,15,0,0],
	     [0,0,2,0,0,0]]

	ostov_tree = kraskal(G)
	print(ostov_tree)

#Алгоритм Краскала
def kraskal(G):
	Tree = {}
	levels = {}
	edges = getEdges(G)
	level = 1
	sum_of_weight = 0
	"""Добавляем пустые списки каждому ребру,
	   в этих списках будут храниться вершины,
	   инцидентные рёбрам.
	"""
	for k, v in edges.items():
		Tree[v[0]] = []
		Tree[v[1]] = []
	
	for k, v in edges.items():
		if not in_dictionary(levels,v[0]):
			if in_dictionary(levels,v[1]):
				levels[v[0]] = levels[v[1]]
				Tree[v[0]].append(v[1])
				Tree[v[1]].append(v[0])
				sum_of_weight += k
			else:
				levels[v[0]] = level
				levels[v[1]] = level
				Tree[v[0]].append(v[1])
				Tree[v[1]].append(v[0])
				sum_of_weight += k
				level += 1
		elif not in_dictionary(levels, v[1]):
			if in_dictionary(levels, v[0]):
				levels[v[1]] = levels[v[0]]
				Tree[v[0]].append(v[1])
				Tree[v[1]].append(v[0])
				sum_of_weight += k
			else:
				levels[v[0]] = level
				levels[v[1]] = level
				Tree[v[0]].append(v[1])
				Tree[v[1]].append(v[0])
				sum_of_weight += k
				level += 1
		else:
			if levels[v[0]] < levels[v[1]]:
				n = levels[v[0]]
				for key, value in levels.items():
					if value == n:
						levels[key] = levels[v[1]]
				Tree[v[0]].append(v[1])
				Tree[v[1]].append(v[0])
				sum_of_weight += k
			elif levels[v[0]] > levels[v[1]]:
				n = levels[v[1]]
				for key, value in levels.items():
					if value == n:
						levels[key] = levels[v[0]]
				Tree[v[1]].append(v[0])
				Tree[v[0]].append(v[1])
				sum_of_weight += k
	print("sum of weight = " + str(sum_of_weight))
	return Tree					

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
	return sort_dict(edges)

#Сортировка по индексам словаря
def sort_dict(edges):
	indexes = []
	result = {}
	for k, v in edges.items():
		indexes.append(k)
	#Сортировка слиянием (код в файле sort.py)
	sort.merge_sort(indexes)
	for i in indexes:
		for k, v in edges.items():
			if i == k:
				result[i] = v
	return result

#Функция для определения наличия индекса key в словаре dict
def in_dictionary(dict, key):
      try:
      	d = dict[key]
      	return True
      except LookupError:
      	return False

if __name__ == "__main__":
	main()