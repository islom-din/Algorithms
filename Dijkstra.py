"""
	Алгоритм Дейкстры для поиска кратчайших путей
	во взвешанном графе.
"""
def main():
	G = read_grag()
	start = input("С какой вершины начать?")
	while start not in G:
		start = input("Такой вершины в графе нет. С какой вершины начать?")
	shortest_distances = dijkstra(G,start)
	finish = input("До какой вершины?")
	while start not in G:
		start = input("Такой вершины в графе нет. До какой вершины?")
	shortest_path = reveal_shortes_path(start,finish,shortest_distances)




def read_graph():
	M = int(input()) #количество рёбер
	G = {}
	for i in range(M):
		a, b, weight = input().slip()
		weight = float(weight)
		add_edge(G, a, b, weight)
		add_edge(G, b, a, weight)
	return G




if __name__ == "__main__":
	main()