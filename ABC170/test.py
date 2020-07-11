import sys
import numpy as np
from numba import njit
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
@njit('(i4[::1],)', cache=True)
def solve(A):
    count = np.zeros(10**6 + 10, np.int32)
    for x in A:
        if count[x] > 1:
            continue
        count[::x] += 1
    ret = 0
    for x in A:
        ret += count[x] == 1
    return ret
 
A = np.array(read().split(), np.int32)[1:]
 
print(solve(A))