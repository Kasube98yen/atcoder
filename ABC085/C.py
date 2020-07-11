def main():
    N, Y = map(int,input().split())
    x, y, z = [0, 0, 0]
    
    for i in range(N + 1):
        for j in range(N + 1 - i):
            if i * 10000 + j * 5000 + (N-i-j) * 1000 == Y and N-i-j >= 0:
                print(i, j , N-i-j)
                return
    
    print(-1, -1, -1)

if __name__ == "__main__":
    main()
