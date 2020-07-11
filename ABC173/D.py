
def solve():
    N = int(input())
    A = list(map(int,input().split()))
    
    Taku = []

    A.sort()
    A.reverse()
    flg = 0

    ans = 0

    for an in A:
        if flg == 0:
            Taku.append(an)
            flg = 1
        else:
            Takudiff = [min(Taku[i], Taku[i-1]) for i in range(len(Taku))]
            Taku.insert(Taku.index(max(Takudiff)), an)
            ans += max(Takudiff)

    print(Taku)

solve()
