a = [4,2,9,0,1,5]

for i in range(1,len(a)):

    value = a[i]

    j = i-1
    while j >=0 and value < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = value

print('Sorted Array')
for i in range(len(a)):
    print("%d" %a[i],end=' ')        