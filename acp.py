size = int(input('Enter the number of values for array:'))
a=[]
for i in range(size):
    value = int(input('Enter your integer value:'))
    a.append(value)


print('Original Array:')
print(a)  
for i in range(1,size):

    tmp = a[i]
    j = i-1

    while j>=0 and tmp<a[j]:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = tmp

print('The sorted Array:')
print(a)
      
