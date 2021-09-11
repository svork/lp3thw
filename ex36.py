# First encounter with Adaon(EK) and Wolf(enemy)
from sys import exit

# Starts the game
def start_game():
    print_game_name()
    print("""
        You just got a magical letter about a hidden treasure in the far,
        far away city of Pindamonhagaba. You are very content and decided
        to start your journey at Taquaral Lagoon. But first, you must
        cross the Osasco forest. Be careful.
    """)
    start_story()

# Print the name of the game, using ASCII art
def print_game_name():
    pass

# Player decide to run the game or exit
def start_story():
    answer = input("Would you want to enter the forest? Y/N\n>")

    if answer == "y" or answer == "Y":
        adaon()
    else:
        death("Choke")

# Meet Adaon
def adaon():
    print("""
        After a few steps into the Osasco forest, you noticed a person
        hiding something behind a huge tree and covering up with leaves
        and tree branches. He is a ridiculously good looking young man,
        wearing a totally not suspicious cloak. You say "Hello there".
    """)

    print("""
        After some chit-chat, Adaon wants to join you, searching for the
        hidden treasure. Would you welcome him to your party?
    """)

    answer = input("Y/N")

    if answer == "y" or answer == "Y":
        wolf()
    else:
        death("Stab")

# Enemy: Wolf
def wolf():
    print("Adaon joins your party. Yay!")
    print("""
        After walking countless miles inside the Osasco forest, Adaon
        tells you it is time to setup camp. You are about to unpack
        your items, when a dire, fearsome grey wolf shows up from nowhere.
        Would you attack the wolf or run for your life?
    """)

    answer = input("(A)ttack / (R)un)")

    if answer == "a" or answer == "A":
        end()
    else:
        death("Bite")

# Endgame
def end():
    print("""
        You unsheathe your trusty dagger and prepare to attack the wolf
        but you wake up from a dream and go back to your boring life.

        The end.
    """)

    exit(0)

# Death: When the player does something I don't want to, he dies :D
def death(reason):
    if reason == "Choke":
        print("You choked with a slice of a moldy bread and died :)")

    if reason == "Stab":
        print("When you turn around, Adaon quickly stabs you from behind.")

    if reason == "Bite":
        print("The wolf jumps towards you and the chews your face off.")

    exit(255)

# Start the game
start_game()
