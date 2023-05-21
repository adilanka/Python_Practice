x = int(input("Enter the budget for the laptop: "))
screen_area = int(input("Enter the screen area user wants: "))

lap1 = {
  "Cost": 75000,
  "Sc_area": 15.6
}
lap2 = {
  "Cost": 48000,
  "Sc_area": 11.4
}
lap3 = {
  "Cost": 100000,
  "Sc_area": 15.6
}
lap4 = {
  "Cost": 125000,
  "Sc_area": 17.0
}
lap5 = {
  "Cost": 85000,
  "Sc_area": 16.0
}
count = 0
a = [lap1,lap2,lap3,lap4,lap5]

for i in a:
    if i.get("Cost") > x:
        continue
    else:
        if i.get("Sc_area") >= screen_area:
            print(i)
            count=count+1
if count<1:
    print("No Laptop")