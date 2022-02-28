''' 문자열과 내장함수

print(msg.upper())
print(msg.lower())
print(msg) # 원본은 변하지 않는다.
tmp = msg.upper()
print(tmp)
print(tmp.find("T"))
for i in range(len(msg)):
    print(msg[i], end=" ")
print(len(msg))
for x in msg:
    print(x, end=' ')
'''
msg="It is Time"
for x in msg:
    if x.isupper():
        print(x,end=" ")
print()
for x in msg:
    if x.islower():
        print(x,end=" ")
print()
for x in msg:
    if x.isalpha():
        print(x,end=" ")
tmp ='AZ'
for x in tmp:
    print(ord(x)) #ord는 아스키넘버를 출력함
tmp='az'
for x in tmp:
    print(ord(x))
tmp=65
print(chr(tmp)) #반대로 숫자를 문자로 변환 시켜주는 chr메소드