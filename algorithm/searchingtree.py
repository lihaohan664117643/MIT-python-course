# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:32:49 2018

@author: 66411
"""

def maxVal(toConsider):
    if toConsider==[] :
        return [],[]
    else:
        nextItem=toConsider[0]  
        print('a'+str(toConsider[1:]))
        withToTake,withoutToTake=maxVal(toConsider[1:])
#        print('a'+str(withToTake))
        print('b'+str(toConsider[1:]))
        print('nextItem_'+str(nextItem))
        judge_without=True
        withoutToTake,withoutToTake=maxVal(toConsider[1:])
#        print('b'+str(withoutToTake))
    
    print('why')
    if withToTake!=[] or withoutToTake!=[]:
        withoutToTake.append(nextItem)
    print('result_2'+str(withoutToTake))
    withToTake.append(nextItem)
    print('result'+str(withToTake))
    return withToTake,withoutToTake