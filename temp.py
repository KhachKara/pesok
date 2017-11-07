# class Counter:
#     """I count. That's all"""
#     def __init__(self, initial=0):  # конструктор
#         self.value = initial        # запись атрибута
#
#         def increment(self):
#             self.value += 1
#
#         def get(self):
#             return self.value

class Counter:
    """I count. That's all"""
    all_counters = []

    def __init__(self, initial=0):  # конструктор
        Counter.all_counters.append(self)

Counter(42)