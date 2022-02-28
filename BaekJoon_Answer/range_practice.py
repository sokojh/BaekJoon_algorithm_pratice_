#a = range(10)  # range 함수는 0부터 9까지 10개의 정수 배열을 만드는 것
#print(list(a)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#b = range(1,11) # 앞에 1을 넣으면 1부터 시작하겠다는 뜻 10까지 하고 싶으면 11로 쓰면 됨.
#print(list(b))
#for i in range(10,0,-2):  #3번째 인자는 줄어드는 방식을 말함.
#    print(i)
'''
i=1
while i<=10:
    print(i)
    i+=1
'''
'''
i=10
while i>=1:
    print(i)
    i=i-1
'''
'''
i=1
while True:
    print(i)
    if i==10:
        break
    i+=1
'''
'''
for i in range(1,11):
    if i%2==0:
        continue # continue는 continue 밑에있는 부분들을 실행 하지 않음
    print(i)
'''
'''
for i in range(1,11):
    print(i)
    if i==5:
        # break #정상적인 종료가 아니라 강제종료이므로 else의 print11은 안나옴
    else:
        print(11)
'''
'''
# 1) 1부터 N까지 홀수 출력하기
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        continue
    print(i)
'''
'''
# 2) 1부터 N까지의 합 구하기
n=int(input())
result =0;
for i in range(1,n+1):
    result += i
print(result)

'''
'''
# 3) N의 약수 출력하기
n=int(input())

for i in range (1,n+1):
    if n%i==0:
        print(i, end=" ")
'''
a=4
b=a/2
print(b,type(b))