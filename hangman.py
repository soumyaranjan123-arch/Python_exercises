import random

def hangman():
    words = ['hello','honest','horse','humble']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    while attempts > 0:
        guess = input('Guess the letter: ')
        if guess in guessed_letters:
            print('You already guessed that letter.')

        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print(''.join(guessed_word))

        else:
            attempts -= 1
            print(f'Wrong! you have {attempts} left.')
            
        guessed_letters.append(guess)

        if '_' not in guessed_word:
            print('You win!')
            break
    else:
        print(f'You lost! The word is {word}')

hangman()
            

