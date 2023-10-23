# Love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

occurrence1 = (lower_name1 + lower_name2).count('t') + \
    (lower_name1 + lower_name2).count('r') + (lower_name1 +
                                              lower_name2).count('u') + (lower_name1 + lower_name2).count('e')
occurrence2 = (lower_name1 + lower_name2).count('l') + \
    (lower_name1 + lower_name2).count('o') + (lower_name1 +
                                              lower_name2).count('v') + (lower_name1 + lower_name2).count('e')

occurrence_convert = str(occurrence1) + str(occurrence2)
occurrence = int(occurrence_convert)

if (occurrence < 10) or (occurrence > 90):
    print(f"Your score is {occurrence}, you go together like coke and mentos.")
elif (occurrence >= 40) and (occurrence <= 50):
    print(f"Your score is {occurrence}, you are alright together.")
else:
    print(f"Your score is {occurrence}.")
