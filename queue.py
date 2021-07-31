# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:48:16 2021

@author: Burak
"""
# from queue import Queue
import queue

# q = Queue()
q = queue.Queue()

list = [5,8,6,11,75]

q.put(15)

for i in range(len(list)):
    q.put(list[i])


while q.empty()==False:
    print(q.get())
    

