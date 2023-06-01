count = 0
sum = 0
num = 1
while num != 0:
    num = int(input("Enter some number and enter 0 to find sum and average of the numbers: "))
    sum += num
    count += 1
if count==0:
    print("Enter some numbers please: ")
else:
    print("Sum: ",sum)
    print("Average: ",sum/count)
