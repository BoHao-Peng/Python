# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:04:16 2021

@author: Ballhow
"""

import numpy as np
import matplotlib.pyplot as plt

def MergeSort(array, term = 0):
    dlen = len(array)
    if dlen > 1:
        # Divide the array into minimum length
        mid = int(dlen/2)
        MergeSort(array[:mid], term)
        MergeSort(array[mid:], term + mid)
        # Start Sort
        left_array = list(array[:mid]) + [max(array)]
        right_array = list(array[mid:]) + [max(array)]
        left_index = 0;
        right_index = 0;
        for i in range(dlen):
            if left_array[left_index] < right_array[right_index]:
                array[i] = left_array[left_index]
                left_index += 1
            else:
                array[i] = right_array[right_index]
                right_index += 1
        # Plot update
            bardata[term + i].set_height(array[i])
            bardata[term + i].set_color('r')
            fig.canvas.draw()
            fig.canvas.flush_events()
            bardata[term + i].set_color('b')

data_len = 100
numlist = np.arange(data_len) + 1
index = np.arange(data_len)
np.random.shuffle(numlist)

fig, ax = plt.subplots()
plt.title('Merge Sort')

bardata = ax.bar(index, numlist, color = 'b')

MergeSort(numlist)