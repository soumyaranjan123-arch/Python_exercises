def factorial():
    user_input = int(input('Enter the number, you want to found factorial of: '))
    result = fact_num(user_input)
    print(result)

def fact_num(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_num(n-1)
    
factorial()