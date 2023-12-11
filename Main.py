def NewImg(xt, yt, zt, punten, oogx, oogy, oogz):
    import math
    import matplotlib.pyplot as plt
    import numpy as np
    import timeit
    from PIL import Image
    from Functions import PixCalc, Prep
    import compiler
    tictot=timeit.default_timer()
    ImgWidth, ImgHeight = 750, 750
        
    Pixels = np.empty([ImgHeight, ImgWidth, 3])
    Pixels.fill(255)
    Oog = [float(oogx), float(oogy), float(oogz)]
    Scherm = [0, 0, -2]
    SchermCor = [0, 0]
    p = [0, 0, 0]
    Bakx = []
    Baky = []

    xt = Prep(xt)
    yt = Prep(yt)
    zt = Prep(zt)
    xtc = compile(xt, '<string>', 'eval')
    ytc = compile(yt, '<string>', 'eval')
    ztc = compile(zt, '<string>', 'eval')

    s = (Scherm[2]-Oog[2])/(0-Oog[2])
    for i in [0, 1]:
        SchermCor[i] = s*(0-Oog[i]) + Oog[i]

    tic=timeit.default_timer()
    for t in np.linspace(0, 2*np.pi, (int(punten)+1)):
        p[0] = eval(xtc)
        p[1] = eval(ytc)
        p[2] = eval(ztc)
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
    print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Calculating)')

    tic=timeit.default_timer()
    Pixels = PixCalc(ImgHeight, ImgWidth, Bakx, Baky, Pixels, 0, 0, 0)
    print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Pixels)')

    Scale = 1
    tic=timeit.default_timer()
    # array = np.array(Pixels, dtype=np.uint8)
    # new_image = Image.fromarray(array)
    # new_image.save('static/new.png')
    array = np.array(Pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    
    print(str(round((timeit.default_timer()-tic)*1000, 8))+ 'ms (Constructing Image)')
    
    print(str(round((timeit.default_timer()-tictot)*1000, 8))+ 'ms (Total)')
    return new_image
    # plt.plot(xCoordsScaled, yCoordsScaled)
    # plt.show()