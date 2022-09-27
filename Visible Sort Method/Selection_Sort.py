# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:01:23 2021

@author: Ballhow
"""

import numpy as np
import matplotlib.pyplot as plt

data_len = 100
numlist = np.arange(data_len) + 1
index = np.arange(data_len)
np.random.shuffle(numlist)

fig, ax = plt.subplots()
plt.title('Selection Sort')

bardata = ax.bar(index, numlist, color = 'b')

for i in range(data_len):
    maxIndex = 0
    for j in range(data_len-i):
        if numlist[j] > numlist[maxIndex]:
            maxIndex = j
            bardata[maxIndex].set_color('r')
            fig.canvas.draw()
            fig.canvas.flush_events()
            bardata[maxIndex].set_color('b')
            
    numlist[-1-i], numlist[maxIndex] = numlist[maxIndex], numlist[-1-i]
    bardata[maxIndex].set_height(numlist[maxIndex])
    bardata[-1-i].set_height(numlist[-1-i])