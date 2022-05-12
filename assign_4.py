#!/usr/bin/env python3

# Created by: Adam Winogron
# Created on: May 4, 2022
# This program asks the user for 2 random intergers
# and finds the lowest common multiple of those two intergers
# using loops.

# include math
import math


# main function
def main():

    # Describe program function
    print("If you give me 2 numbers I'll find \
their lowest common multiple!")
    print()

    # declare variables
    num_1_string = ""
    num_2_string = ""

    # catch statement
    try:
        # get user input
        num_1_string = input("What's the first number you'd like \
me to use?: ")
        # check for int
        num_1 = int(num_1_string)
        # variable for use in while loop
        temp_num_1 = num_1
        print()

    except Exception:
        # tell the user they need an interger
        print()
        print("Sorry, I'm going to need a whole positive interger \
for your first number!")

        # conclusion scentance
        print()
        print("try again by restarting the program!")

    else:
        try:
            # get the second number from the user
            num_2_string = input("Now I'll need the second number!: ")
            # check for int
            num_2 = int(num_2_string)
            # for use in while loop
            temp_num_2 = num_2

            # declare loop variables
            multi_1 = 1
            multi_2 = 1
            holder_1 = num_1
            holder_2 = num_2

            # rearrange variables to work with loop
            if (num_1 > num_2):
                holder_1 = num_2
                holder_2 = num_1

            # check for same number
            if (num_1 == num_2):
                print()
                print("The lowest common multiple of two of the same number \
is just that number! So in this case it's {}".format(num_1))
            else:
                # while loop for calculating lcm of 2 user_nums
                while (holder_1 < holder_2):
                    # increase counter
                    multi_1 = multi_1 + 1
                    # increase num
                    num_1 = num_1 * multi_1
                    # assign holder
                    holder_1 = num_1
                    # check for lcm
                    if (holder_1 == holder_2):
                        print()
                        # tell user lcm
                        print("The lowest common multiple of your two \
numbers is {}".format(holder_1))
                        break
                    # check for larger number
                    while (holder_1 > holder_2):
                        # increase counter
                        multi_2 = multi_2 + 1
                        # multiply
                        num_2 = num_2 * multi_2
                        # assign holder
                        holder_2 = num_2
                        # check for lcm
                        if (holder_1 == holder_2):
                            print()
                            # tell user lcm
                            print("The lowest common multiple of your two \
numbers is {}".format(holder_1))
                            break
                        else:
                            # reset nums
                            num_1 = temp_num_1
                            num_2 = temp_num_2
                    else:
                        # reset nums
                        num_1 = temp_num_1
                        num_2 = temp_num_2

        except Exception:
            # tell the user their input wasn't an interger
            print()
            print("Sorry, I'm going to need a whole positive interger \
for your second number!")

        # display final message
        finally:
            print()
            print("Feel free to try again by restarting the program!")


# call main
if __name__ == "__main__":
    main()
