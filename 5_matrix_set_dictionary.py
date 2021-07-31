# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:40:09 2021

@author: Burak
"""

#MATRIX
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
# TRANSPOSE:
matrixT = [[row[i] for row in matrix]for i in range(4)]

#transposed = []
#for i in range(4):
#   transposed.append([row[i] for row in matrix])

print(matrixT)


# del
a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)


#SET
basket = {'banana','apple','cherry','orange','orange', 'banana'}
print(basket) #NO DUPLICANT!!!

b=set('abracadabra')
print(b) #unique letters
# a-b, a|b, a^b, a&b


#DICTIONARY !!!
# use keys as array, int, or int Tuples

tel = {'burak': 5454, 'ayse':3535}
tel['furkan'] =3434
print(tel)
print(tel['burak']) #takes key-> gives variable
sorted(tel)
print(tel)
'burak' in tel #TRUE
'furkan' not in tel #FALSE

d= dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
for x in list(d):
    print(d[x])
    
for x,y in d.items():
    print(x,y)
    

#ZIP()
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# SORTED
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)): #IF we dont use set -> multiple variables!
    print(f)
