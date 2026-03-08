import math


def convert_ptr(polar_input):

    # taking Value of the Magnitude
    r = ""

    for i1 in polar_input:
        if i1 == "∠":
            break
        r += str(i1)
    # print(r)
    # print(r) to check the result of iteration

    wp = []

    for i1 in polar_input:
        wp += str(i1)

    wp.reverse()

    xp = []
    for i1 in wp:
        if i1 == "∠":
            break
        xp += i1

    xp.reverse()
    # print(x)
    # convert list to a single set of string
    # taking the string value of angle in yp

    yp = ""
    for i1 in xp:
        yp += i1

    # print(yp) #to check result of iteration
    # Convert yp to radian
    rad1 = math.radians(float(yp))

    # print("The rad value: " +  str(rad))

    real_x = round((float(r)) * (math.cos(rad1)), 12)   # Round float to 12 digits
    imag_y = round((float(r)) * (math.sin(rad1)), 12)

    # testing result only not part of the program
    # print("Cosine Result : " + str(rad))
    # print("Sine result : " +str(math.sin(int(float(rad)))))
    # print("The user input :  " + pol)
    # print("The real part is: " +str(real_x))
    # print("The imaginary part is:  " + str(imag_y))

    #z = (str(real_x) + "j" + str(imag_y))
    z_imag = ("j"+str(imag_y))

    # taking imaginary part to arrange (+jb or -jb)

    # step 1: Convert imaginary part to a list
    k1 = []
    for i1 in z_imag:
        k1 += i1
    #print("k1 value: "+ str(k1)) # to check content of k1
    # step 2: remove j operator
    k1.remove("j")
    # print( "-" in k1) # check if there is "-" negative sign in the list returns True or False
    if "-" in k1:  # no need to put == True:
        k1.insert(0,"-j")
        k1.remove("-")
        #print(k1)
    else:
        k1.insert(0,"+j")
    # print("k1 value: "+ str(k1))

    # step 3: Convert the list into concatenated string
    z_imaginary = ""
    for i1 in k1:
        z_imaginary += i1

    # print('Value of imaginary form :'+ z_imaginary)
    zf = (str(real_x) + str(z_imaginary))
    return zf


def getrinput_ptr(polar_input):
    # taking Value of the Magnitude
    r = ""

    for i2 in polar_input:
        if i2 == "∠":
            break
        r += str(i2)
    return r


def getangleinput_ptr(polar_input):

    wp = []

    for i3 in polar_input:
        wp += str(i3)

    wp.reverse()

    xp = []
    for i3 in wp:
        if i3 == "∠":
            break
        xp += i3

    xp.reverse()
    # print(x)
    # convert list to a single set of string
    # taking the string value of angle in y
    yp = ""
    for i3 in xp:
        yp += i3

    return yp


def getxresult_ptr(polar_input):

    r = ""
    for i4 in polar_input:
        if i4 == "∠":
            break
        r += str(i4)

    wp = []
    for i4 in polar_input:
        wp += str(i4)
    wp.reverse()

    xp = []
    for i4 in wp:
        if i4 == "∠":
            break
        xp += i4

    xp.reverse()
    yp = ""
    for i4 in xp:
        yp += i4

    rad1 = math.radians(float(yp))
    real_x = (float(r)) * (math.cos(rad1))
    return round(real_x, 12)


def getyresult_ptr(polar_input):

    r = ""
    for i5 in polar_input:
        if i5 == "∠":
            break
        r += str(i5)

    wp = []
    for i5 in polar_input:
        wp += str(i5)
    wp.reverse()

    xp = []
    for i5 in wp:
        if i5 == "∠":
            break
        xp += i5
    xp.reverse()

    yp = ""
    for i5 in xp:
        yp += i5

    rad1 = math.radians(int(float(yp)))

    imag_y = round((float(r)) * (math.sin(rad1)), 12)

    z_imag = ("j"+str(imag_y))

    k1 = []
    for i5 in z_imag:
        k1 += i5

    k1.remove("j")
    k2 = ""
    for i5 in k1:
        k2 += i5
    return k2











#polar_input1 = "1∠-45"
#print(convert_to_rec(polar_input1))
#print(get_input_mag(polar_input1))
#print(get_input_angle(polar_input1))
#print(get_result_ptr_real(polar_input1))
#print(get_result_ptr_imag(polar_input1))










