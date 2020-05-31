import math

A, B = input().split()
A = int(A)
B = float(B)

# 小数を各数字にまとめる
# B_sho, B_sei = math.modf(B)
# print(B_sei, B_sho)
# B_sei = int(B_sei)
# B_sho = int(B_sho*100)
# B_sho1, B_sho2 = divmod(B_sho,10)

B_fix = int(round(B*100))
B_sei, B_sho = divmod(B_fix,100)
B_sho1, B_sho2 = divmod(B_sho, 10)

# print(B_sei, B_sho1,B_sho2)

ans = 100 * A * B_sei + 10 * A * B_sho1 + 1 * A * B_sho2

ans = ans // 100

print(ans)