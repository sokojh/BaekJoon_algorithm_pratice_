'''
리스트와 내장함수(2)
'''
a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i],end=" ")
print()
for x in a:
    print(x,end=" ")
for x in a:
    if x%2==1:
        print(x,end=" ")
tuple_a=()
for x in enumerate(a): #인덱스와 같이 튜플로 묶어주는 방식
    tuple_a +=x
print(tuple_a)
for x in enumerate(a):
    print(x[0],x[1])
print()
for index,value in enumerate(a):
    print(index,value)
print()
if all(60>x for x in a): # all함수는 하나라도 거짓이면 False 리턴 모두 맞으면 True 리턴
    print("YES")
else:
    print("NO")

if any(11>x for x in a): # any함수는 하나라도 참이면 그러면 참
    print("YES")
else:
    print("NO")