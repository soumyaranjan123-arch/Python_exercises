
def main():
    user_input = int(input('Enter a number: '))

    is_prime = check_prime(user_input)
    if is_prime == True:
        print('It is a Prime number.')
    else:
        print('It is not a prime number.')

def check_prime(num):
    if num < 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

main()