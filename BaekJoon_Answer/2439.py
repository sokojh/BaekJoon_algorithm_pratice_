import sys
A = int(sys.stdin.readline())

for i in range(1,A+1):
    print(" " * (A - i) + "*" * i)