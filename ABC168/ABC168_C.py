import math

A, B, H, M = map(int, input().split())

jihari = 30 * H + 1 / 2 * M
hunhari = 6 * M 

theta = abs(jihari - hunhari)
thetarad = math.radians(theta)

l = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(thetarad))

print(l)