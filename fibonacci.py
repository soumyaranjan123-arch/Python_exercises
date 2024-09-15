def fibonacci():
    user_input = int(input('Enter no. of term upto which, you want to find fibonacci series: ')) 
    for i in range(user_input):
        print(fib(i))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
fibonacci()