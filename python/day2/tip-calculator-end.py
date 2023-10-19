# 1. Create a greeting for the program
print("Welcome to the tip calculator! ")

# 2. Ask the user for the total bill
total_bill = float(input("What was the total bill? $"))

# 3. Ask the user for the number of people to split the bill
split_bill = int(input("How many people to split the bill? "))

# 4. Ask the user for the percentage of tip to give
percentage_tip = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))

# 5. Calculate the total amount each person should pay
amount_per_person = total_bill * (1 + percentage_tip / 100) / split_bill
final_amount = "{:.2f}".format(amount_per_person)
print(type(final_amount))

print(f"Each person should pay: ${final_amount}")
