# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:01:51 2021

@author: Burak
"""

# More on lists
l = [45,54,34,41,25,59]
# append, insert
l.append(77) #add to the end
l.insert(0, 99) #add where u want

print(l)

for x in range(len(l)):
    print(l[x])
    
# Remove, pop , clear , count, sort ,reverse

print(l.pop(2))
l2=l.copy()
l2.reverse()
print(l2)

# 
squares =[x**2 for x in range(1,11)]
print(squares)

ruleList = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(ruleList)

l3= [(x,x**2) for x in squares]
print(l3)

#extracting numbers 
vec = [[1,2,3], [4,5,6], [7,8,9]]
flatList=[num for elem in vec for num in elem]
print(flatList)

# l.extend()
# print(l)
