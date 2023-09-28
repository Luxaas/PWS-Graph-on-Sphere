import math
import matplotlib.pyplot as plt
import numpy as np
import timeit
from PIL import Image
from Functions import *

ImgWidth, ImgHeight = 1000, 1000

    
Pixels = np.empty([ImgHeight, ImgWidth, 3])
Pixels.fill(255)

fx, fy, fz = 'cos(312*t)*sin(0,5*t)', 'cos(0.5*t)', 'sin(215*t) * sin(0,5*t)'
Oog = [0, 0, -5]
Scherm = [0, 0, -2]
SchermCor = [0, 0]
p = [0, 0, 0]
Bakx = []
Baky = []

fx = Prep(fx)
fy = Prep(fy)
fz = Prep(fz)
#  
# * math.sin(0.3*t)

s = (Scherm[2]-Oog[2])/(0-Oog[2])
for i in [0, 1]:
    SchermCor[i] = s*(0-Oog[i]) + Oog[i]

tic=timeit.default_timer()
for t in np.linspace(0, 2*np.pi, (2**17+1)):
    p[0] = math.cos(150*t) * math.sin(0.5*t)
    p[1] = math.cos(25*t)
    p[2] = math.sin(200*t) * math.sin(0.5*t)
    # print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Pixels)')
    s = (Scherm[2]-Oog[2])/(p[2]-Oog[2])
    for i in [0, 1]:
        Scherm[i] = s*(p[i]-Oog[i]) + Oog[i]
    Bakx.append(Scherm[0]-SchermCor[0])
    Baky.append(Scherm[1]-SchermCor[1])
    # print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Pixels)')
print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Calculating)')


tic=timeit.default_timer()
Pixels = PixCalc(ImgHeight, ImgWidth, Bakx, Baky, Pixels, 0, 0, 0)
print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Pixels)')



# f(x) = 1/x, f(x) = x, f(x) = x^2, f(x) = sqrt(abs(x))
fx, fy = 't', 't^2'
# xPoints1, yPoints1, r1, g1, b1 = 0, 0, 191, 191, 191
# xPoints2, yPoints2, r2, g2, b2 = 1, 1, 0, 255, 0
# xPoints3, yPoints3, r3, g3, b3 = 10, 10, 0, 0, 255
Scale = 1



# xCirc1 = Coords('cos(t)', 1)
# yCirc1 = Coords('sin(t)', 1)
# Pixels = PixCalc(ImgHeight, ImgWidth, xCirc1, yCirc1, Pixels, 191, 191, 191)

# xCirc2 = Coords('10*cos(t)', 1)
# yCirc2 = Coords('10*sin(t)', 1)
# Pixels = PixCalc(ImgHeight, ImgWidth, xCirc2, yCirc2, Pixels, 191, 191, 191)

# tic=timeit.default_timer()

# xCoordsScaled = Coords(fx, 1)

# yCoordsScaled = Coords(fy, 1)
# print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Prep + CalcArray + Scaler)')


# xCirc1 = Coords('cos(t)', 1)
# yCirc1 = Coords('sin(t)', 1)
# Pixels = PixCalc(ImgHeight, ImgWidth, xCirc1, yCirc1, Pixels, 191, 191, 191)

# xCirc2 = Coords('10*cos(t)', 1)
# yCirc2 = Coords('10*sin(t)', 1)
# Pixels = PixCalc(ImgHeight, ImgWidth, xCirc2, yCirc2, Pixels, 191, 191, 191)



# tic=timeit.default_timer()
# Pixels = PixCalc(ImgHeight, ImgWidth, xCoordsScaled, yCoordsScaled, Pixels, 0, 0, 0)
# print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Calculating Pixels)')

# tic=timeit.default_timer()
# Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints1, yPoints1, Scale, r1, g1, b1)
# Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints2, yPoints2, Scale, r2, g2, b2)
# Pixels = PointCreation(Pixels, ImgHeight, ImgWidth, xPoints3, yPoints3, Scale, r3, g3, b3)
# print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (PointCreation)')

array = np.array(Pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')

# plt.plot(xCoordsScaled, yCoordsScaled)
# plt.show()