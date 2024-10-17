#Practice Tasks
# Countdown: Create a program that counts down from 10 to 1 and then prints "Lift off!".
# Even Numbers: Write a loop that prints all even numbers between 1 and 20.
# Guessing Game: Create a simple guessing game where the user has to guess a predefined number. The program should keep asking for guesses until the correct number is guessed.
#count down

# i = 10
#
# while i >= 1:
#     print(i)
#     i-=1
# print("Lift off!")


#Even Numbers: Write a loop that prints all even numbers between 1 and 20.

# i=2
#
# while i <= 20:
#     print(i)
#     i+=2

 #Guessing Game: Create a simple guessing game where the user has to guess a predefined number. The program should keep asking for guesses until the correct number is guessed.

target_number = 7
guess = None

while guess != target_number:
    guess = int(input("Guess the number between 1 to 10: "))
    if guess < target_number:
        print("Too low! try again. ")
    elif guess > target_number:
        print("Too high! try again. ")
    else:
        print("Congratulation! you win. ")


