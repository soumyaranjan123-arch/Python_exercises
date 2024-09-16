
def quiz_game():
    questions = {
        'What is the capital of France?':'Paris',
        'What is the smallest country in the world?':'Vatikan city',
        "Who wrote 'Harry Porter'?":'J.K. Rowling'
    }
    score = 0

    for ques, ans in questions.items():
        user_ans = input(ques+'').lower()

        if user_ans == ans.lower():
            print('Correct')
            score += 1
        else:
            print('Incorrect')

    print(f'Your score is {score} out of {len(questions)}')
        

quiz_game()