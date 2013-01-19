# validate_mastervisa.py
# validate a user input MasterCard or VISA credit card number

import re

def validate(card_no):
    ''' Function to validate a MasterCard or VISA credit card number'''
    total = 0


    for a in range(0, 16, 2):
        # add value of digit multiplied by 2 to total if digit is less than 4
        if int(card_no[a]) <= 4:
            total = total + int(card_no[a]) * 2
            
        # minus 9 before adding value of digit multiplied by 2 to total
        else:
            total = total + int(card_no[a]) * 2 - 9

    # add the other digits
    for b in range(1, 16, 2):
        total = total + int(card_no[b])
    print(total)
    
    # modulo 10
    if total % 10 == 0:
        print("Credit card number is valid.")
    
    else:
        print("Credit card number is invalid.")

card_no = input("Enter your 16-digit credit card number: ")

# verify that card number is made up of 16 digits
pattern = re.compile("^[0-9]{16}$")
if not pattern.match(card_no):
    print("Credit card number has to be made up of 16 numbers.")

else:
    # visa
    if card_no[0] == '4':
        validate(card_no)

    # mastercard
    elif card_no[0] == '5' and 0 <= int(card_no[1]) <= 5:
        validate(card_no)
    
