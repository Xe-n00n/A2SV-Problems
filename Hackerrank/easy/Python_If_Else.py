#!/bin/python3

import math
import os
import random
import re
import sys



def is_weird(num):
    if num%2==1:
        print('Weird') 
    elif num>=1 and num<=3:
        print('Not Weird')
    elif num>=6 and num<=20:
        print('Weird')
    else:
        print('Not Weird')
if __name__ == '__main__':
    n = int(input().strip())
    is_weird(n)