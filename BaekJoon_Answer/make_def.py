'''
함수 만들기
'''
'''
def add(a,b):
    c=a+b
    print(c)

add(3,2)
add(5,7)
def add(a,b):
    c=a+b
    return c #함수를 종료되는 역할도 함
print(add(3,2)+3)


def add(a,b):
    c=a+b
    d=a-b
    return c,d #튜플로 리턴, 값을 여러개 리턴 할 수 있다.
print(add(3,2))
'''
def isPrime(x):  #소수 출력하는 방법
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=[12,13,7,9,19]

for y in a:
    if isPrime(y):
        print(y,end=" ")