
def main():
    myheight = int(input('Enter your height: '))
    myweight = int(input('Enter your weight: '))

    bmi = bmi_calc(myheight,myweight)
    # print(bmi)

    if bmi < 16:
        print('You are Severe Thinness.')
    elif 16 <= bmi < 17:
        print('You are Moderate hinness.')
    elif 17 <= bmi < 18.5:
        print('You are Mild Thinness.')
    elif 18.5 <= bmi < 25:
        print('You are Normal.')
    elif 25 <= bmi < 30:
        print('You are Overweight.')
    elif 30 <= bmi < 35:
        print('You are Obese Class I.')
    elif 35 <= bmi < 40:
        print('You are Obese Class II.')
    elif bmi >= 40:
        print('You are Obese Class III.')

def bmi_calc(height, weight):
    result = (weight/(height ** 2)) * 10000
    return round(result, 2)

main()