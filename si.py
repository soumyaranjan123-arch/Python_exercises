
def main():
    principal = int(input('Enter your capital price: '))
    time = float(input('Enter your time (in year): '))
    rate_of_interest = float(input('Enter your rate of interest (per annum): '))

    simple_interest = simple_interest_calc(principal, time, rate_of_interest)

    print(f'The resulted SI for your plan is {simple_interest} rupees.')

def simple_interest_calc(principal, time, roi):
    return (principal * time * roi) / 100

main()