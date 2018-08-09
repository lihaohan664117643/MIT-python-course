# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:28:36 2018

@author: 66411
"""

class Node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    