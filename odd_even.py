
def main():
    user_input = int(input('Enter a number: '))
    
    result = odd_even(user_input)

    if result == True:
        print('This number is Even.')
    else:
        print('This number is Odd.')


def odd_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

main()