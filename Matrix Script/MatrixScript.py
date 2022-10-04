#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
a = list(zip(*matrix))
string = ""
for i in range(len(a)):
    string += "".join(a[i])
pattern = re.compile(r"(?<=\w)[!@#$%& ]{1,}(?=\s*\w)")
new_string = re.sub(pattern," ",string)
print(new_string)
