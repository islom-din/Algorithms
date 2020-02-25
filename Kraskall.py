"""
	Алгоритм Краскала для нахождения минимального остовного дерева.
"""

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
	return edges



if __name__ == "__main__":
	main()