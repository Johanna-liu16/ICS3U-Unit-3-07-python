#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program adds two numbers

import random


def main():
    # this is a number guessing game

    # input
    print("This program checks if you're suitable or not for dating.")
    str_user_age = input("Enter your age: ")

    # process
    try:
        user_age = int(str_user_age)
        if user_age >= 25 and user_age <= 40:
            print("Congratulations! You're an acceptable age.")
        elif user_age < 0:
            print("Invalid integer")
        else:
            print("Sorry, you're not an acceptable age.")
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thanks for playing")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
