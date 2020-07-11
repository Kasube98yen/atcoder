from collections import deque


S = list(input())
T = list(input())



dqS = deque(S)
dqT = deque(T)

cnt = 0

while dqS:
    tempS = dqS.popleft()
    tempT = dqT.popleft()
    if tempS != tempT:
        cnt += 1

print(cnt)