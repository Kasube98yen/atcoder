import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [1] * (N)
    B.append(0)
    sumA = sum(A)
    ans = 0

    # if A[0] == 1 and N == 0:
    #     print(1)
    #     return
    # elif A[0] > 1:
    #     print(-1)
    #     return

    for i in range(1,N):
        sumA -= A[i]
        B[i] = min(2 * B[i-1] - A[i], sumA)
        if B[i] < 0:
            print(-1)
            return

    print(sum(A+B))

if __name__ == "__main__":
    main()

