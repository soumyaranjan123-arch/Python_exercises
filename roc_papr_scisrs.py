import random

def rock_paper_scissors():

    comp = ['rock','paper','scissors']

    print('Welcome to Rock, Paper and Scissors game .')

    i = 0
    score = 0
    tie = 0
    system_score = 0

    while i < 5:
        system_choice = random.choice(comp)
        user_choice = input('Enter your choice(rock/paper/scissors): ')
        print(f'System choose {system_choice}')

        if system_choice == user_choice:
            print('Draw')
            tie += 1
        elif system_choice == 'rock' and user_choice == 'paper':
            print('You win')
            score += 1
        elif system_choice == 'paper' and user_choice == 'scissors':
            print('You win')
            score += 1
        elif system_choice == 'scissors' and user_choice == 'rock':
            print('You win')
            score += 1
        else:
            print('You lose')
            system_score += 1
        i += 1

    print(f'Your score is {score} out of 5 with system\'s score {system_score} with {tie} ties.')

rock_paper_scissors()