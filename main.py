# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:09:12 2022

@author: rhegstrom
Use numpy.array to define a 3-by-7 array, A.  
In array location (i,j), row i, column j,  put the number i*j

"""

import numpy as np

# Initalize nparray A to shape 3-by-7 array
A = np.zeros(shape=(3,7), dtype=np.int8)

# In array locations (i, j) put the number i * j
for i in range(3):
    for j in range(7):
        A[i,j] = i * j
    
print(A)
