# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6 to 20 , print Weird
# If  is even and greater than 20, print Not Weird

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0:
        if n <= 5 and n >= 2:
            print('Not Weird')
        elif n <= 20 and n >= 6:
            print('Weird')
        elif n > 20:
            print('Weird')
