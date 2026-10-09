# Program to print the K pattern
# Kpatern.py

n = 9
for i in range(n):
    for j in range(n):
        if j == 0 or (i + j == n // 2) or (i - j == n // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
