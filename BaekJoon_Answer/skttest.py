def sel_sort(a):
    n = len(a)
    count= 0
    array=[]
    for i in range(0, n - 1):
        count =0
        min_idx = i
        
        for j in range(i + 1, n):

            if a[j] < a[min_idx]:
                min_idx = j
                count=count+1


        array.append(count)
        a[i], a[min_idx] = a[min_idx], a[i]

        print(a)  # 정렬 과정 출력하기
        print(array)
    array.append(count)
    print(array)




d = [2,3,4,5,6,1]

sel_sort(d)

print(d)
print(d)