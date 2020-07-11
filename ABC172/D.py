import math
N = int(input())

ans = 0
for i in range(1,N+1):
    K = int(N/i)
    anstemp = i * K * (K+1) // 2
    ans += anstemp
print(ans)