def unit_converter():
    user_input = int(input('Enter your value: '))
    from_unit = input('Enter the unit you have given(kg/km/pound/miles): ')
    to_unit = input('Enter the unit you want to convert(kg<->pound,km<->miles): ')

    if from_unit == 'km' and to_unit == 'miles':
        result = user_input * 0.62137119
        print(f'{user_input} km is {result.__floor__()} miles.')

    elif from_unit == 'miles' and to_unit == 'km':
        result = user_input / 0.62137119
        print(f'{user_input} miles is {result.__floor__()} km.')

    elif from_unit == 'pound' and to_unit == 'kg':
        result = user_input * 0.45359237
        print(f'{user_input} pound is {result.__floor__()} kg.')

    elif from_unit == 'kg' and to_unit == 'pound':
        result = user_input / 0.45359237
        print(f'{user_input} kg is {result.__floor__()} pound.')
    else:
        print('Invalid Choice.')

unit_converter()

