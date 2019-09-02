# Given an integer,n , print the following values for each i integer 1  from n to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary


def print_formatted(number):
    for i in range(1, number+1):
        print("{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}".format(
            i, w=len(bin(number)[2:])))
# def print_formatted(number):
#     # your code goes here
#     for x in range(1, number+1):
#         print(x, end="  ")
#         print(oct(x)[2::], end="  ")
#         print(hex(x)[2::], end="  ")
#         print(bin(x)[2::], end="  ")
#         print(" ")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
