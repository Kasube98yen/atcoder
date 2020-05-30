
N = int(input())
A = list(map(int, input().split()))
A_leaf = [0] * N
A_leaf.append(2**N)
A_leafans = [0] * N
A_leafans.append(2**N)
answer = 2^(N+1) - 1

def kiru_leaf(lyr, cut_leaf, add_leaf, answer):
    print(lyr, cut_leaf, add_leaf)

    if lyr - 1 == 0:
        answer = answer - cut_leaf
        return answer
    if A[lyr] * 2 < add_leaf:
        return -1
    else:
        A_leafans[lyr] = A[lyr]
        A_leafans[lyr - 1] = add_leaf
        answer = answer - cut_leaf
        for adds in range((A[lyr] - A_leaf[lyr]) // 2 + 1):
            kiru_leaf(lyr - 1, A[lyr] - A_leaf[lyr],adds, answer)

for i in range((A_leaf[N] - A[N]) // 2 + 1):
    print(kiru_leaf(N, A_leaf[N] - A[N], i, answer))

