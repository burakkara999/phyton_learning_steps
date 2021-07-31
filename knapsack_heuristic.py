# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:52:08 2021
Knapsack heuristic algorithm***

@author: Burak
"""

import pandas as pd
import numpy as np
import matplotlib as plt

data = pd.read_csv("data_246.csv")

data = pd.DataFrame(data)
data = pd.DataFrame.transpose(data)

# print(data.head(5))

data1 = data.dropna(axis=1,how="all")

# print(data1.head(5))

pi= data1[0]
wi = data1[1]
capacity = data1[3][1]
# print(wi)

itemCount = wi.count()
itemIndex = []
for x in range(1,itemCount):
    itemIndex.append(pi[x]/wi[x])

itemIndex.insert(0,"valuePerW")
data1[4] = itemIndex

new_header = data1.iloc[0] #grab the first row for the header
data1 = data1[1:] #take the data less the header row
data1.columns = new_header #set the header row as the df header

data1.index.name="item"
data1.reset_index(inplace=True)

print(data1.head(15))

data1=data1.sort_values("valuePerW",axis=0,ascending=False,ignore_index=True)

addedItems = []
totalKnapsackValue=0
totalKnapsackW=0
print(data1.head(15))

for x in range(15):
    if capacity < totalKnapsackW + data1["weight"][x]:
        break
    addedItems.append(data1["item"][x])
    totalKnapsackW = totalKnapsackW + data1["weight"][x]
    totalKnapsackValue = totalKnapsackValue + data1["value"][x]

print("Value in knapsack: " , totalKnapsackValue)
print("Weight of knapsack: ", totalKnapsackW)
print("Added items: " , addedItems)
print("Heuristic has been done!!")

