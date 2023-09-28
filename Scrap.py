
import math
import numpy as np

expression = "math.cos(200*t) * math.sin(0.5*t)"
exp_as_func = eval('lambda: ' + expression)
t = 2*np.pi
print(exp_as_func())