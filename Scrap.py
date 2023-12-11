import numpy as np

a = np.linspace(xC[s], xC[s + 1], int(math.sqrt((yC[s + 1] - yC[s]) ** 2 + (xC[s + 1] - xC[s]) ** 2) * IH))
