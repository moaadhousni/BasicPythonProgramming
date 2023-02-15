#Problem 1

import stdio
import sys

m =   int(input("enter a number"))
d =   int(input("enter a number"))

isSpring = (m == 3 and d >= 20 and d <= 31) or \
           (m == 4 and d >=  1 and d <= 30) or \
           (m == 5 and d >=  1 and d <= 31) or \
           (m == 6 and d >=  1 and d <= 20)

stdio.writeln(isSpring)
