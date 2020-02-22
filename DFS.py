"""
	Обход графа в глубину. Функция DFS возвращает словарь из пар {ключ:значение}, где ключ - вершина, 
	а значение это вершина, с которой можно добраться до исходной (той, что в ключе). Входной граф 
	представляется в виде матрицы смежности. По словарю строится остовное дерево и возвращается 
	в виде списка смежности при помощи функции build_tree(L).
"""
import myStack

def main():
	G = [[0,1,0,0,0,0,1,1],
		 [1,0,1,0,0,0,0,0],
		 [0,1,0,1,0,1,0,0],
		 [0,0,1,0,1,0,0,0],
		 [0,0,0,1,0,0,0,0],
		 [0,0,1,0,0,0,0,0],
		 [1,0,0,0,0,0,0,1],
		 [1,0,0,0,0,0,1,0]]
	L = DFS(G)
	tree = build_tree(L)
	print(tree)

#Обход графа в глубину
def DFS(G):
	S = myStack.myStack()
	L = {}
	S.push(0)
	L[0] = 0
	i = S.top()
	while S.length != 0:
		j = get_adjacent_vertex(G,i,S,L)
		if j > 0:
			S.push(j)
			i = S.top()
		if j == -1:
			if i == 0:
				break
			else:
				L[i] = S.underTop()
				S.pop()
				i = S.top()
	return L

#Построение остовного дерева
def build_tree(L):
	tmp = []
	tree = {}
	for i in range(0,len(L)):
		for k, v in L.items():
			if k == 0 and v == 0:
				continue
			if k == i:
				tmp.append(v)
		for k, v in L.items():
			if k == 0 and v == 0:
				continue
			if v == i:
				tmp.append(k)
		tree[i] = tmp
		tmp = []
	return tree


#Функция нахождение смежных вершин
def get_adjacent_vertex(G,i,S,L:list):
	for j in range(0, len(G)):
		if G[i][j] == 1 and not S.hasElem(j) and not in_list(L,j):
			return j
	return -1

#Проверка наличия элемента в списке
def in_list(L,element):
	for elem in L:
		if elem == element:
			return True
	return False

if __name__ == "__main__":
	main()

