
def main():
    text = input('Enter a word: ')
    reversed_text = palindrome_checker(text)

    if text == reversed_text:
        print('It is a palindrome.')
    else:
        print('Not a Palindrome.')

def palindrome_checker(myStr):
    reversed_str = myStr[::-1]
    return reversed_str


main()