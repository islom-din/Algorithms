"""
	Алгоритм Дейкстры для поиска кратчайших путей
	во взвешанном графе.
"""
def main():
	G = read_graph()
	start = input("С какой вершины начать?")
	while start not in G:
		start = input("Такой вершины в графе нет. С какой вершины начать?")
	shortest_distances = dijkstra(G,start)
	finish = input("До какой вершины?")
	while start not in G:
		start = input("Такой вершины в графе нет. До какой вершины?")
	shortest_path = reveal_shortes_path(G,start,finish,shortest_distances)


def dijkstra(G, start):
	Q = deque()
	S = {}
	S[start] = 0
	Q.push(start)
	while Q:
		v = Q.pop()
		for u in G[v]:
			if u not in S or S[v] + G[v][u] < S[u]:
				S[u] = S[v] + G[v][u]
				Q.push(u)



#Считывание графа
def read_graph():
	M = int(input()) #количество рёбер
	G = {}
	for i in range(M):
		a, b, weight = input().split()
		weight = float(weight)
		add_edge(G, a, b, weight)
		add_edge(G, b, a, weight)
	return G

#Добавление ребра в исходный граф
def add_edge(G, a, b, weight):
	if a not in G:
		G[a] = {b: weight}
	else:
		G[a][b] = weight
	


if __name__ == "__main__":
	main()