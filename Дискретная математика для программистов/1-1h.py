# from collections import deque

vert = 'abcdefg'
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

used_edge = set()
visited_v = []
start_v = 'a'


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


def bfs(v, graph, used_edge):
    value = []
    temp_dict = dict()
    for i in graph[v]:
        if v + i not in used_edge:
            used_edge.add(v + i)
            value.append(edges[v + i])
            temp_dict[v + i] = edges[v + i]
    edge = get_key(temp_dict, min(temp_dict.values()))
    used_edge.add(edge)
    new_v = edge.replace(v, '')
    bfs(new_v, graph, used_edge)


bfs(start_v, graph, used_edge)
print(used_edge)
