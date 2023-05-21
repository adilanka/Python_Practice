credits_taken = int(input("Enter the number of credits taken:"))

if credits_taken<=23:
    print("Student is a Freshman.")
elif credits_taken>=24 and credits_taken<=53:
    print("Student is a Sophomore.")
elif credits_taken>=54 and credits_taken<=83:
    print("Student is a Junior.")
else:
    print("Student is a Senior.")
