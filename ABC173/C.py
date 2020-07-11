import copy

def solve():
    H, W, K = map(int,input().split())
    C = [list(input()) for _ in range(H)]

    ans = 0

    for bitH in range(2**(H) - 1):
        for bitW in range(2**(W) - 1):
            Ctmp = copy.deepcopy(C)
            for i in range(H):
                if((bitH >> i) & 1):
                    Ctmp[i] = ["x" for _ in range(W)]
            Ctmp_t = [list(x) for x in zip(*Ctmp)]
            
            for j in range(W):
                if((bitW >> j) & 1):
                    Ctmp_t[j] = ["x" for _ in range(H)]
            
            Clast = [list(x) for x in zip(*Ctmp_t)]
            
            cnt = 0
            
            for s in range(H):
                cnt += Clast[s].count("#")
            
            if cnt == K:
                ans += 1
            
            # for i in range(H):

            # #     print(Clast[i])
            # # print(bitH, bitW)
            # # print(cnt)
    print(ans)

solve()