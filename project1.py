name = input("Please type your name: ")
print("Hi " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("let's play!")
    weapon = input("Choose a weapon (harpoon/axe): ").lower()

    direction = input("Do you want to go left or right? (type: left/right)" ).lower()
    if direction == "left":
        print("You went left and fell off a cliff, game over, try again")
    
    elif direction == "right":
        print("right we go then")
        choice = input("Okay, now you see a river with a battered rope bridge going across, hanging by a thread. would you like to swim across the river or cross the bridge? (type: swim/cross) ").lower()
            
        if choice == "swim" and weapon== "harpoon":
            print("You were attacked by a fresh water shark but you used the harpoon to kill it and cross safely, you've won the game and receive eternal glory!")

        elif choice == "swim":
            print("You were eaten by a fresh water shark, you died and the game is over. Better luck next time")

        elif choice == "cross":
            print("the bridge fell right as you crossed! hope you didn't have any friends behind you... Anyways *awkward silence* you found the gold and won the game!")
            
        else:
            print ("not a valid response, you die!")

    else:
        print ("not a valid response, you die!")

else:
    print("go home then")
