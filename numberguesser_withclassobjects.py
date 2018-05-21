
import random

#Create classes

class CompNumber:

    def __init__(self):
        self.number = random.randint(0, 101)

    def __repr__(self):
        return "self.number"

    def check_guess(self, guess):
        if self.number == guess:
            return True
        else:
            return False

    def is_close(self, guess):
        if self.number - guess.number <= 10 and guess.number - self.number <= 10:
            return True
        else:
            return False

    def high_low(self, guess):
        if guess.number > self.number:
            print("Too high.")
        else:
            print("Too low.")


class HumanNumber:

    def __init__(self):
        self.number = 0

    def __repr__(self):
        return "self.number"

    def check_number(self, number):
        if number >= 0 and number <= 100:
            return True
        else:
            return False

    def get_number(self):
        self.number = input("Pick a number between 0 and 100: ")
        self.number = int(self.number)
        if not self.check_number(self.number):
            print("That number was not within the specified range.")
            self.get_number()





#Start program

computer_number = CompNumber()
human_number = HumanNumber()
counter = 1

human_number.get_number()

while not computer_number.check_guess(human_number.number):
    computer_number.high_low(human_number)
    if computer_number.is_close(human_number):
        print("Getting close!")
    counter += 1
    human_number.get_number()

print("Congratulations, you guessed the number!")
print("It took you " + str(counter) + " times to guess the number.")
