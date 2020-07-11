from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    d = dict()

    # dictに格納 O(1)
    for a in A:
        try:
            d[a] += 1
        except KeyError:
            d[a] = 1
    
    ans = 100000000000000000000000000
    ans = 0

    # 一旦ans出す
    for dat in d.items():
        ans += dat[0]*dat[1]

    # B,Cの操作
    # for bc in BC:
    #     try:
    #         d[bc[1]] += d[bc[0]]
    #     except KeyError:
    #         try:
    #             d[bc[1]] = d[bc[0]]
    #         except KeyError:
    #             d[bc[0]] = 0
    #             d[bc[1]] = 0
    #     finally:
    #     # 増減分だけ変更
    #         ans += bc[1]*d[bc[0]] - bc[0]*d[bc[0]]
    #         d[bc[0]] = 0
    #     print(ans)

    # B,Cの操作
    for bc in BC:
        if bc[0] in d:
            if bc[1] in d:
                d[bc[1]] += d[bc[0]]
                ans += bc[1]*d[bc[0]] - bc[0]*d[bc[0]]
                d[bc[0]] = 0
            else:
                d[bc[1]] = d[bc[0]]
                ans += bc[1]*d[bc[0]] - bc[0]*d[bc[0]]
                d[bc[0]] = 0
        else:
            pass
        print(ans)



if __name__ == "__main__":
    main()