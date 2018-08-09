# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 14:21:40 2018

@author: 66411
"""
from Digraph import Digraph
from Node import Node
from Edge import Edge
from graph import Graph
def permutation( num_of_student,students_name ):
    avail_student=list(students_name)
    if(num_of_student==2):
#        mid=avail_student
#        avail_student.reverse()
#        print(mid)
#        print(avail_student)
        mid=avail_student.copy()
        avail_student.reverse()
        return [avail_student,mid]
    result=[]
    for student in students_name:
        avail_student=list(students_name)
        avail_student.remove(student)
        back=permutation(num_of_student-1,avail_student)
        for permu in back:
#            result.append([student].extend(permu))
            subpermu=[student]
            subpermu.extend(permu)
#            result.append(subpermu.extend(permu))
            result.append(subpermu)
    return result

def build_class_graph(graphtype):
    g=graphtype()
    for substring in permutation(3,'ABC'):
        vertice=' '.join(substring)
        g.addNode(Node(vertice))
        
    
            
           
    