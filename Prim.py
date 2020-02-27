"""
	Алгоритм Прима для поиска минимального остовного дерева.
"""

def main():
	

#Получение минимального веса среди рёбер
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