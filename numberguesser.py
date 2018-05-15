import random

computer_number = random.randint(0 , 101)

my_num = input("Pick a number between 0 and 100: ")
my_num = int(my_num)

while my_num < 0 or my_num > 100:
    my_num = input("That number is not between 0 and 100, please try again: ")
    my_num = int(my_num)

counter = 1

while my_num != computer_number:
    if my_num - computer_number < 10 and computer_number - my_num < 10:
        print("Getting close! ")
    if my_num > computer_number:
        my_num = input("Too high.  Guess again: ")
        my_num = int(my_num)
        counter += 1
    else:
        my_num = input("Too low.  Guess again: ")
        my_num = int(my_num)
        counter += 1

counter = str(counter)
print("Congratulations, you guessed the number!")
print("It took you " + counter + " times to guess the number.")
