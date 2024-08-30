print("Welcome to the Tip Collector!")
bill = float(input("What was the total bill?"))
n = int(input("How many people to split the bill?"))
tip = int(input("What percentage tip would you like to give?10,12 or 15?"))
payment_each = (bill +(tip*bill)/100)/n
print("Each person should pay: $"+ str(payment_each))

