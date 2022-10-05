#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 3, 2022
# This program calculates and displays the subtotal with tax
# using the Alberta tax rate


import constants


def main():

    # Asks user for their subtotal
    subtotal = float(input("Enter your subtotal: $"))

    # Calculates tax and total
    tax = subtotal * constants.ALBERTA_GST
    total = subtotal + tax

    # Displays tax and total to user
    print("The tax (Alberta GST) you must pay: ${:.2f}".format(tax))
    print("Your total is ${:.2f}".format(total))


if __name__ == "__main__":
    main()
