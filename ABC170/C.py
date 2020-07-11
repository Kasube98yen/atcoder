import numpy as np

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))

    p.sort()
    q = p
    ans = list(map(lambda _: abs(_ - x), q))

    cnt = 0
    while cnt <= 101:
        if ans.count(cnt) == 2 and cnt != 0:
            pass
        elif ans.count(cnt) == 1 and cnt == 0:
            pass
        else:
            if (x - cnt) in p:
                return x + cnt
            else:
                return x - cnt

        cnt += 1    
    


if __name__ == "__main__":
    print(main())