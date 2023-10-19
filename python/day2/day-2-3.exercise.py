# Program that calculates the number of days, weeks and months given 90 years as constant

age = input("What is your current age? ")

convert_age = int(age)

days_left = (90 * 365) - (convert_age * 365)

weeks_left = (90 * 52) - (convert_age * 52)

months_left = (90 * 12) - (convert_age * 12)

print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
