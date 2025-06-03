#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    return string[:5];

def last_seven(string):
    # Find length of string then subtract by 7 to find where to splice string
    length_of_string = len(string) - 7;
    return string[length_of_string:];

def middle_number(string):
    string = str(string);
    mid_num = string[1] + string[2];
    return mid_num;

def first_three_last_three(string1, string2):
    return string1[:3] + string2[-3:]; 


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
