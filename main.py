import time
import random
from actors import Hero, Opponent


def main():
    print_welcome()
    play_game()

def print_welcome():
    print("""
----------------------------------------------------------
----------- Welcome to the Legend of Link RPG! -----------
----------------------------------------------------------

A dark shadow was cast over the lands of Heirulez. You are
the chosen one who shall venture through the forests of
the web to defeat what lurks a few links off Google's main
results. The wwworld needs you to restore peaceful linking
to the internet...

""")

def play_game():

    opponents = [
        Opponent('.docx', 1),
        Opponent('FTP-Server', 5),
        Opponent('www.xxx.com', 10),
        Opponent('.php', 15),
        Opponent('Pop-up Ad', 20),
        Opponent('Paywall', 30),
        Opponent('Wordpress-Site', 50),
        Opponent('Google Data Center', 500),
    ]

    hero = Hero('Link', 42)

    while True:
        # select a random opponent
        current_opponent = random.choice(opponents)
        print(f"101010111beeeep... A wild {current_opponent.name} \
at Level {current_opponent.level} has appeared.\n")

        cmd = input("Do you want to [a]ttack, [r]unaway, or [l]ook around? ")
        # check up for input validity
        while cmd not in ['a', 'r', 'l', 'q']:
            print("Please enter one of the three letters [a, r, l] to play")
            print("To exit game, type [q] for 'quit'.")
            cmd = input("Do you want to [a]ttack, [r]unaway, or [l]ook around? ")

        # do specific things depending on the user input

        # ATTACK LOGIC
        if cmd == 'a':
            if hero.attack(current_opponent):
                opponents.remove(current_opponent)
            else:
                print(f"{hero.name} caps their internet connection in despair...")
                time.sleep(5)  # pause for 5 seconds
                print(f"{hero.name} comes back online refreshed!\n")

        # RUNAWAY LOGIC
        elif cmd == 'r':
            print("You got away safely...\n")

        # LOOKAROUND LOGIC
        elif cmd == 'l':
            print(f"Hacking and checking out the surroundings... |Oh!| {hero.name} sees:")
            for op in opponents:
                print(f"* A {op.name} of Level {op.level}")
                # print(f"a {op}")  # using the __repr__ function
            print()

        # QUITTERS QUIT HERE
        elif cmd == 'q':
            print("\nExiting LINK RPG. ByeBye...")
            break


if __name__ == '__main__':
    main()
