print("Welcome to Treasure Island\nYour mission is to find the treasure.")

direction = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\" ")

if direction.lower() == "left":
    wait_or_swim = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    
    if wait_or_swim.lower() == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

        if color.lower() == "blue":
            print("You enter a room of beasts. Game over.")
        elif color.lower() == "red":
            print("You enter a room of fire. Game over.")
        elif color.lower() == "yellow":
            print("You found the treasure. You win!")
        else:
            print("You died")
    
    elif wait_or_swim.lower() == "swim":
        print("You drown. Game over.")

    else:
        print("This kills you. Game over.")

elif direction.lower() == "right":    
    print("You fall into a sandpit. Game over.")

else:
    print("You can only go left or right! Try again")