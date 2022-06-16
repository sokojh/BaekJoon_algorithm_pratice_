import sys

A = sys.stdin.readline()
for i in range(0,int(A)):
    a,b= map(int,sys.stdin.readline().split(' '))
    print(a+b)
