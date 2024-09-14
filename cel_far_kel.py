'''
celsius to farenheit
c = ((f-32)/9)*5
f = 9/5 * c + 32

celsius to kelvin
c = k - 273
k = c + 273
'''

def unit_converter():
    celsius = float(input('Enter your value in Celsius: '))
    desired_unit = input('Enter your desired unit for conversion(farenheit/kelvin): ')

    if desired_unit == 'farenheit':
        result = (9/5) * celsius + 32
        print(f'{celsius} degree celsius is {(result.__floor__())} degree farenheit.')
    elif desired_unit == 'kelvin':
        result = celsius + 273
        print(f'{celsius} degree celsius is {result} kelvin.')

unit_converter()