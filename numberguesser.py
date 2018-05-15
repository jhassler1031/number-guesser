import random

computer_number = random.randint(0 , 10)

my_num = input("Pick a number between 1 and 10: ")
my_num = int(my_num)

counter = 1

while my_num != computer_number:
    if my_num > computer_number:
        my_num = input("Too high, guess again: ")
        my_num = int(my_num)
    else:
        my_num = input("Too low, guess again: ")
        my_num = int(my_num)

print("Congratulations, you guessed the number!")
