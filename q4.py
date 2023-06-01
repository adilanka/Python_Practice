def PrintPrimeNumbers(n):
    for num in range(1, n + 1):
        if(num>1):
            for i in range(2, num):
                if(num%i == 0):
                    break
            else:
                print(num)

number = int(input("Enter the number n: "))
PrintPrimeNumbers(number)