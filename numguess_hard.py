
import random

human_num = input("Please enter a number between 0 and 100 for the computer to guess: ")
human_num = int(human_num)

while my_num < 0 or my_num > 100:
    my_num = input("That number is not between 0 and 100, please try again: ")
    my_num = int(my_num)

computer_number = random.randint(0 , 101)
counter = 1

while computer_number != my_num:
    


counter = str(counter)
print("The computer guessed your number in " + counter + " turns.")
