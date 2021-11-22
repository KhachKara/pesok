# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:31:24 2019

@author: khach
"""
Object = {'a': 5, 'b': 11}

class Graph(Object):
    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict
        
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

a = Graph()
a.add_vertex = 'a'
print(a)