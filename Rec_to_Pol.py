import math


def convert_rtp(rectangular_input):

    a_real = 0
    a_imag = 0

    v = []
    for rp in rectangular_input:
        if rp == "j":
            break
        v += str(rp)
        # print(v)
    # removing the last item
    copyof_v = v.copy()
    v.pop()

    # taking the real Numbers

    zp = ""
    for xr in v:
        zp = str(zp)
        zp += str(xr)
        # print(z)


    a_real = zp
    # print("the real part is "+a_real)
    # **************************************************************************************
    # taking the complex number
    w = []
    for rp in rectangular_input:
        w += str(rp)
        # print(w)

    w.reverse()

    k = []
    for y1 in w:
        if y1 == "+":
            break
        elif y1 == "-":
            break
        k += str(y1)
        # print(k)

    k.reverse()
    copyof_v.reverse()  # reversed copied list
    copyof_k = k.copy()
    k.insert(0, copyof_v[0])  # inserting list in k in the first index of the first index of the list copyof_v.reverse

    ep = ""
    for y1 in k:
        ep = str(ep)
        ep += str(y1)
    a_imag = ep

    without_j_with_sign = k
    without_j_with_sign.remove("j")

    # print(without_j_with_sign)

    # convert list to numbers with sign
    j_op = ""
    for rp in without_j_with_sign:
        j_op = str(j_op)
        j_op += str(rp)

    # print(j_op)

    r_0 = float(a_real)*float(a_real)+float(j_op)*float(j_op)
    r_1 = float(math.sqrt(r_0))

    angle = 0

    if r_1 == 0:
        print("Nothing to Compute")
    elif float(a_real) > 0 and float(j_op) > 0:  # 1st Quadrant
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))

    elif float(a_real) < 0 < float(j_op):  # 2nd Quadrant
        angle = ((math.acos(float(j_op) / r_1))*(180 / math.pi))+90

    elif float(a_real) < 0 and float(j_op) < 0:  # 3rd Quadrant
        angle = ((math.acos(abs(float(a_real)) / r_1)) * (180 / math.pi))-180

    elif float(a_real) > 0 > float(j_op):  # 4th Quadrant
        angle = ((math.acos(abs(float(j_op)) / r_1)) * (180 / math.pi))-90

    elif float(a_real) > 0 and float(j_op) == 0:  # 5 Real axis (x)
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))

    elif float(a_real) == 0 and float(j_op) < 0:  # 8 Imaginary axis (y)
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))-180

    else:   # for #6 and # 7 Imaginary and Real axis
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))

    #print("You have Entered Complex number: " + user_input)
    #print("Equivalent Polar Coordinate  = " + str(r_1) + "∠"+str(angle)+" Deg")
    p = str(round(r_1, 12))+"∠"+str(round(angle, 12))
    return p


def getxinput_rtp(rectangular_input):

    vp = []
    for i7 in rectangular_input:
        if i7 == "j":
            break
        vp += str(i7)
        # print(v)
    # removing the last item
    copyof_v = vp.copy()
    vp.pop()

    # taking the real Numbers

    zp = ""
    for x in vp:
        zp = str(zp)
        zp += str(x)
        # print(z)

    return zp


def getyinput_rtp(rectangular_input):

    vp = []

    for i8 in rectangular_input:
        if i8 == "j":
            break
        vp += str(i8)
        # print(v)
    # removing the last item
    copyof_v = vp.copy()
    vp.pop()

    # taking the real Numbers

    zp = ""

    for xp in vp:
        zp = str(zp)
        zp += str(xp)
        # print(z)

    wp = []

    for i8 in rectangular_input:
        wp += str(i8)
        # print(w)

    wp.reverse()

    k7 = []

    for y7 in wp:
        if y7 == "+":
            break
        elif y7 == "-":
            break
        k7 += str(y7)
        # print(k)

    k7.reverse()
    copyof_v.reverse()  # reversed copied list
    copyof_k7 = k7.copy()
    k7.insert(0, copyof_v[0])  # inserting list in k in the first index of the first index of the list copyof_v.reverse

    e = ""
    for y7 in k7:
        e = str(e)
        e += str(y7)
    a_imag = e

    without_j_with_sign = k7
    without_j_with_sign.remove("j")

    # convert list to concatenated string

    j_op = ""
    for i8 in without_j_with_sign:
        j_op = str(j_op)
        j_op += str(i8)

    return j_op


def getrad_rtp(rectangular_input):
    a_real = 0
    a_imag = 0


    vp = []

    for i8 in rectangular_input:
        if i8 == "j":
            break
        vp += str(i8)
        # print(v)
    # removing the last item
    copyof_v = vp.copy()
    vp.pop()

    # taking the real Numbers

    zp = ""
    for x in vp:
        zp = str(zp)
        zp += str(x)
        # print(z)

    a_real = zp
    # print("the real part is "+a_real)
    # **************************************************************************************
    # taking the complex number

    wp = []
    for i8 in rectangular_input:
        wp += str(i8)
        # print(w)

    wp.reverse()


    kp = []
    for y8 in wp:
        if y8 == "+":
            break
        elif y8 == "-":
            break
        kp += str(y8)
        # print(k)

    kp.reverse()
    copyof_v.reverse()  # reversed copied list
    copyof_kp = kp.copy()
    kp.insert(0, copyof_v[0])  # inserting list in k in the first index of the first index of the list copyof_v.reverse

    e = ""

    for y8 in kp:
        e = str(e)
        e += str(y8)
    a_imag = e

    without_j_with_sign = kp
    without_j_with_sign.remove("j")

    j_op = ""
    for i8 in without_j_with_sign:
        j_op = str(j_op)
        j_op += str(i8)

    r = float(a_real)*float(a_real)+float(j_op)*float(j_op)
    r_1 = float(math.sqrt(r))

    return round(r_1, 12)


def getangle_rtp(rectangular_input):
    a_real = 0
    a_imag = 0

    vp = []

    for i9 in rectangular_input:
        if i9 == "j":
            break
        vp += str(i9)
        # print(v)
    # removing the last item
    copyof_v = vp.copy()
    vp.pop()

    # taking the real Numbers
    zp = ""
    for x in vp:
        zp = str(zp)
        zp += str(x)
        # print(zp)


    a_real = zp
    # print("the real part is "+a_real)
    # **************************************************************************************
    # taking the complex number
    w = []
    for i9 in rectangular_input:
        w += str(i9)
        # print(w)

    w.reverse()

    kp = []

    for y10 in w:
        if y10 == "+":
            break
        elif y10 == "-":
            break

        kp += str(y10)
        # print(kp)

    kp.reverse()
    copyof_v.reverse()  # reversed copied list
    copyof_k = kp.copy()
    kp.insert(0, copyof_v[0])  # inserting list in k in the first index of the first index of the list copyof_v.reverse

    ep = ""

    for y10 in kp:
        ep = str(ep)
        ep += str(y10)
    a_imag = ep

    without_j_with_sign = kp
    without_j_with_sign.remove("j")

    # print(without_j_with_sign)

    # convert list to numbers with sign
    j_op = ""
    for i9 in without_j_with_sign:
        j_op = str(j_op)
        j_op += str(i9)

    # print(j_op)


    r_0 = float(a_real)*float(a_real)+float(j_op)*float(j_op)
    r_1 = float(math.sqrt(r_0))

    angle = 0

    if r_1 == 0:
        print("Nothing to Compute")
    elif float(a_real) > 0 and float(j_op) > 0:  # 1st Quadrant
        angle = ((math.acos(int(float(a_real)) / r_1)) * (180 / math.pi))

    elif float(a_real) < 0 < float(j_op): # 2nd Quadrant
        angle = ((math.acos(int(float(j_op)) / r_1))*(180 / math.pi))+90

    elif float(a_real) < 0 and float(j_op) < 0:  # 3rd Quadrant
        angle = ((math.acos(abs(float(a_real)) / r_1)) * (180 / math.pi))-180

    elif float(a_real) > 0 > float(j_op):  # 4th Quadrant
        angle = ((math.acos(abs(float(j_op)) / r_1)) * (180 / math.pi))-90

    elif float(a_real) > 0 and float(j_op) == 0:  # 5 Real axis (x)
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))

    elif float(a_real) == 0 and float(j_op) < 0:  # 8 Imaginary axis (y)
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))-180

    else:   # for #6 and # 7 Imaginary and Real axis
        angle = ((math.acos(float(a_real) / r_1)) * (180 / math.pi))

    #print("You have Entered Complex number: " + user_input)
    #print("Equivalent Polar Coordinate  = " + str(r_1) + "∠"+str(angle)+" Deg")

    return round(angle, 12)















# -123.123+j67.890



