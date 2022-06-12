def solution(periods, payments, estimates):
    answer = []
    이번달금액=[]
    다음달금액=[]
    이번달VIP이면서다음달VIP아닌놈 = 0
    이번달VIP아니면서다음달VIP인놈 = 0
    for i in range(len(payments)):
        이번달금액.append(sum(payments[i]))
        다음달금액.append(이번달금액[i] + estimates[i])

    print('이번달금액:' ,이번달금액)
    print('다음달금액:',다음달금액)
    for i in range(len(periods)):
        if periods[i]<=60 and 이번달금액[i]>=480000 :
            if 다음달금액[i] <=600000:
                print()
            else:
                이번달VIP이면서다음달VIP아닌놈 = 이번달VIP이면서다음달VIP아닌놈+1
        elif periods[i]<=24 and periods[i] > 60:
            if 이번달금액[i] < 900000 and 다음달금액[i] >=900000:
                이번달VIP아니면서다음달VIP인놈 = 이번달VIP아니면서다음달VIP인놈+1
            elif 이번달금액[i] < 900000:
                print()
    answer.append(이번달VIP이면서다음달VIP아닌놈)
    answer.append(이번달VIP아니면서다음달VIP인놈)

    return answer

estimates = [100000, 100000, 100000]
periods = [20, 23, 24]
payments = [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]

solution(periods, payments, estimates)