price_of_house = 1000000
buyer_credit = True

if buyer_credit:
    down_payment = 0.1 * price_of_house
else:
    down_payment = 0.2 * price_of_house

print(f'Down Payment: ${down_payment}')
