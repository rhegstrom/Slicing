# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 18:09:12 2022

@author: Roger Hegstrom (rhegstrom@avc.edu)

Use numpy.array to define a 3-by-7 array, A.  
In array location (i,j), row i, column j,  put the number i*j

Use slicing to produce and print:
    1)  row 2 of A
    2) row 2 of A in reverse order
    3) the sub-matrix consisting or the bottom right 2x2 sub-array 
    4) the sub-array consisting of the bottom left 2x2 sub-array
    5) the 3x3 sub-array in the middle of A
"""

import numpy as np

# Initalize nparray A to shape 3-by-7 array
A = np.zeros(shape=(3,7), dtype=np.int8)

# In array locations (i, j) put the number i * j
for i in range(3):
    for j in range(7):
        A[i,j] = i * j
    


# 1)  row 2 of A
print(f'Row 2 of A is {A[1]}')

# 2) row 2 of A in reverse order
print(f'Row 2 of A, reverse order, is {A[1,::-1]}', end="\n\n")

# 3) the sub-matrix consisting or the bottom right 2x2 sub-array 
print(A[1:,5:], end="\n\n")

# 4) the sub-array consisting of the bottom left 2x2 sub-array
print(A[1:,0:2], end="\n\n")

# 5) the 3x3 sub-array in the middle of A
print(A[0:,2:5])