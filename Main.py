def NewImg(xt, yt, zt, punten, oogx, oogy, oogz, color):
    import math
    import numpy as np
    import timeit
    from PIL import Image
    from Functions import PixCalc, Prep
    tictot=timeit.default_timer()
    ImgWidth, ImgHeight = 1000, 1000
    rgb = tuple(int((color.lstrip('#'))[i:i+2], 16) for i in (0, 2, 4))
    Pixels = np.full((ImgHeight, ImgWidth, 3), [rgb[0], rgb[1], rgb[2]], dtype=np.uint8)
    Oog = [float(oogx), float(oogy), float(oogz)]
    Scherm = [0, 0, -2]
    SchermCor = [0, 0]
    p = [0, 0, 0]
    Bakx = []
    Baky = []
    if punten == 'true':
        punten = 200000
    else:
        punten = 2000
    
        
    xt = float(xt)
    yt = float(yt)
    zt = float(zt)
    
    s = (Scherm[2]-Oog[2])/(0-Oog[2])
    for i in [0, 1]:
        SchermCor[i] = s*(0-Oog[i]) + Oog[i]

    for t in np.linspace(0, 2*np.pi, (int(punten)+1)):
        p[0] = math.cos(xt*t) * math.sin(0.5*t)
        p[1] = math.cos(yt*t)
        p[2] = math.sin(zt*t) * math.sin(0.5*t)
        # print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Pixels)')
        s = (Scherm[2]-Oog[2])/(p[2]-Oog[2])
        for i in [0, 1]:
            Scherm[i] = s*(p[i]-Oog[i]) + Oog[i]
        if Scherm[0]-SchermCor[0] <= 1 and Scherm[0]-SchermCor[0] >= -1:
            Bakx.append(Scherm[0]-SchermCor[0])
        else:
            Bakx.append("skip")
        if Scherm[1]-SchermCor[1] <=1 and Scherm[1]-SchermCor[1] >= -1:
            Baky.append(Scherm[1]-SchermCor[1])
        else:
            Baky.append('skip')
        # print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Pixels)')
    Pixels = PixCalc(ImgHeight, ImgWidth, Bakx, Baky, Pixels, 0, 0, 0)

    array = np.array(Pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    
    print(str(round((timeit.default_timer()-tictot)*1000, 8))+ 'ms (Total)')
    return new_image