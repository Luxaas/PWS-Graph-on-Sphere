def NewImg(yt, punten, oogx, oogy, oogz, r):
    import math
    import matplotlib.pyplot as plt
    import numpy as np
    import timeit
    from PIL import Image
    from Functions import PixCalc, Prep
 
    punten = int(punten)
    tictot=timeit.default_timer()
    ImgWidth, ImgHeight = 750, 750
        
    Pixels = np.empty([ImgHeight, ImgWidth, 3])
    Pixels.fill(255)
    Oog = [float(oogx), -1*float(oogy), float(oogz)]
    Scherm = [0, 0, -2]
    SchermCor = [0, 0]
    p = [0, 0, 0]
    Bakx = []
    Baky = []
    k = [0, 0]
    xt = "t"
    yt = Prep(yt)
    xtc = compile(xt, '<string>', 'eval')
    ytc = compile(yt, '<string>', 'eval')
    po = 0
    s = (Scherm[2]-Oog[2])/(0-Oog[2])
    for i in [0, 1]:
        SchermCor[i] = s*(0-Oog[i]) + Oog[i]
    for t in np.linspace(-0.5*np.pi, 0.5*np.pi, (punten+1)):
        t = math.tan(t)
        po += 1
        try: 
            k[1] = eval(ytc)
        except:
            1+1
        else:
            k[0] = eval(xtc)
        r = float(r)
        
        p[0] = (2*r*k[0])/(r**2+k[0]**2+k[1]**2)
        p[1] = (2*r*k[1])/(r**2+k[0]**2+k[1]**2)
        p[2] = (r**2-k[0]**2-k[1]**2)/(r**2+k[0]**2+k[1]**2)
        s = (Scherm[2]-Oog[2])/(p[2]-Oog[2])
        for i in [0, 1]:
            Scherm[i] = s*(p[i]-Oog[i]) + Oog[i]
        if Scherm[0]-SchermCor[0] <= 1 and Scherm[0]-SchermCor[0] >= -1:
            Bakx.append(Scherm[0]-SchermCor[0])
        if Scherm[1]-SchermCor[1] <=1 and Scherm[1]-SchermCor[1] >= -1:
            Baky.append(Scherm[1]-SchermCor[1])

    for t in np.linspace(-np.pi, np.pi, 200):
        p[0] = math.sin(t)
        p[1] = 0
        p[2] = math.cos(t)
        s = (Scherm[2]-Oog[2])/(p[2]-Oog[2])
        for i in [0, 1]:
            Scherm[i] = s*(p[i]-Oog[i]) + Oog[i]
        if Scherm[0]-SchermCor[0] <= 1 and Scherm[0]-SchermCor[0] >= -1:
            Bakx.append(Scherm[0]-SchermCor[0])
        if Scherm[1]-SchermCor[1] <=1 and Scherm[1]-SchermCor[1] >= -1:
            Baky.append(Scherm[1]-SchermCor[1])

    for t in np.linspace(-np.pi, 1.01*np.pi, 200):
        p[0] = 0
        p[1] = math.sin(t)
        p[2] = math.cos(t)
        s = (Scherm[2]-Oog[2])/(p[2]-Oog[2])
        for i in [0, 1]:
            Scherm[i] = s*(p[i]-Oog[i]) + Oog[i]
        if Scherm[0]-SchermCor[0] <= 1 and Scherm[0]-SchermCor[0] >= -1:
            Bakx.append(Scherm[0]-SchermCor[0])
        if Scherm[1]-SchermCor[1] <=1 and Scherm[1]-SchermCor[1] >= -1:
            Baky.append(Scherm[1]-SchermCor[1])
        
    Pixels = PixCalc(ImgHeight, ImgWidth, Bakx, Baky, Pixels, punten)
  
    array = np.array(Pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)

    print(str(round((timeit.default_timer()-tictot)*1000, 8))+ 'ms (Total)')
    return new_image