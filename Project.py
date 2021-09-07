
#In this python project, you input a year and check whether it is a leap year or not. For this,
#you’ll have to create a function that recognizes the pattern of leap years and can try fitting the
#inputted year into the pattern. In the end, you can print the result using a boolean expression




#Number_guessing > Make a program in which the computer randomly chooses a number between 1 to 10,
#1 to 100, or any range. Then give users a hint to guess the number. Every time the user guesses
#wrong, he gets another clue, and his score gets reduced. The clue can be multiples, divisible,
#greater or smaller, or a combination of all
import random


def guess_random_number(x):
    computer_random_number = random.randint(1, x)
    guess = 0
    lives = 6  # (bug)>if I make the correct guess on my last life, I still lose
    while guess != computer_random_number and lives > 0:
        guess = int(input(f"Guess a number from 1 to {x}\n"))
        lives -= 1
        print("You have " + str(lives) + " live(s) left.")
        if lives == 0:
            print('You lost!')
            quit()
        elif guess < computer_random_number:
            print("That's too low, try again.")
        elif guess > computer_random_number:
            print("That's too high, try again.")
        else:
            print("You got it!!!")


guess_random_number(20)


#madlibs
"""adj = input("adjective\n")
verb1 = input("verb\n")
verb2 = input("verb\n")
famous_person = input("famous person\n")

madlib = f"computer programming is so {adj}! It makes me so excited all the time. I love to {verb1}. Stay hydrated and \
{verb2} like you are {famous_person}!"

print(madlib)"""



# Guess the number (Computer has a secret number, user has to guess it)
"""import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}\n'))
        if guess < random_number:
            print("Too low, guess again")
        elif guess > random_number:
            print("Too high, guess again")
    print(f"Yay, you have guessed the number {random_number}")

guess(100)"""


# Guess the number (Computer has to guess the secret number.)
"""import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)??\n').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("You got it, computer!")

computer_guess(100)"""

# Rock, Paper, Scissors
"""import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    #return true if player wins
    if (player == 'r' and oppenent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())"""









