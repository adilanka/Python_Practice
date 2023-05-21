hours = int(input("Enter the number of hours browsed: "))
mins = int(input("Enter the number of minutes browsed: "))

if hours>9:
    print("Invalid input.")

elif hours>=5 and hours<=9:
    billing_amt = 300+(hours-5)*50+mins

elif hours<5:
    billing_amt = hours*50+mins

print("The Billing amount for Internet Browsing is: ",billing_amt)