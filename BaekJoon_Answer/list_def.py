'''
리스트와 내장함수(1)
'''
import random as r
'''
a=[]
print(a)
b=list()
print(b)

a=[1,3,4,5,6]
print(a)
print(a[0])
b=list(range(1,int(round(r.random(),1)*10)))

c=a+b
'''
'''
a=[1,2,3,4,5,6]
a.append(1)
a.insert(2,2)
print(a)
a.pop(0)
print(a)
a.remove(4)
print(a)
print(a.index(6))
'''
a=list(range(1,11))
print(a)
print(sum(a)) # sum함수는 a라는 리스트의 값들을 모두 더해준다.
print(max(a))
print(min(a))
print(min(7,5)) # 두개 인자중 작은 하나의 값을 찾아줌
print(min(7,3,5))
r.shuffle(a)
print(a)
a.sort(reverse=True)
print(a)
a.clear()
print(a)