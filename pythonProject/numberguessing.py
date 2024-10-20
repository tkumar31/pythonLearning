import random

number_to_guess = random.randint(1,100)
while True:
  try:
    number = int(input('Guess the number between 1 and 100: '))
    if number > number_to_guess:
        print('Too high!')
    elif number < number_to_guess:
        print('Too low!')
    else:
        print('Congratulations! You guessed the number.')
        break
  except ValueError:
      print('Please enter a valid number!')