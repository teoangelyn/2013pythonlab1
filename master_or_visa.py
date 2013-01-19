# master_or_visa.py

import re

def master_or_visa(card_no):
    ''' Function to determine if a user input credit card number belongs to MasterCard or Visa'''

    # reverse card number
    card_no == card_no[::-1]
    
   
    if card_no[0] == '4':
        print("Visa")

    elif card_no[0] == '5' and 0 <= int(card_no[1]) <= 5:
        print("Mastercard")

    else:
        print("Credit card number is neither Visa not Mastercard.")



# main

# get card number
card_no = input("Enter your 16-digit credit card number: ")

# verify that card number is made up of 16 digits
pattern = re.compile("^[0-9]{16}$")
if not pattern.match(card_no):
    print("Credit card number has to be made up of 16 numbers.")

else:
    master_or_visa(card_no)
