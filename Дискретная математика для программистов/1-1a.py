N, M = 7, 11
vert = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
neighbours = {'A': ('B', 'F'),
              'B': ('A', 'C', 'G'),
              'C': ('B', 'D', 'E', 'G'),
              'D': ('C', 'E'),
              'E': ('C', 'D', 'F', 'G'),
              'F': ('A', 'E', 'G'),
              'G': ('B', 'C', 'E', 'F')}
edgesCoast = {'AB': 3, 'BA': 3,
              'BC': 3, 'CB': 3,
              'CD': 3, 'DC': 3,
              'DE': 5, 'ED': 5,
              'EF': 4, 'FE': 4,
              'FA': 2, 'AF': 2,
              'BG': 6, 'GB': 6,
              'CG': 1, 'GC': 1,
              'EG': 3, 'GE': 3,
              'FG': 3, 'GF': 3,
              'CE': 2, 'EC': 2
              }
path = []
visited =[]
startVertex = 'A'
z = 0
while z < N:
    def f_path(v):
        path = []
        minimum = [999]
        mini = 0
        for i in neighbours[v]:
            if i not in visited:
                if edgesCoast[v+i] < min(minimum):
                    path = v+i
            minimum.append(edgesCoast[v+i])
        return path
    path.append(f_path(startVertex))
    visited.append(startVertex)
    startVertex = f_path(startVertex).replace(startVertex, '')
    z += 1
dist = 0
for i in path:
    dist += edgesCoast[i]
print(startVertex)
