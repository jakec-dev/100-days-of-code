from art import logo
import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    return [random.choice(cards), random.choice(cards)]

def hit(cards_array):
    cards_array.append(random.choice(cards))
    tally = sum(cards_array)
    if tally > 21 and 11 in cards_array:
        index = cards_array.index(11)
        cards_array[index] = 1
    return cards_array

def house_plays(house_cards):
    tally = sum(house_cards)
    while tally < 17:
        house_cards = hit(house_cards)
        tally = sum(house_cards)
    return house_cards

keep_playing = True
while keep_playing:
    system("clear")
    print(logo)
    players_cards = deal_cards()
    house_cards = deal_cards()
    hit_or_sit = ""
    player_tally = sum(players_cards)
    
    print(f"Your cards: {players_cards} (total: {player_tally})")
    print(f"House shows a {house_cards[0]}")

    if player_tally == 21:
        print("Blackjack!! You win!")
        hit_or_sit = "s"

    while player_tally < 21 and hit_or_sit != "s":
        hit_or_sit = input("Type 'h' to hit or 's' to sit: ").lower()
        if hit_or_sit == "h":
            players_cards = hit(players_cards)
            player_tally = sum(players_cards)
            print(f"Your cards: {players_cards} (total: {player_tally})")

    if player_tally == 21:
        pass
    elif player_tally > 21:
        print("Bust! You lose.")
    else:
        house_cards = house_plays(house_cards)
        house_tally = sum(house_cards)
        print(f"Your final hand: {players_cards} (total: {player_tally})")
        print(f"House shows {house_cards} (total: {house_tally})")
        if house_tally > 21:
            print("House busts. You win!")
        elif player_tally > house_tally:
            print("You win!")
        elif player_tally == house_tally:
            print("It's a draw!")
        else:
            print("You lose!")

    play_again = input("Play again? [y/N] ")
    if play_again != "y":
        keep_playing = False