def Prep(Func):
    function = ["cos", "sin", "tan", "sqrt", "atan"]
    Func = Func.replace(",", ".")
    Func = Func.replace("^", "**")
    for p in function:
        Func = Func.replace(p, "math."+p)
    Func = Func.replace("pi", "np.pi")
    Func = Func.replace("math.math", "math")
    return Func
    
def CalcArray(PrepFunc):
    import math
    import numpy as np
    coords = []
    for T in np.linspace(-0.4999*np.pi, 0.4999*np.pi, (2**16 + 1)):
        t = math.tan(T)
        try:
            coords.append(eval(PrepFunc))
        except ZeroDivisionError:
            coords.append('skip')
            
    return coords

def Scaler(CoordsList, Scale):
    import math
    import numpy as np
    tel = 0
    for coord in CoordsList:
        if coord != 'skip':
            CoordsList[tel] = (math.atan(coord*Scale))/(0.5*np.pi)
        tel +=1 
    return CoordsList




def PixCalc(IW, IH, xC, yC, Pixels, r, g, b):
    import numpy as np
    import math
    xCl = []
    yCl = []

    # Construct xCl and yCl lists, filtering out 'skip' values
    for s in range(len(xC) - 1):
        if xC[s] != 'skip' and yC[s] != 'skip' and xC[s + 1] != 'skip' and yC[s + 1] != 'skip':
            a = (yC[s + 1] - yC[s]) / (xC[s + 1] - xC[s])
            b = yC[s] - (a * xC[s])
            x_range = np.linspace(xC[s], xC[s + 1], int(math.sqrt((yC[s + 1] - yC[s]) ** 2 + (xC[s + 1] - xC[s]) ** 2) * IH))
            y_range = [a * x + b for x in x_range]
            xCl.extend(x_range)
            yCl.extend(y_range)

    # Ensure xCl and yCl are NumPy arrays
    xCl = np.array(xCl)
    yCl = np.array(yCl)

    # Compute pixel coordinates
    x_pixels = ((xCl + 1) * 0.5 * (IW - 1)).astype(int)
    y_pixels = (IH - 1) - ((yCl + 1) * 0.5 * (IH - 1)).astype(int)

    # Compute color values using vectorized operations
    Rs = np.linspace(0, 2 * np.pi, len(xCl))
    r_values = (255 * np.sin(Rs)).astype(np.uint8)
    g_values = (255 * np.sin(Rs + (2 / 3 * np.pi))).astype(np.uint8)
    b_values = (255 * np.sin(Rs + (4 / 3 * np.pi))).astype(np.uint8)

    # Assign color values to Pixels using integer indexing
    Pixels[y_pixels, x_pixels, 0] = r_values
    Pixels[y_pixels, x_pixels, 1] = g_values
    Pixels[y_pixels, x_pixels, 2] = b_values

    return Pixels


# def PixCalc(IW, IH, xC, yC, Pixels, r, g, b):
#     import numpy as np
#     import math
#     import timeit
#     Rs = np.linspace(0, 2*np.pi, len(xC))
#     for l in range(len(xC)):
#         if xC[l] != 'skip' and yC[l] != 'skip':
#             Pixels[int(-(round((yC[l]+1)*0.5*(IH))-1))-1][int(round((xC[l]+1)*0.5*(IW)-1))-1] = (255*math.sin(Rs[l]), 255*math.sin(Rs[l]+(2/3 * np.pi)), 255*math.sin(Rs[l]+(4/3*np.pi)))
#     return Pixels

def PointCreation(Pixels, IH, IW, X, Y, Scale, r, g, b):
    import numpy as np
    import math
    ts = np.linspace(0, 2*np.pi, 101)
    PosX = int(((math.atan(X*Scale)/np.pi))*IW+0.5*IW)
    PosY = int(-((math.atan(Y*Scale)/np.pi))*IH+0.5*IH)
    for t in ts: 
        # Pixels[int((math.atan(X*Scale)*0.3 + (IW/20000)*math.cos(float(t)))*IW + 0.5*IW)][int((math.atan(Y*Scale)*0.3 + (IH/20000)*math.sin(float(t)))*IH + 0.5*IH)] = (255, 0, 255)
        CirX = int(PosX + (IW/100)*math.cos(float(t)))
        CirY = int(PosY + (IH/100)*math.sin(float(t)))
        Pixels[CirY][CirX] = (r, g, b)
    return(Pixels)
    
def Coords(f, scale):
    f = Prep(f)
    f = CalcArray(f)
    return Scaler(f, scale)
    
