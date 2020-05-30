
K = int(input())
S = list(input())

if K < len(S):
    S = S[:K] 
    S.append("...")

print("".join(S))