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
    for T in np.linspace(-0.4995*np.pi, 0.4995*np.pi, (2**5 + 1)):
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
