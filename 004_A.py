from math import sqrt
from operator import sub

def Distance(a :list, b :list) -> float:
    vec1 = list(map(sub,a,b))
    return sqrt(sum(map(lambda x: x**2, vec1)))

def main():
    N = int(input())
    pnt = [list(map(int,input().split())) for _ in range(N)]
    maxdist = 0

    for i in range(N-1):
        for j in range(N):
            temp = Distance(pnt[i],pnt[j])
            if maxdist < temp:
                maxdist = temp
    
    print(maxdist)

if __name__ == "__main__":
    main()


