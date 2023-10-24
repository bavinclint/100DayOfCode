import random
# Who's Paying
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(",")
item_number = len(names)

random_number = random.randint(0, item_number - 1)

choosen = names[random_number]


print(f"{choosen} is going to buy the meal today!")
