
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:36:51 2018

@author: 66411
"""
from Digraph import Digraph
from Node import Node
from Edge import Edge
from graph import Graph


def buildCityGraph(graphtype):
    g=graphtype()
    for name in ('Boston','Providence','NewYork','Chicago','Denver','Phoenix','Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'),g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'),g.getNode('NewYork')))
    g.addEdge(Edge(g.getNode('Providence'),g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'),g.getNode('NewYork')))
    g.addEdge(Edge(g.getNode('NewYork'),g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'),g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'),g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'),g.getNode('NewYork')))
    g.addEdge(Edge(g.getNode('Chicago'),g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'),g.getNode('Boston')))
    return g
    
    
    