
def main():
    text = input('Enter a word: ')
    palindrome_checker(text)

def palindrome_checker(myStr):
    reversed_str = myStr[::-1]
    print(reversed_str)

    if myStr == reversed_str:
        print('It is a palindrome.')
    else:
        print('Not a Palindrome.')

main()