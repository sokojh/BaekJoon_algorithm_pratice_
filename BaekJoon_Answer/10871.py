import sys
N,X = map(int,sys.stdin.readline().split(' '))
A =sys.stdin.readline().split(' ')
result=[]
for i in range(0,N):
    if(X<int(A[i])):
        result.append(A[i])

print(' '.join(result))