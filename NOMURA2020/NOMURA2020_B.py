from collections import deque

def main():
    T = input()
    d = deque(T)
    ans = deque()
    nxt = ""
    cnt = 0

    while d:
        now = d.pop()
        if now == "?":
            now = "D"
        ans.appendleft(now)

    print("".join(ans))
    

if __name__ == "__main__":
    main()            