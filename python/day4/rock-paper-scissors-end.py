import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("Welcome to rock-paper-scissors game!")
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
options = [rock, paper, scissors]

computer_choice = random.randint(0, len(options) - 1)

if user_choice == 0 and computer_choice == 2:
    print(f"{rock}\nComputer chose:\n{scissors}\nYou win!")
elif user_choice == 2 and computer_choice == 1:
    print(f"{scissors}\nComputer chose:\n{paper}\nYou win!")
elif user_choice == 1 and computer_choice == 0:
    print(f"{paper}\nComputer chose:\n{rock}\nYou win!")
elif user_choice == computer_choice:
    print(
        f"{options[user_choice]}Computer chose:\n{options[computer_choice]}\nIt's a draw")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(
        f"{options[user_choice]}Computer chose:\n{options[computer_choice]}\nIt's a lose")
