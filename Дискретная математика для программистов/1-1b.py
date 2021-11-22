# coding=utf-8
from collections import deque

v = 'abcdefg'
graph = {'a': ('b', 'f'),
         'b': ('a', 'c', 'g'),
         'c': ('b', 'd', 'e', 'g'),
         'd': ('c', 'e'),
         'e': ('c', 'd', 'g'),
         'f': ('a', 'e', 'g'),
         'g': ('b', 'c', 'e', 'f')
         }
# edges = dict()
trash = []
# for key, value in graph.items():
#     for i in range(len(value)):
#         edge1 = key + value[i]
#         edge2 = edge1[::-1]
#         if edge1 not in trash and edge2 not in trash:
#             edges[edge1] = int(input(f'"{key}{value[i]}": '))
#             edges[edge2] = edges[edge1]
#             trash.append(edge1)
#             trash.append(edge2)
edges = dict(ab=3, ba=3, af=2, fa=2, bc=3, cb=3, bg=6, gb=6, cd=3, dc=3, ce=2, ec=2, cg=1, gc=1, de=5, ed=5, eg=3, ge=3,
             fe=4, ef=4, fg=3, gf=3)

start_v = 'a'
distance = 0
visited_v = {i: None for i in v}
queue = deque([start_v])
path = []

def get_key(d, value):
    for kk, vv in d.items():
        if vv == value:
            return kk

z = 0
cur_v = start_v
while z < len(edges):
    temp = dict()
    # cur_v = queue.popleft()
    # vert.append(cur_v)
    visited_v[cur_v] = cur_v
    for neigh_v in graph[cur_v]:
        if visited_v[neigh_v] is None:
            temp[cur_v + neigh_v] = edges[cur_v + neigh_v]
    if temp.values():
        cur_v = get_key(temp, min(temp.values())).replace(cur_v, '')
        path.append(get_key(temp, min(temp.values())))
        queue.append(cur_v)
        distance += min(temp.values())
    z += 1
for i in graph:
    if i is None:
        for neigh_v in graph[i]:
            print(neigh_v)

print(distance, path)
