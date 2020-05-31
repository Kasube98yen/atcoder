import math
import numpy as np

N = int(input())
A = list(map(int,input().split()))
ans = 1
A_log = A
try:
    A_log = list(map(math.log10,A))
except ValueError:
    print(0)
else:
    if sum(A_log) > 18:
        print(-1)
    else:
        for i in A:
            ans *= i
        if ans <= 1e18:
            print(ans)
        else:
            print(-1)