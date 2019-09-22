def main():
    N, K, Q = map(int, input().split())
    A_list = [int(input()) for _ in range(Q)]
    player_score = [K for _ in range(N)]

    for player_answer in A_list:
        # 正解者スコア+1して, その後全体-n
        player_score[player_answer - 1] = player_score[player_answer - 1] + 1

    player_score = list(map(lambda i: i - len(A_list), player_score))
    
    for score in player_score:
        print("Yes" if score > 0 else "No")
    
if __name__ == "__main__":
    main()
