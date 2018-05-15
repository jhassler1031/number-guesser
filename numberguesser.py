import random

computer_number = random.randint(0 , 10)

my_num = input("Pick a number between 1 and 10: ")
my_num = int(my_num)

counter = 1

while my_num != computer_number:
    if my_num > computer_number:
        my_num = input("Too high, guess again: ")
        my_num = int(my_num)
        counter += 1
    else:
        my_num = input("Too low, guess again: ")
        my_num = int(my_num)
        counter += 1

counter = str(counter)
print("Congratulations, you guessed the number!")
print("It took you " + counter + " times to guess the number.")
