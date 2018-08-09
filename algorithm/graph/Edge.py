# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:47:18 2018

@author: 66411
"""

class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName()+'->'+self.dest.getName()