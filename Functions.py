def Prep(Func):
    Func = Func.replace("t", "value")
    function = ["cos", "sin", "tan"]
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
    for T in np.linspace(-0.4995*np.pi, 0.4995*np.pi, (2**16 + 1)):
        num = math.tan(T)
        ftemp = PrepFunc.replace("value", str(num))
        coords.append(round(eval(ftemp), 8))
    return coords

def Scaler(CoordsList):
    import math
    import numpy as np
    tel = 0
    for coord in CoordsList:
        CoordsList[tel] = math.atan(coord)/(0.5*np.pi)
        tel +=1 
    return CoordsList

def PixCalc(IW, IH, xC, yC):
    import numpy as np
    Pixels = np.empty([IW, IH, 3])
    Pixels.fill(255)
    myC = min(yC)
    mxC = min(xC)
    maxC = max(xC)
    mayC = max(yC)
    for l in range(len(xC)):
        Pixels[int(round((yC[l]-myC)*(IH-1)))][int(round((xC[l]-mxC)*(IW-1)))] = (0, 0, 0)
    return Pixels
