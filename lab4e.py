#!/usr/bin/env python3
# Author ID: jli699 - 175495233

def is_digits(sobj):
    string = 0;
    for x in sobj:
        # Checks through entire list to see if there is any non digit
        if x not in '0123456789':
            # Increment string variable by the amount of non digits
            string += 1;
    # Returns False if there is 1 or more non digits        
    if string > 0:
        return False;
    else:
        return True;
        

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
