import math
import matplotlib.pyplot as plt
import numpy as np

from Functions import *

fx = input("wat moet x(t) zijn? ")
fy = input("wat moet xy(t) zijn? ")


xCoords = []
yCoords = []

fxPrep = Prep(fx)
xCoords = CalcArray(fxPrep)

fyPrep = Prep(fy)
yCoords = CalcArray(fyPrep)

# print(xCoords)

# print(yCoords)

plt.plot(xCoords, yCoords)
plt.show()