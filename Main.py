import math
import matplotlib.pyplot as plt
import numpy as np
import timeit
from PIL import Image

from Functions import *

ImgWidth, ImgHeight = 500, 500

fx = 't'
fy = '(t)^2'
# fx = input("wat moet x(t) zijn? ")
# fy = input("wat moet y(t) zijn? ")


tic=timeit.default_timer()

fxPrep = Prep(fx)
xCoords = CalcArray(fxPrep)
xCoordsScaled = Scaler(xCoords)

fyPrep = Prep(fy)
yCoords = CalcArray(fyPrep)
yCoordsScaled = Scaler(yCoords)

toc=timeit.default_timer()
print(str(round((toc-tic)*1000, 8))+ 'ms (Prep + CalcArray + Scaler)')


tic=timeit.default_timer()
Pixels = PixCalc(ImgHeight, ImgWidth, xCoordsScaled, yCoordsScaled)
toc=timeit.default_timer()
print(str(round((toc-tic)*1000, 8))+ 'ms (Calculating Pixels)')


array = np.array(Pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')
print(xCoordsScaled)

# plt.plot(xCoordsScaled, yCoordsScaled)
# plt.show()