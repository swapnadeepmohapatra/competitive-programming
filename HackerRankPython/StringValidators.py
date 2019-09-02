# You are given a string s.
# Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# In the first line, print True if it has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if it has any alphabetical characters. Otherwise, print False.
# In the third line, print True if it has any digits. Otherwise, print False.
# In the fourth line, print True if it has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if it has any uppercase characters. Otherwise, print False.


if __name__ == '__main__':
    s = input()

    alnum = False
    for x in s:
        if x.isalnum():
            alnum = True

    alb = False
    for x in s:
        if x.isalpha():
            alb = True

    dgt = False
    for x in s:
        if x.isdigit():
            dgt = True

    low = False
    for x in s:
        if x.islower():
            low = True

    up = False
    for x in s:
        if x.isupper():
            up = True

    print(alnum)
    print(alnum)
    print(dgt)
    print(low)
    print(up)
