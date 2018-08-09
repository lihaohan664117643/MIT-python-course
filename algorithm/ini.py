# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:34:35 2018

@author: 66411
"""

def getSublists(L, n):
    length=len(L)
    sublist=[]
    i1=0
    while i1<=length-4:
        the_first=L[i1]
        i2=i1+1
        while i2<=length-3:
            print(i2)
            the_second=L[i2]
            i3=i2+1
            while i3<=length-2:
                the_third=L[i3]
                i4=i3+1
                while i4<=length-1:
                    the_fourth=L[i4]
                    i4+=1
                    sublist.append((the_first,the_second,the_third,the_fourth))
                i3+=1
            i2+=1
        i1+=1
    return sublist
    

def getSublists(L, n):
    length=len(L)
    sublist=[]
    i1=0
    while i1<=length-n:
        the_first=L[i1]
        i4=i1+n-1
        sub=L[i1:i4+1]
        sublist.append(sub)
        i1+=1

    return sublist

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    val=aDict.values()
    ans=[]
    sorted_list=sorted(val)
    length=len(sorted_list)
    if length<2:
        return sorted_list
    else:
        for i in range(0,length):
            if i+1<=length-1:
                
                if i==0 and sorted_list[i]!=sorted_list[i+1]:
                    ans.append(sorted_list[i])
                elif sorted_list[i]!=sorted_list[i+1] and sorted_list[i]!=sorted_list[i-1]:
                    print(i)
                    ans.append(sorted_list[i])
            elif i==length-1 and sorted_list[i]!=sorted_list[i-1]:
                ans.append(sorted_list[i])
                
        return ans
