print('Welcome to Calculator built in Python.')

first_num = int(input('Enter your First_Number: '))
second_num = int(input('Enter your Second_Number: '))

operator = input('Input a mathematical operator to perform certain operation: ')

if operator == '+':
    print('You want to Summation,that\'s Intresting.')
    result = first_num + second_num
elif operator == '-':
    print('You want to Substract,that\'s Intresting.')
    result = first_num - second_num
elif operator == '*':
    print('You want to Multiply,that\'s Intresting.')
    result = first_num * second_num
elif operator == '%':
    print('You want to to do Modular Division,that\'s Intresting.')
    result = first_num % second_num
elif operator == '/':
    print('You want to Divide,that\'s Intresting.')
    result = first_num / second_num
elif operator == '**':
    print('You want to Raise to the Power,that\'s Intresting.')
    result = first_num ** second_num
else:
    print('Invalid Inputs')

print(f'Your Answer is: {result}')