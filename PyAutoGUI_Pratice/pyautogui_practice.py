# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:58:51 2021

@author: Ballhow
"""
import cv2

img = cv2.imread('House.jpg')
(h, w, d) = img.shape
center = (0, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("House", rotated)