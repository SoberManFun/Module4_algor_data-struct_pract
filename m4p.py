#___________________МОДУЛЬ_4__УРОВЕНЬ1_НАЧАЛО____________________
# def binary_search(mass, value):
# 	center = len(mass) // 2
# 	left = 0
# 	right = len(mass) - 1
# 	while mass[center] != value and left <= right:
# 		if value > mass[center]:
# 			left = center + 1
# 		else:
# 			right = center - 1
# 		center = (left + right) // 2
# 	if left > right:
# 		print('В данном массиве искомое число отсутствует!')
# 	else:
# 		MassVal = []
# 		i = center
# 		while mass[i] == value and i >= 0:
# 			MassVal.append(i)
# 			i -= 1
# 		i = center + 1	
# 		while mass[i] == value and i < len(mass):
# 			MassVal.append(i)
# 			i += 1
# 		sort_insert(MassVal)
# 		print('Индекс(ы) искомого числа = ', MassVal)
# #___________________МОДУЛЬ_4__УРОВЕНЬ1_КОНЕЦ____________________

# #___________________МОДУЛЬ_4__УРОВЕНЬ2_НАЧАЛО____________________
# def sort_insert(mass):
# 	N = len(mass)
# 	for i in range(1,N):
# 		for j in range(i, 0, -1):
# 			if mass[j] < mass[j-1]:
# 				mass[j], mass[j-1] = mass[j-1], mass[j]
# 			else:
# 				break
# 	return mass
# #___________________МОДУЛЬ_4__УРОВЕНЬ2_КОНЕЦ____________________

# from random import randint
# n = int(input('Введите количество элементов массива: '))
# d = int(input('Введите диапазон значений массива: '))
# m = [randint(-d, d) for i in range(n)]
# sort_insert(m)

# print('Сгенерирован и отсортирован следующий массив: ', m)
# val = int(input('Введите искомое число: '))
# binary_search(m, val)
#___________________МОДУЛЬ_4__УРОВЕНЬ3_НАЧАЛО____________________
# from collections import deque

# def bfs(graph, start):
# 	visited = set()
# 	queue = deque([start])
# 	visited.add(start)
# 	while queue:
# 		vertex = queue.popleft()
# 		print(vertex, end=' ')
# 		for neighbor in graph[vertex]:
# 			if neighbor not in visited:
# 				queue.append(neighbor)
# 				visited.add(neighbor)

# graph = {'1' : set(['2', '5']),
# '2' : set(['3', '4']),
# '3' : set(['2', '4']),
# '4' : set(['2']),
# '5' : set(['1', '6']),
# '6' : set(['5', '8']),
# '7' : set(['5', '8', '9']),
# '8' : set(['7', '9']),
# '9' : set(['7', '8']),}

# print('Результат поиска в ширину:')
# print(bfs(graph, '1'))
#___________________МОДУЛЬ_4__УРОВЕНЬ3_КОНЕЦ____________________