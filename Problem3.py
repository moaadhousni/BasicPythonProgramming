#Problem 3

import stdio
import sys
import numpy

t = float(input("enter a number"))
v = float(input("enter a number"))

if numpy.absolute(t)>50 or v > 120 or v < 3:
    print("invalid")
else: 
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)
    print(w)

stdio.writeln('Temperature = ' + str(t))
stdio.writeln('Wind speed  = ' + str(v))
stdio.writeln('Wind chill  = ' + str(w))

