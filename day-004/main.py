import random

rock = '''
    _______
---\'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---\'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---\'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["rock", "paper", "scissors"]
ascii_list = [rock, paper, scissors]

# Players choice is vertical axis
#          | rock | paper | scissors |
# rock     | tie  | lose  | win      |
# paper    | win  | tie   | lose     |
# scissors | lose | win   | tie      |

rock_choice = ["tie", "lose", "win"]
paper_choice = ["win", "tie", "lose"]
scissors_choice = ["lose", "win", "tie"]
matrix = [rock_choice, paper_choice, scissors_choice]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

outcome = matrix[player_choice][computer_choice]

print(f"You chose {options[player_choice]}")
print(ascii_list[player_choice])
print(f"Computer chose {options[computer_choice]}")
print(ascii_list[computer_choice])
print(f"You {outcome}")