'''
람다 함수 = 익명 함수 = 람다 표현식

# 평소 사용하는 함수 방식
def plus_one(x):
    return x+1
print(plus_one(1))

# 람다 방식  그냥 변수에 넣어주면 함수완성    변수 = lambda 파라미터 : 리턴값
plus_two = lambda x: x+2

print(plus_two(1))
'''
def plus_one(x):
    return x+3
a=[1,2,3]
print(list(map(plus_one,a)))
print(list(map(lambda x: x+3,a))) #둘이 값음


