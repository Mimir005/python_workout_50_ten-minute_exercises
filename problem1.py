import random

def guessing_game():
    the_right_number = random.randint(0, 100)
    while True:
        the_user_guess = input('Enter your guess (0-100): ')
        if the_right_number>int(the_user_guess):
            print('Too low!')
        elif the_right_number<int(the_user_guess):
            print('Too high!')
        else:
            print('Congratulations! You guessed the right number! The right number is: ', the_right_number)
            break

if __name__ == "__main__":
    guessing_game()

