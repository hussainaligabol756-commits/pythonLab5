numbers=(10,15,20,25,30,35,40)

even=0
odd=0

for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("The total even numbers: ",even)
print("The total odd numbers: ",odd)
        