from PIL import Image
import numpy as np
im = Image.open("new.png")
a = np.asarray(im)
print(type(a[1]))