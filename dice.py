import random

def main():
    while True:
        print('Dice rolled! and You got, ',roll_dice())
        
        roll_again = input('Do you want to roll again? (y/n): ').lower()

        if roll_again != 'y':
            print('Thanks for playing.')
            break
        
def roll_dice():
    return random.randint(1,6)

main()
