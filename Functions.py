def Prep(Func):
    function = ["cos", "sin", "tan", "sqrt"]
    Func = Func.replace(",", ".")
    Func = Func.replace("^", "**")
    for p in function:
        Func = Func.replace(p, "math."+p)
    Func = Func.replace("pi", "np.pi")
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
    for l in range(len(xC)):
        if xC[l] != 'skip' and yC[l] != 'skip':
            Pixels[int(-(round((yC[l]+1)*0.5*(IH))))][int(round((xC[l]+1)*0.5*(IW)-1))] = (r, g, b)
    return Pixels

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
    
