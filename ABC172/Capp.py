from collections import deque

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    dA = deque([0] + A)
    dB = deque([0] + B)

    sumA = sum(A)
    sumB = sum(B)
    sumall = sumA + sumB
    lenall = len(A) + len(B) 
    Atmp = [0,0]
    Btmp = [0,0]

    Atmp[1] = dA.pop()
    Btmp[1] = dB.pop()

    while sumall > K:
        if Atmp[0] == 0 and dA:
            Atmp[0] = dA.pop()
        if Btmp[0] == 0 and dB:
            Btmp[0] = dB.pop()
        if not dA and not dB:
            print(0)
            return
        if sumA >= sumB:
            sumall -= Atmp[1]
            sumA -= Atmp[1]
            lenall -= 1
            Atmp[1] = Atmp[0]
            Atmp[0] = 0 
        else:
            sumall -= Btmp[1]
            sumB -= Btmp[1]
            lenall -= 1
            Btmp[1] = Btmp[0]
            Btmp[0] = 0 
    print(lenall)
                 
solve()