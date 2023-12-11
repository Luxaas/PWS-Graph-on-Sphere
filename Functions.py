def Prep(Func):
    function = ["cos", "sin", "tan", "sqrt", "atan", "log", "e"]
    Func = Func.replace(",", ".")
    Func = Func.replace("^", "**")
    for p in function:
        Func = Func.replace(p, "math."+p)
    Func = Func.replace("x", "t")    
    Func = Func.replace("pi", "np.pi")
    Func = Func.replace("math.math", "math")
    return Func

def PixCalc(IW, IH, xC, yC, Pixels, punten):
    import numpy as np
    import math
    xCl = []
    yCl = []
    a = 0
    # Construct xCl and yCl lists
    for s in range(punten-1):
        try:
            if (xC[s + 1] - xC[s]) != 0:
                a = (yC[s + 1] - yC[s]) / (xC[s + 1] - xC[s])
            c = yC[s] - (a * xC[s])
            l = int(math.sqrt((yC[s + 1] - yC[s]) ** 2 + (xC[s + 1] - xC[s]) ** 2) * IH)
            if l == 0:
                l = 1
            x_range = np.linspace(xC[s], xC[s + 1], l)
            y_range = [a * x + c for x in x_range]
            xCl.extend(x_range)
            yCl.extend(y_range)
        except:
            1+1

    # Ensure xCl and yCl are NumPy arrays
    xCl = np.array(xCl)
    yCl = np.array(yCl)

    # Compute pixel coordinates
    x_pixels = ((xCl + 1) * 0.5 * (IW - 1)).astype(int)
    y_pixels = (IH - 1) - ((yCl + 1) * 0.5 * (IH - 1)).astype(int)

    # Assign color values to Pixels using integer indexing
    Pixels[y_pixels, x_pixels, 0] = 0
    Pixels[y_pixels, x_pixels, 1] = 0
    Pixels[y_pixels, x_pixels, 2] = 0

    xCl = []
    yCl = []

    for s in range(punten, len(xC)-1):
        if (xC[s + 1] - xC[s]) != 0:
            a = (yC[s + 1] - yC[s]) / (xC[s + 1] - xC[s])
        c = yC[s] - (a * xC[s])
        l = int(math.sqrt((yC[s + 1] - yC[s]) ** 2 + (xC[s + 1] - xC[s]) ** 2) * IH)
        if l == 0:
            l = 1
        x_range = np.linspace(xC[s], xC[s + 1], l)
        y_range = [a * x + c for x in x_range]
        xCl.extend(x_range)
        yCl.extend(y_range)

    # Ensure xCl and yCl are NumPy arrays
    xCl = np.array(xCl)
    yCl = np.array(yCl)

    # Compute pixel coordinates
    x_pixels = ((xCl + 1) * 0.5 * (IW - 1)).astype(int)
    y_pixels = (IH - 1) - ((yCl + 1) * 0.5 * (IH - 1)).astype(int)

    # Assign color values to Pixels using integer indexing
    Pixels[y_pixels, x_pixels, 0] = 0.75 * Pixels[y_pixels, x_pixels, 0]
    Pixels[y_pixels, x_pixels, 1] = 0.75 * Pixels[y_pixels, x_pixels, 1]
    Pixels[y_pixels, x_pixels, 2] = 0.75 * Pixels[y_pixels, x_pixels, 2]
    return Pixels
    
