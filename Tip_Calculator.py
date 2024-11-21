print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 15 20 "))
people = int(input("How many people to split the bill? "))


total = (tip / 100  * bill + bill) / people


print(f"Each person should pay: ${total}")
