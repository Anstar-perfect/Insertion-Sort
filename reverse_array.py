a = [3,5,7,9]

start = 0
end =len(a)-1

while start<end:
    a[start],a[end] = a[end],a[start]
    start +=1 
    end -=1

print('Reversed Array:')
print(a)    