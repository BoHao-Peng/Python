# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:10:37 2021

@author: Ballhow
"""
import numpy as np
import matplotlib.pyplot as plt

data_len = 50
numlist = np.arange(data_len) + 1
index = np.arange(data_len)
np.random.shuffle(numlist)

fig, ax = plt.subplots()
plt.title('Bubble Sort')

bardata = ax.bar(index, numlist, color = 'b')

for i in range(data_len):
    for j in range(data_len - i - 1):
        if numlist[j] > numlist[j+1]:
            numlist[j], numlist[j+1] = numlist[j+1], numlist[j];
            bardata[j].set_height(numlist[j])
            bardata[j+1].set_height(numlist[j+1])
            bardata[j+1].set_color('r')
            fig.canvas.draw()
            fig.canvas.flush_events()
            bardata[j+1].set_color('b')