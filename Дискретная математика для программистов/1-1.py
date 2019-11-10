# coding=utf-8
"""
Граф изображает сеть дорог, связывающих семь деревень.
Расстояние между деревнями задано в милях. Используя алгоритм Прима,
найдите сеть дорог минимальной общей длины, охватывающую все деревни.
AB, BA = 3, 3
BC, CB = 3, 3
CD, DC = 3, 3
DE, ED = 5, 5
EF, FE = 4, 4
FA, AF = 2, 2
BG, GB = 6, 6
CG, GC = 1, 1
EG, GE = 3, 3
FG, GF = 3, 3
CE, EC = 2, 2
"""

N, M = 7, 11  # количество вершин и ребер
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
vertexDict = {i: False for i in vertex}  # вершины не посещены
ribsV1 = ['AB', 'BC', 'CD', 'DE', 'EF', 'FA', 'BG', 'CG', 'EG', 'FG', 'CE']  # рёбра
ribsV2 = ['BA', 'CB', 'DC', 'ED', 'FE', 'AF', 'GB', 'GC', 'GE', 'GF', 'EC']  # рёбра в обратную сторону
ribs = ribsV1 + ribsV2  # все рёбра
ribsValue = [3, 3, 3, 5, 4, 2, 6, 1, 3, 3, 2]  # стоимость рёбер
ribsZip = tuple(zip(ribs, ribsValue * 2))
graphValues = {i: tuple([j for j in ribsZip if i == j[0][0]]) for i in vertexDict}
distances = 0
startVertex = vertex[0]


def pathsearch(obj, v):
    edge = ''
    listMinimum = [999]
    nextVertex = ''
    for path, value in obj:
        if value < min(listMinimum) and not vertexDict[v]:
            edge = path
        listMinimum.append(value)

    minumum = min(listMinimum)
    nextVertex = edge.replace(v, '')
    return edge, minumum, nextVertex


path = []
z = 0
nextVertex = 'A'
while z < N:
    if not vertexDict[nextVertex]:
        temp = pathsearch(graphValues[nextVertex], nextVertex)
        path.append(temp[0])
        distances += temp[1]
        nextVertex = temp[2]
        vertexDict[nextVertex] = True
    z += 1
print(path)
