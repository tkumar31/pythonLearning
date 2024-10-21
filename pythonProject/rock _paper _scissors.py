import random

choices = ('r','p','s')
emojies = {'r': '🪨', 'p': '📄', 's': '✂️'}

while True:
    user_choice = input('Rock, paper, scissors? (r,p,s): ').lower()

    if user_choice not in choices:
        print('Invalid choice!')
        continue
    computer_choice = random.choice(choices)

    print(f'User choice: {emojies[user_choice]}')
    print(f'Computer choice: {emojies[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r') ):
        print('You win!')
    else:
     print('You loose!')

    should_continue = input('Should continue? ').lower()
    if should_continue == 'n':
        break
