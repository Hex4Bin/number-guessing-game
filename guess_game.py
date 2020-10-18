"""
This is a number guessing game!
"""
import random

if __name__ == '__main__':

    rand = random.randint(1, 100)
    guesses = [0]

    while True:
        guess = int(
            input("I'm guessing a number between 1-100!\nWhat is your guess?: "))

        if guess < 1 or guess > 100:
            print('OUT OF BOUNDS! Please try again: ')
            continue

        if guess == rand:
            print(
                f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
            break

        guesses.append(guess)

        if guesses[-2]:
            if abs(rand - guess) < abs(rand - guesses[-2]):
                print('WARMER!')
            else:
                print('COLDER!')

        else:
            if abs(rand - guess) <= 10:
                print('WARM!')
            else:
                print('COLD!')
