import random

def russian_roulette():
    # Create a list to represent the chambers in the gun
    chambers = [0, 0, 0, 0, 0, 1]  # 1 represents a loaded chamber

    # Shuffle the chambers randomly
    random.shuffle(chambers)

    # Prompt the player to pull the trigger
    input("Press Enter to pull the trigger...")

    # Select a random chamber
    selected_chamber = random.choice(chambers)

    # Check if the selected chamber is loaded
    if selected_chamber == 1:
        print("Bang! You're dead!")
    else:
        print("Click! You survived!")

# Call the function to play the game
russian_roulette()