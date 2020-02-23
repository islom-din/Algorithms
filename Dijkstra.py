"""
	Алгоритм Дейкстры для поиска кратчайших путей
	во взвешанном графе.
"""
import myDeque
import DFS

def main():
	G = [[0,2,0,0,0,0,0,15,0],
		 [2,0,1,5,0,0,0,0,0],
		 [0,1,0,3,0,2,1,0,0],
		 [0,5,3,0,6,4,0,0,0],
		 [0,0,0,6,0,7,0,0,2],
		 [0,0,2,4,7,0,1,3,0],
		 [0,0,1,0,0,1,0,0,0],
		 [15,0,0,0,0,3,0,0,12],
		 [0,0,0,0,2,0,0,12,0]]	

	weights = dijkstra(G,0)
	print(recover_way(G,weights,0,8))

#Алгоритм Дейкстры
def dijkstra(G, start):
	Q = myDeque.myDeque()
	weights = {}
	L = []

	Q.push(start)
	weights[start] = 0
	for i in range(0,len(G)):
		if i == start:
			continue
		weights[i] = 1000000 #имитация бесконечности

	while Q.length() != 0:
		i = Q.topL()
		if not DFS.in_list(L,i):
			for j in range(0,len(G)):
				if G[i][j] > 0:
					Q.push(j)
					put_weight(Q,G,weights,i,j)
			L.append(Q.topL())
		Q.pop()
	return weights

#Восстановление пути от start до finish
def recover_way(G, weights, start, finish):
	way = ""
	i = finish
	while i >= 0:
		if i == start:
			way += str(i)
			break
		for j in range(0,len(G)):
			if weights[i] - G[i][j] == weights[j]:
				way += str(i) + " --> "
				i = j
				break
	return way



#Добавление минимального веса к вершине
def put_weight(Q,G,weights,i,j):
	n1 = weights[Q.topR()]
	n2 = weights[Q.topL()]
	n2 += G[i][j]
	if n2 < n1:
		weights[Q.topR()] = n2

if __name__ == "__main__":
	main()