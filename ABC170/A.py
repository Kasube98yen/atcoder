def main():
    x = list(map(int,input().split()))

    for i in range(5):
        if x[i] == 0:
            return(i+1)


print(main())