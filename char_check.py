size = int(input('Enter the number of words for the array:'))
a = []

for i in range(size):
    value = input('Enter your word:')
    a.append(value)
print('The original array:')
print(a)

for i in range(1,size):

    tmp = a[i]
    j=i-1

    while j>=0 and tmp.lower()<a[j].lower():
        a[j+1] = a[j]
        j-=1
    a[j+1] = tmp
print('The sorted array:')
print(a)        
