
def solve():
    N = int(input())
    S = [input() for N in range(N)]
    snames = ["AC", "WA", "TLE", "RE"]
    score = {"AC": 0, "TLE": 0, "WA": 0, "RE": 0}


    for st in S:
        score[st] += 1

    for sname in snames:
        print(sname + " x " + str(score[sname]))

solve()