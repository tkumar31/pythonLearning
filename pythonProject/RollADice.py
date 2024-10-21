# Aisk user roll a dice
# if user input 'y'
# print the random numbers
# if user input 'n'
## print 'Thanks for playing!'
# else
# print 'Invalid choice!'
import random

while True:
    choice = input('Roll a dice? (y/n) ').lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(dice1,dice2)
    elif choice == 'n':
        print('Thanks for playing')
        break
    else:
        print('Invalid choice!')

