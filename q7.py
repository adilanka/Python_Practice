def SumofDigits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

n = int(input("Enter the number for the sum of digits: "))
print("Sum of digits is: ",SumofDigits(n))