import os
import time
import random

# Declare lists that will be generated by global scope in the next methods
generate_guess_list = []
generate_user_list = []
win = False

# class MemoryGame(Games)
def generate_sequence(difficulty):
    global generate_guess_list
    for item in range(difficulty):
        generate_guess_list.append(random.randint(1, 101))
    return generate_guess_list

def get_list_from_user(difficulty):
    global generate_user_list
    valid_range = range(1, 102)
    for count in range(difficulty):
        guess_num = input(f"Guess number: {count+1}, Please guess a number that prompted from 1-101: ")

        # User guess number validation
        while guess_num not in valid_range:
            try:
                guess_num = int(guess_num)
                if guess_num not in valid_range:
                    raise ValueError
            except ValueError:
                print("You didn't entered a number in the range!")
                guess_num = input(f"Guess number: {count+1}, Please guess a number that prompted from 1-101: ")

        generate_user_list.append(guess_num)
    return generate_user_list

def is_list_equal(random_list, user_list):
    random_list.sort()
    user_list.sort()
    if random_list == user_list:
        return True
    else:
        return False

def play(difficulty):
    global win
    random_list = generate_sequence(difficulty)
    print(random_list)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_list = get_list_from_user(difficulty)
    equal = (is_list_equal(random_list, user_list))
    if equal:
        print("True\nCongratulations! you won the memory game!")
        win = True
    else:
        print("False\nUnfortunately you lost the memory game, feel free to try another time :)")
    # print(f"Random List is: {random_list}")
    # print(f"User List is: {user_list}")
