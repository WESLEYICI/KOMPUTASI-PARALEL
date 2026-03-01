# simd_addition.py
# SIMD Example - Vector Addition

import numpy as np

# Data (Multiple Data)
A = np.array([1, 2, 3, 4])
B = np.array([10, 20, 30, 40])

# Single Instruction (C = A + B)
C = A + B   # ini dijalankan sekaligus (vectorized)

print("A =", A)
print("B =", B)
print("C = A + B =", C)