#!/usr/bin/python3

import math
import random


def weird(n):
    if n < 1:
        pass
    elif n % 2 != 0:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    elif n > 100:
        pass
    else:
        print("Not Weird")


n = int(input())
weird(n)
