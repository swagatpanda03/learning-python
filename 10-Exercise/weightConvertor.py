weight = float(input('Enter your weight'))
unit = input('(L) for pounds and (K) for kilo')

if unit == 'l' or unit == 'L':
    weight *= 0.45
    print(f'Weight: {weight} kilos')
elif unit == 'k' or unit == 'K':
    weight /= 0.45
    print(f'Weight: {weight} pounds')
