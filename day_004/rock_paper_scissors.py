import random

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
)
computer_choice = random.randint(0, 2)


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

print(choices[user_choice])

print("Computer chose:")
print(choices[computer_choice])

if user_choice == 0:
    if computer_choice == 0:
        print("Tie game")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("You win")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("Tie game")
    else:
        print("You lose")
else:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    else:
        print("Tie game")
