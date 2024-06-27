# Read the secret password from the file
with open('/src/SecretPasswordFile.txt', 'r') as passwordFile:
    secretPassword = passwordFile.read()

# Prompt the user to enter their password
typedPassword = input('Enter your password: ')

# Check if the typed password matches the secret password
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print("That password is one that an idiot puts on their luggage.")
else:
    print('Access denied')
