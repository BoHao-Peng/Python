# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:01:07 2021

@author: Ballhow
"""

import numpy as np
import matplotlib.pyplot as plt

def QuickSort(array, term = 0):
    dlen = len(array)
    if dlen <= 1:
        return array
    else:
        pIndex = dlen - 1 # The end of data index
        sIndex = 0
        for i in range(dlen-1):
            if array[i] < array[pIndex]:
                array[sIndex], array[i] = array[i], array[sIndex]
            # Plot 
                bardata[term + sIndex].set_height(array[sIndex])
                bardata[term + i].set_height(array[i])
                bardata[term + sIndex].set_color('r')
                fig.canvas.draw()
                fig.canvas.flush_events()
                bardata[term + sIndex].set_color('b')
            # Plot end
                sIndex += 1
                
        array[sIndex], array[pIndex] = array[pIndex], array[sIndex]
    # Plot 
        bardata[term + sIndex].set_height(array[sIndex])
        bardata[term + pIndex].set_height(array[pIndex])
        bardata[term + sIndex].set_color('r')
        fig.canvas.draw()
        fig.canvas.flush_events()
        bardata[term + sIndex].set_color('b')
    # Plot end
        QuickSort(array[:sIndex], term)
        QuickSort(array[sIndex+1:], term + sIndex + 1)

# ------------ main code ---------------------
data_len = 100
numlist = np.arange(data_len) + 1
index = np.arange(data_len)
np.random.shuffle(numlist)

fig, ax = plt.subplots()
plt.title('Quick Sort')

bardata = ax.bar(index, numlist, color = 'b')

QuickSort(numlist)