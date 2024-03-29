from collections import deque

vert = 'abcdefg'
queue = deque(vert)
start_v = 'a'

graph = {'a': ('b', 'f'),
         'b': ('a', 'c', 'g'),
         'c': ('b', 'd', 'e', 'g'),
         'd': ('c', 'e'),
         'e': ('c', 'd', 'f', 'g'),
         'f': ('a', 'e', 'g'),
         'g': ('b', 'c', 'e', 'f')
         }
# edges = dict()
# trash = []
# for key, value in graph.items():
#     for i in range(len(value)):
#         edge1 = key + value[i]
#         edge2 = edge1[::-1]
#         if edge1 not in trash and edge2 not in trash:
#             edges[edge1] = int(input(f'"{key}{value[i]}": '))
#             edges[edge2] = edges[edge1]
#             trash.append(edge1)
#             trash.append(edge2)

# --------------------- чтобы при каждом запуске не вводить рёбра -------------
edges = dict(ab=3, ba=3, af=2, fa=2, bc=3, cb=3, bg=6, gb=6, cd=3, dc=3, ce=2,
             ec=2, cg=1, gc=1, de=5, ed=5, eg=3, ge=3, fe=4, ef=4, fg=3, gf=3)
# -----------------------------------------------------------------------------


def get_key(dict_, value_):
    """
    Возвращает ключ словаря по значению.
    :param value_: значение ключа
    :param dict_: словарь
    :return: ключ
    """
    for key, value in dict_.items():
        if value_ == value:
            return key


new_graph = dict()
while queue:
    print(new_graph.keys())
    queue.remove(start_v)
    min_path = 0
    distance = 0
    path = {start_v + i: None for i in graph[start_v]}
    for i in graph[start_v]:
        if not start_v + i in new_graph.keys() and not i + start_v in new_graph.keys():
            path[start_v + i] = edges[start_v + i]

    next_v = get_key(path, min(path.values()))
    distance += min(path.values())
    min_path += distance
    new_graph[next_v] = distance
    start_v = next_v.replace(start_v, '')

    print(path)
