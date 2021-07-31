# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:14:40 2021

@author: Burak
"""

import minHeap

heap = minHeap.Heap()
heap.insert(55)
heap.insert(44)
heap.insert(11)

print(heap.getMin())
