import math
import statistics
import functools
from functools import reduce

# Reduce function
"""
Data = [a1, a2, ..., an]
Function: f(x,y)

reduce(f, data):
Step1: val1 = f(a1, a2)
Step2: val2 = f(val1, a3)
Step3: val3 = f(val2, a4)
...
Step_n-1: val_n-1 = f(val_n-2, an)
"""
# Alternatively: f(f(f(a1, a2), a4), ... , an)
# Multiply all numbers in list
data_reduce = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x * y
print(reduce(multiplier, data_reduce))

multiplier_ = 1
for i in data_reduce:
    multiplier_ *= i
print(multiplier_)


# Filter function
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))

# Remove missing data
countries = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Columbia', '',
             'Ecuador', '', '', 'Venezuela']
print(list(filter(None, countries)))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26),
         ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)

print(list(map(c_to_f, temps)))


def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r ** 2)


radii = [2, 5, 7.1, 0.3, 10]

# Method1: Direct method
areas = []
for r in radii:
    areas.append(area(r))
print(areas)

# Method2: Map method
areas = map(area, radii)
print(list(areas))
