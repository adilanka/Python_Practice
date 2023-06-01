def BinaryCoversion(decimal):
    if decimal >=1:
        BinaryCoversion(decimal//2)
    print(decimal%2, end ="")
num = int(input("Enter the decimal number: "))
BinaryCoversion(num)
