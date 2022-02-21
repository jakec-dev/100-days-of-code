total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

total_with_tip = total_bill * (1 + (percentage / 100))
split_amount = round(total_with_tip / num_of_people, 2)

print(f"Each person should pay: ${split_amount}")