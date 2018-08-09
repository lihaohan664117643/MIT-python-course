# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:07:13 2018

@author: 66411
"""
def DirDFS(graph,source,destination,path=[],current_path=[]):
    src=graph.getNode(source)
    dest=graph.getNode(destination)
    current_path.append(src.getName())
    if( src.getName()==dest.getName()):
        
        current_path.extend(dest.getName())
        if(len(current_path)<len(path) or len(path)==0 ):
            path=current_path
            
        return path
    print(current_path)
    for subdest in graph.childrenOf(src):
#        if(src.getName()=='Chicago'):
#            print('now chicago '+str(id(current_path)))
#        if(src.getName()=='Denver'):
#            print('now Denver '+str(id(current_path)))        
        print('current source '+src.getName())
#        print(current_path)
        print('subdest: '+subdest.getName())

        if(  subdest.getName()==dest.getName()):
            current_path.append(subdest.getName())
            if(len(current_path)-1<len(path) or len(path)==0):
#                path.extend(current_path)
                 path=current_path
#                return path
            else:
                pass
#                return path
        elif(subdest.getName() not in current_path):
            path=DirBFS(graph,subdest.getName(),destination,path,current_path.copy())
        else:
            pass
#            return path

    return path



def DirBFS(graph,source,destination):
    src=graph.getNode(source)
    dest=graph.getNode(destination)
    initpath=[source]
    pathqueue=[initpath]
    while(len(pathqueue)!=0):
        tmppath=pathqueue.pop(0)
        lastNode=tmppath[-1]
        if lastNode==destination:
            return tmppath
        for nextNode in graph.childrenOf(graph.getNode(lastNode)):
            if nextNode.getName() not in tmppath:
                newPath=tmppath+[nextNode.getName()]
                pathqueue.append(newPath)
    return []
    
    
    
        
        