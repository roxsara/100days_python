#100 days of code - python bootcamp udemy
#Project 2

#Calculate the amount of money to be paid by each person after receiving a bill and entering a custom tip amount

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
participants = int(input("How many people to split the bill? "))

amount = (bill + bill*(tip/100))/participants
result = round(amount, 2)

print("Each person should pay: ", result)