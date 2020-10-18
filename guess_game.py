"""
This is a number guessing game!
"""

import random


class GuessGame:

    def __init__(self, minNum, maxNum):
        self.number = 0
        self.minimum = minNum
        self.maximum = maxNum
        self.guesses = [0]

    def rand(self):
        """ Randomize a number between minimum and maximum. """
        self.number = random.randint(self.minimum, self.maximum)

    def get_guess(self):
        """ Ask the user to guess a number between minimum and maximum. """
        guess = input(
            f"Please, guess a number between ({self.minimum} - {self.maximum}): ")

        if self.valid_number(guess):
            return(int(guess))
        else:
            print("Please enter a valid number.")
            return self.get_guess()

    def valid_number(self, str_num):
        """ Check if the given number is valid or not. """
        try:
            num = int(str_num)
        except:
            return False

        return self.minimum <= num <= self.maximum

    def play(self):
        """ Game logic """
        game.rand()
        while True:
            guess = self.get_guess()
            self.guesses.append(guess)

            if self.number == guess:
                print(
                    f"Congratulation! You guessed it in {len(self.guesses)-1} guesses.")
                break

            elif self.guesses[-2]:
                if abs(self.number - guess) < abs(self.number - self.guesses[-2]):
                    print("WARMER")
                else:
                    print("COLDER!")

            else:
                if abs(self.number - guess) <= 10:
                    print("WARM!")
                else:
                    print("COLD!")


if __name__ == '__main__':

    game = GuessGame(1, 100)
    game.play()
