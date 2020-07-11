
def main():
    x, y = map(int, input().split())

    tsuru = x
    kame = 0

    while tsuru >= 0:
        if tsuru * 2 + kame * 4 == y:
            return "Yes"
        tsuru -= 1
        kame += 1
    

    return "No"

if __name__ == "__main__":
    print(main())

