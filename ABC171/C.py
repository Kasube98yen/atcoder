from collections import deque

def main():
    N = int(input())
    l = deque()
    mozi = list("abcdefghijklmnopqrstuvwxyz")
    a, b = divmod(N, 26)
    N -= 1

    while True:
        a, b = divmod(N, 26)
        l.appendleft(mozi[b])
        N = a
        N -= 1
        if a == 0:
            break

    print("".join(l))


main()