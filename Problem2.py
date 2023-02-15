#Problem 2

import stdio
import sys
import math

t =   int(input("number of years?"))
P =   int(input("principal?"))
r =   int(input("annual interest rate?"))
money = P*(math.exp(r*t))
print("Amount of money you would have if you invested it at a given interest rate:", money)
