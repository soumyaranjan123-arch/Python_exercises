'''
celsius to farenheit
c = ((f-32)/9)*5
f = 9/5 * c + 32

celsius to kelvin
c = k - 273
k = c + 273

kelvin to farenheit
f = ((k - 273.15) * 1.8) + 32
k = ((f - 32) / 1.8) + 273.15
'''

def unit_converter():
    user_input = float(input('Enter your value: '))
    from_unit = input('Input your given unit(celsius/farenheit/kelvin): ')
    to_unit = input('Enter your desired unit for conversion(celsius<->farenheit, celsius<->kelvin, kelvin<->farenheit): ')

    if from_unit == 'celsius' and to_unit == 'farenheit':
        result = (9/5) * user_input + 32
        print(f'{user_input} degree celsius is {(result.__floor__())} degree farenheit.')

    elif from_unit == 'farenheit' and to_unit == 'celsius':
        result = ((user_input - 32)/9)*5
        print(f'{user_input} farenheit is {(result.__floor__())} degree celsius.')

    elif from_unit == 'celsius' and to_unit == 'kelvin':
        result = user_input + 273
        print(f'{user_input} degree celsius is {result} kelvin.')

    elif from_unit == 'kelvin' and to_unit == 'celsius':
        result = user_input - 273
        print(f'{user_input} kelvin is {result} celsius.')

    elif from_unit == 'kelvin' and to_unit == 'farenheit':
        result =  ((user_input - 273.15) * 1.8) + 32
        print(f'{user_input} kelvin is {result.__floor__()} farenheit.')

    elif from_unit == 'farenheit' and to_unit == 'kelvin':
        result = ((user_input-32) / (1.8)) + 273.15
        print(f'{user_input} farenheit is {result.__floor__()} kelvin.')

    else:
        print('Invalid Choice.')

unit_converter()