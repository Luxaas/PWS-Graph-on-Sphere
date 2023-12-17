def Prep(Func):
    function = ["cos", "sin", "tan", "sqrt", "atan"]
    Func = Func.replace(",", ".")
    Func = Func.replace("^", "**")
    for p in function:
        Func = Func.replace(p, "math."+p)
    Func = Func.replace("pi", "np.pi")
    Func = Func.replace("math.math", "math")
    return Func

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
            l = int(math.ceil(math.sqrt((yC[s + 1] - yC[s]) ** 2 + (xC[s + 1] - xC[s]) ** 2) * IH))
            x_range = np.linspace(xC[s], xC[s + 1], l)
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
