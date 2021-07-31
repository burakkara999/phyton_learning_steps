# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:27:16 2021

@author: Burak
"""
# BUBBLE SORT

def bubbleSort(list):
    n = len(list)
    
    for x in range(n):
        
        isSorted = True
        
        for y in range(n-x-1):
            if list[y]>list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
                
                isSorted = False
        
        if isSorted == True:
            break
        
list = [22,9,18,28,17,24,19]
bubbleSort(list)
print(list)
