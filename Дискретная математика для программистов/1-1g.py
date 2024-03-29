from collections import deque

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
visited = set()
start_v = 'b'
ans = []
queue = deque(vert)


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


def bfs(vert, graph, ans):
    visited.add(vert)
    ans.append(vert)


bfs(start_v, graph, ans)

while queue:
    value = []
    temp_dict = dict()
    if start_v in queue:
        neighbor = graph[start_v]
        for i in neighbor:
            if i not in visited:
                temp_dict[start_v + i] = edges[start_v + i]
                value.append(edges[start_v + i])
            else:
                continue
        less_cost = min(value)
        short_path = get_key(temp_dict, less_cost)
        new_v = short_path.replace(start_v, '')
        queue.remove(start_v)
        if new_v not in visited:
            start_v = new_v
            bfs(start_v, graph, ans)

print(ans)
