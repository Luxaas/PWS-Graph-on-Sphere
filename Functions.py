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
    for T in np.linspace(-0.4999*np.pi, 0.4999*np.pi, (2**14 + 1)):
        num = math.tan(T)
        ftemp = PrepFunc.replace("value", str(num))
        try:
            coords.append(eval(ftemp))
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

def PixCalc(IW, IH, xC, yC):
    import numpy as np
    Pixels = np.empty([IH, IW, 3])
    Pixels.fill(255)
    for l in range(len(xC)):
        if xC[l] != 'skip' and yC[l] != 'skip':
            Pixels[int(-(round((yC[l]+1)*0.5*(IH))-1))][int(round((xC[l]+1)*0.5*(IW)-1))] = (0, 0, 0)
    return Pixels
