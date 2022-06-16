import sys
A = int(sys.stdin.readline())
for i in range(1,A+1):
    a,b = map(int,sys.stdin.readline().split(' '))
    c=a+b
    print('Case #%d: %d'%(i,c))