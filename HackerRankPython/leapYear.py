# You are given the year, and you have to write a function to check if the year is leap or not.

# Note that you have to complete the function and remaining code is given as template.


def is_leap(year):
    leap = False
    if(year % 400 == 0):
        leap = True
    elif(year % 4 == 0 and year % 100 != 0):
        leap = True
    return leap


year = int(input())
print(is_leap(year))
