import math


def convert_to_polar(user_input):

    a_real = 0
    a_imag = 0
    v = []
    for i in user_input:
        if i == "j":
            break
        v += str(i)
        # print(v)
    # removing the last item
    copyof_v = v.copy()
    v.pop()

    # taking the real Numbers
    z = ""
    for x in v:
        z = str(z)
        z += str(x)
        # print(z)

    a_real = z
    # print("the real part is "+a_real)
    # **************************************************************************************
    # taking the complex number
    w = []
    for i in user_input:
        w += str(i)
        # print(w)

    w.reverse()

    k = []
    for y in w:
        if y == "+":
            break
        elif y == "-":
            break
        k += str(y)
        # print(k)

    k.reverse()
    copyof_v.reverse()  # reversed copied list
    copyof_k = k.copy()
    k.insert(0, copyof_v[0])  # inserting list in k in the first index of the first index of the list copyof_v.reverse

    e = ""
    for y in k:
        e = str(e)
        e += str(y)
    a_imag = e

    without_j_with_sign = k
    without_j_with_sign.remove("j")

    # print(without_j_with_sign)

    # convert list to numbers with sign
    j_op = ""
    for i in without_j_with_sign:
        j_op = str(j_op)
        j_op += str(i)

    # print(j_op)

    r = int(float(a_real))*int(float(a_real))+int(float(j_op))*int(float(j_op))
    r_1 = float(math.sqrt(r))

    angle=0

    if  r_1==0:
        print("Nothing to Compute")
    elif int(float(a_real)) > 0 and int(float(j_op)) > 0: # 1st Quadrant
        angle = ((math.acos(int(float(a_real)) / r_1)) * (180 / math.pi))

    elif int(float(a_real)) < 0 < int(float(j_op)): # 2nd Quadrant
        angle = ((math.acos(int(float(j_op)) / r_1))*(180 / math.pi))+90

    elif int(float(a_real)) < 0 and int(float(j_op)) < 0:  # 3rd Quadrant
        angle = ((math.acos(abs(int(float(a_real))) / r_1)) * (180 / math.pi))-180

    elif int(float(a_real)) > 0 > int(float(j_op)):  # 4th Quadrant
        angle = ((math.acos(abs(int(float(j_op))) / r_1)) * (180 / math.pi))-90

    elif int(float(a_real)) > 0 and int(float(j_op)) == 0:  # 5 Real axis (x)
        angle = ((math.acos(int(float(a_real)) / r_1)) * (180 / math.pi))

    elif int(float(a_real)) == 0 and int(float(j_op)) < 0:  # 8 Imaginary axis (y)
        angle = ((math.acos(int(float(a_real)) / r_1)) * (180 / math.pi))-180

    else:   # for #6 and # 7 Imaginary and Real axis
        angle = ((math.acos(int(float(a_real)) / r_1)) * (180 / math.pi))

    #print("You have Entered Complex number: " + user_input)
    #print("Equivalent Polar Coordinate  = " + str(r_1) + "∠"+str(angle)+" Deg")
    p = str(r_1)+"∠"+str(angle)
    return p




# -123.123+j67.890



