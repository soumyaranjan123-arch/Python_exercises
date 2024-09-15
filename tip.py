def main():
    bill = int(input('Enter your bill in rupees: '))
    tip_per = float(input('Enter the percentage of bill, you want to give as a tip: '))
    
    print(f'You should give {tip_calc(bill,tip_per)} rupees as a tip.')

def tip_calc(bill, tip_per):
    return bill * (tip_per / 100) 

main()