"""
	Алгоритм Прима для поиска минимального остовного дерева.
"""

def main():
	G = [[0,1,7,0,0],
	     [1,0,3,2,0],
	     [7,3,0,3,5],
	     [0,2,3,0,4],
	     [0,0,5,4,0]]
	print(Prim(G))

#Алгоритм Прима
def Prim(G):
	S = {}
	heap = {}
	result = {}
	S[0] = 1
	edge = ""
	minEdge = ""
	for i in range(1, len(G)):
		S[i] = 0
	#Начнём с первой вершины
	i = 0 
	while 1 == 1:
		for j in range(0, len(G)):
			if G[i][j] > 0:
				edge = str(i) + str(j)
				heap[edge] = G[i][j]
		while 1 == 1:
			minEdge = getMinEdge(heap)
			print(minEdge)
			if S[int(minEdge[0])] == 1 and S[int(minEdge[1])] == 1:
				heap.pop(minEdge)
			else:
				if S[int(minEdge[0])] == 1:
					S[int(minEdge[1])] = 1
					i = int(minEdge[1])
					result[minEdge] = heap[minEdge]
					heap.pop(minEdge)
					break
				elif S[int(minEdge[1])] == 1:
					S[int(minEdge[1])] = 1
					i = int(minEdge[0])
					result[minEdge] = heap[minEdge]
					heap.pop(minEdge)
					break
		counter = 0
		for k, v in S.items():
			if v == 1:
				counter += 1
		if counter == len(S):
			break
	return result	

	

#Получение минимального веса среди рёбер (возвращаются вершины, инцидентные данному ребру)
def getMinEdge(dict):
	min = 0
	for k, v in dict.items():
		min = v
		break
	for k, v in dict.items():
		if min > v:
			min = v
	for k, v in dict.items():
		if v == min:
			return k

if __name__ == "__main__":
	main()