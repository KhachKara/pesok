from collections import deque

v = 'abcdefg'
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

# --------------------- чтобы при каждом запуске не вводить рёбра -----------------
edges = dict(ab=3, ba=3, af=2, fa=2, bc=3, cb=3, bg=6, gb=6, cd=3, dc=3, ce=2, ec=2, cg=1, gc=1, de=5, ed=5, eg=3, ge=3,
             fe=4, ef=4, fg=3, gf=3)
# ---------------------------------------------------------------------------------


def get_key(d, value):
    for kk, vv in d.items():
        if vv == value:
            return kk


visited_v = {i: None for i in v}
distance = 0
path = []
start_v = 'a'
queue = deque(start_v)
cur_v = start_v
while queue:
    cur_v = queue.popleft()
    neigh_v = []
    if not visited_v[cur_v]:
        visited_v[cur_v] = cur_v
        neigh_v = graph[cur_v]
        temp = dict()
        minimum = 999
        for i in neigh_v:
            temp[i] = edges[cur_v + i]
            if edges[cur_v + i] < minimum and not visited_v[i]:
                if i not in queue:
                    queue.appendleft(i)
                else:
                    queue.remove(i)
                    queue.appendleft(i)
                minimum = edges[cur_v + i]
        next_v = str(get_key(temp, minimum))
        path.append(cur_v + next_v)
        print(cur_v + next_v)
        cur_v = next_v
print(path)
