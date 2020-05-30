
N = int(input())

N_ichi = N % 10

if N_ichi == 3:
    print("bon")
elif N_ichi == 0 or N_ichi == 1 or N_ichi == 6 or N_ichi == 8:
    print("pon")
else:
    print("hon")