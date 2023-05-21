n = int(input("Enter the number of participants: "))
x = input("Enter the participants score with a space: ")
a = x.split()
runner_up = '0'
winner = max(a)

for i in a:
    if i == winner:
        pass
    elif i>runner_up:
        runner_up = i
print("The runner up score is: ",runner_up)