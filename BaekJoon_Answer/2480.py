A,B,C =map(int,input().split(' '))

if A==B and B==C and A==C:
    print(10000+(A*1000))
elif A==B and B!=C and A!=C:
    print(1000+(A*100))
elif A!=B and B!=C and A!=C:
    if A > B and A > C:
        result = A
    elif B > C:
        result = B
    else:
        result = C
    print(result*100)