import math
import matplotlib.pyplot as plt
import numpy as np

from Functions import *
test = []
deezer = []

fx = 't'
fy = '(t)^2'
# fx = input("wat moet x(t) zijn? ")
# fy = input("wat moet y(t) zijn? ")

import timeit
tic=timeit.default_timer()

fxPrep = Prep(fx)
xCoords = CalcArray(fxPrep)
xCoordsScaled = Scaler(xCoords)

fyPrep = Prep(fy)
yCoords = CalcArray(fyPrep)
yCoordsScaled = Scaler(yCoords)

toc=timeit.default_timer()
print(round((toc-tic)*1000, 5))


plt.plot(xCoordsScaled, yCoordsScaled)
plt.show()