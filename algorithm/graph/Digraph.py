# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:55:35 2018

@author: 66411
"""
from Node import Node
from Edge import Edge

class Digraph(object):
    ##该类只有一个属性那就是字典edges
    def __init__(self):
        self.edges={}
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node]=[]
    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        if dest not in self.edges[src]:
            self.edges[src].append(dest)
            
    def childrenOf(self,node):
        return self.edges[node]
    def hasNode(self,node):
        return node in self.edges
    def getNode(self,name):
        for n in self.edges:
            if n.getName()==name:
                return n
        raise NameError(name)
    def __str__(self):
        result=''
        for src in self.edges:
            for dest in self.edges[src]:
                result=result+src.getName()+'->'+dest.getName()+'\n'
        return result[:-1]#omit final newline
        