import math
import matplotlib.pyplot as plt
import numpy as np
import timeit
from PIL import Image

from Functions import *

ImgWidth, ImgHeight = 1000, 1000 

fx, fy = 'sin(t*51)', 'sin(t*50)'
xPoints1, yPoints1, r1, g1, b1 = 0, 0, 255, 0, 0
xPoints2, yPoints2, r2, g2, b2 = 1, 1, 0, 255, 0
xPoints3, yPoints3, r3, g3, b3 = 10, 10, 0, 0, 255
Scale = 1

# fx = input("wat moet x(t) zijn? ")
# fy = input("wat moet y(t) zijn? ")


tic=timeit.default_timer()

fxPrep = Prep(fx)
xCoords = CalcArray(fxPrep)
xCoordsScaled = Scaler(xCoords, Scale)

fyPrep = Prep(fy)
yCoords = CalcArray(fyPrep)
yCoordsScaled = Scaler(yCoords, Scale)

toc=timeit.default_timer()
print(str(round((toc-tic)*1000, 8))+ 'ms (Prep + CalcArray + Scaler)')


tic=timeit.default_timer()
Pixels = PixCalc(ImgHeight, ImgWidth, xCoordsScaled, yCoordsScaled)
toc=timeit.default_timer()
print(str(round((toc-tic)*1000, 8))+ 'ms (Calculating Pixels)')

Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints1, yPoints1, Scale, r1, g1, b1)
Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints2, yPoints2, Scale, r2, g2, b2)
Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints3, yPoints3, Scale, r3, g3, b3)

array = np.array(Pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')

plt.plot(xCoordsScaled, yCoordsScaled)
# plt.show()