from art import logo, vs
from game_data import data
from random import choice
from os import system

def return_compare(compare_dict):
    return f"{compare_dict['name']}, a {compare_dict['description']} from {compare_dict['country']}"

system("clear")
print(logo)

def play_round(score, compare_a):
    compare_b = choice(data)
    while compare_a == compare_b:
        compare_b = choice(data)

    if compare_a["follower_count"] > compare_b["follower_count"]:
        winner = "a"
        winner_data = compare_a
    else:
        winner = "b"
        winner_data = compare_b

    print(f"Compare A: {return_compare(compare_a)}")
    print(vs)
    print(f"Against B: {return_compare(compare_b)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == winner:
        score += 1
        system("clear")
        print(logo)
        print(f"You're right! Current score: {score}")
        play_round(score, winner_data)
    else:
        system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

play_round(0, choice(data))