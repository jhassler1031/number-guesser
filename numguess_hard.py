
import random

my_num = input("Please enter a number between 0 and 100 for the computer to guess: ")
my_num = int(my_num)

while my_num < 0 or my_num > 100:
    my_num = input("That number is not between 0 and 100, please try again: ")
    my_num = int(my_num)

#computer_number = random.randint(0 , 101)
high_end = 100
low_end = 0
computer_number = (low_end + high_end) / 2
counter = 1

while computer_number != my_num:
    if computer_number < my_num:
        low_end = computer_number
        computer_number = (low_end + high_end) / 2
        computer_number = int(computer_number)
        counter += 1
    else:
        high_end = computer_number
        computer_number = (low_end + high_end) / 2
        computer_number = int(computer_number)
        counter += 1

counter = str(counter)
print("The computer guessed your number in " + counter + " turns.")
