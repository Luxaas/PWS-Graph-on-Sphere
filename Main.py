import math
import matplotlib.pyplot as plt
import numpy as np


from Functions import *

# fx = input("wat moet x(t) zijn? ")
fx = "2sin(t - 0,5) + 1"
# fy = input("wat moet xy(t) zijn? ")
# tbegin = int(input("van waar moet t lopen? "))
# teind = int(input("tot waar moet t lopen"))
# xCoords = []
# yCoords = []

for p in range(len(fx)):
    if fx[p:(p+3)] == "sin" or fx[p:(p+3)] == "cos":
        print(p)

fx = fx.replace(",", ".")
fx = fx.replace("sin", "math.sin")



print(fx.replace("(t", "(6"))

print(fx.replace("t", "6"))
# for t in range(tbegin, teind):
    # xCoords.append(xt)