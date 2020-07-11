from collections import deque

def main():
    N, K = map(int, input().split())
    p = list(map(int,input().split()))

    p.sort()

    q = deque(p)

    ans = 0
    for _ in range(K):
        ans += q.popleft()

    print(ans)

if __name__ == "__main__":
    main()