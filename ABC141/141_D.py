def main():
    N, M = map(int, input().split())
    # A_list = list(map(int,input().split())
    A_list = [int() for _ in input().split()]

    # 昇順sort
    A_list.sort()
    A_list.reverse()

    # 最大値取る
    A_max = A_list[0]
    A_max_point = 0

    # 後ろの値と比較,
    for _ in range(M):
        if A_list[A_max_point] < A_list[A_max_point + 1]:
            A_list[A_max_point + 1] = A_list[A_max_point + 1] // 2
            A_max_point = A_max_point + 1
        else:
            A_list[A_max_point] = A_list[A_max_point] // 2
    
    print(sum(A_list))

if __name__ == "__main__":
    main()


