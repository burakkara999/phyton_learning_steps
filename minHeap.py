# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 23:21:34 2021

@author: Burak
"""

class Heap:
    list =[]
    def _init_(self):
        self.list[0] = -1
        
    def getMin(self):
        minValue = self.list[1]
        
        x = self.list.pop()
        i=1
        
        while x > self.list[2*i] or x > self.list[2*i+1]:
            if x > self.list[2*i] and x > self.list[2*i+1]:
                if self.list[2*i] < self.list[2*i+1]:
                    self.list[i], self.list[2*i] = self.list[2*i], self.list[i]
                    i=2*i
                else:
                    self.list[i], self.list[2*i+1] = self.list[2*i+1], self.list[i]
                    i=2*i+1
            elif x > self.list[2*i]:
                self.list[i], self.list[2*i] = self.list[2*i], self.list[i]
                i=2*i
            else:
                self.list[i], self.list[2*i+1] = self.list[2*i+1], self.list[i]
                i=2*i+1
        return minValue
            
                    
    def insert(self,x):
        self.list.append(x)
        n = len(self.list)-1
        
        
        while self.list[n//2] > x and n!=1:
            self.list[n//2], self.list[n] =self.list[n], self.list[n//2]
            n=n//2
            # if n==0:
                # break


heap = Heap()
heap.insert(15)
heap.insert(22)
heap.insert(14)
heap.insert(11)
heap.insert(18)
heap.insert(28)

print(heap.getMin())
print(heap.getMin())
print(heap.getMin())
        
        