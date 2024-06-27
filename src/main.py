
"""
This document determines the Pythagorean Distance
between three given points
"""


def pythagorean_distance(x, y, z) -> float:
    # Returns the Pythagorean distance between the three given points
    # Pythagorean Theorem in 3 dimensions
    w_squared = x ** 2 + y**2 + z**2
    # The square root gives the distance
    w = w_squared ** 0.5
    # return the distance
    return w


dimensions = pythagorean_distance(2, 3, 4)
print(f'The distance is ({dimensions:.3f})\n')


# choose a question to ask
print('How would you rate your day on a scale of 1 to 10?')
# ask the user for their answer
day_rating = input()
# select an appropriate output
print(f'You feel lik a {day_rating} today. Thank for letting me know\n')

# find the least common multiple of two divisors
counting = True
divisor1 = 24
divisor2 = 36
i = 1
while counting:
    if i % divisor1 == 0 and i % divisor2 == 0:
        print(f'The least common multiple of {divisor1} and {divisor2} is {i}')
        break
    i += 1

print('What is your name?')
name = input()
print(f'Fascinating {name} is my name too.\n')
print('Have you thought about holes today?')
yes_no = input()
print(f'I am so glad you said, {yes_no} I am was thinking the same thing.')

print(f'We\'re kindred spirits, {name}. Talk later.')
