birth_days = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birth_days:
        print(f'{birth_days[name]} is the birthday of {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print('What is their birthday?')
        b_day = input()
        birth_days[name] = b_day
        print('Birthday database updated.')
