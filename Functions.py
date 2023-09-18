def Prep(Func):
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
    for T in np.linspace(-0*np.pi, 2*np.pi, 17):
        ftemp = PrepFunc.replace("t", str(T))
        ftemp = ftemp.replace("ma"+str(T)+"h", "math")
        print(ftemp)
        coords.append(round(eval(ftemp), 8))
    return coords