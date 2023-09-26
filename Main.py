import math
import matplotlib.pyplot as plt
import numpy as np
import timeit
from PIL import Image
from Functions import *

ImgWidth, ImgHeight = 750, 750 

    
Pixels = np.empty([ImgHeight, ImgWidth, 3])
Pixels.fill(255)

# f(x) = 1/x, f(x) = x, f(x) = x^2, f(x) = sqrt(abs(x))
fx, fy = 't', 't^2'
xPoints1, yPoints1, r1, g1, b1 = 0, 0, 191, 191, 191
xPoints2, yPoints2, r2, g2, b2 = 1, 1, 0, 255, 0
xPoints3, yPoints3, r3, g3, b3 = 10, 10, 0, 0, 255
Scale = 1



xCirc1 = Coords('cos(t)', 1)
yCirc1 = Coords('sin(t)', 1)
Pixels = PixCalc(ImgHeight, ImgWidth, xCirc1, yCirc1, Pixels, 191, 191, 191)

xCirc2 = Coords('10*cos(t)', 1)
yCirc2 = Coords('10*sin(t)', 1)
Pixels = PixCalc(ImgHeight, ImgWidth, xCirc2, yCirc2, Pixels, 191, 191, 191)

tic=timeit.default_timer()

xCoordsScaled = Coords(fx, 1)

yCoordsScaled = Coords(fy, 1)
print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Prep + CalcArray + Scaler)')


xCirc1 = Coords('cos(t)', 1)
yCirc1 = Coords('sin(t)', 1)
Pixels = PixCalc(ImgHeight, ImgWidth, xCirc1, yCirc1, Pixels, 191, 191, 191)

xCirc2 = Coords('10*cos(t)', 1)
yCirc2 = Coords('10*sin(t)', 1)
Pixels = PixCalc(ImgHeight, ImgWidth, xCirc2, yCirc2, Pixels, 191, 191, 191)



tic=timeit.default_timer()
Pixels = PixCalc(ImgHeight, ImgWidth, xCoordsScaled, yCoordsScaled, Pixels, 0, 0, 0)
print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Calculating Pixels)')

tic=timeit.default_timer()
Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints1, yPoints1, Scale, r1, g1, b1)
# Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints2, yPoints2, Scale, r2, g2, b2)
# Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints3, yPoints3, Scale, r3, g3, b3)
print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (PointCreation)')

array = np.array(Pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')

plt.plot(xCoordsScaled, yCoordsScaled)
# plt.show()