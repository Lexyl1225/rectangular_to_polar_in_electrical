from Pol_to_Rec import *
from Rec_to_Pol import *


# Adding Rectangular coordinates - result in Rectangular form

def add_rr(rec1, rec2):
    rcx = round(float(getxinput_rtp(rec1))+float(getxinput_rtp(rec2)), 16)
    rcy = round(float(getyinput_rtp(rec1))+float(getyinput_rtp(rec2)), 16)
    #print(rcx)
    #print(rcy)

    # convert imaginary part to a list and add "+j" or "-j" operator in the list in index 1
    g = []
    for i in str(rcy):
        g += i
    #print(g)

    if "-" in g:
        g.remove("-")
        g.insert(0, "-j")
    elif "+" in g:
        g.remove("+")
        g.insert(0, "+j")
    else:
        g.insert(0, "+j")

    # convert list to a concatenated string using for loop
    g1 = ""
    for i in g:
        g1 += i
    # print(g1)
    # print(str(rcy)+str(g1))
    return str(rcx)+str(g1)


# Subtraction of Rectangular Coordinates - result in Rectangular form


def sub_rr(rec1, rec2):
    rcx = round(float(getxinput_rtp(rec1)) - float(getxinput_rtp(rec2)), 16)
    rcy = round(float(getyinput_rtp(rec1)) - float(getyinput_rtp(rec2)), 16)
    # print(rcx)
    # print(rcy)

    # convert imaginary part to a list and add "+j" or "-j" operator in the list in index 1
    g = []
    for i in str(rcy):
        g += i
    # print(g)

    if "-" in g:
        g.remove("-")
        g.insert(0, "-j")
    elif "+" in g:
        g.remove("+")
        g.insert(0, "+j")
    else:
        g.insert(0, "+j")

    # convert list to a concatenated string using for loop
    g1 = ""
    for i in g:
        g1 += i
    # print(g1)
    # print(str(rcy)+str(g1))
    return str(rcx) + str(g1)


# Multiplication of Rectangular Coordinates -result in Rectangular form


def multi_rr(rec1, rec2):
    # convert to polar coordinates and stores value to a variable
    rcp1 = convert_rtp(rec1)
    rcp2 = convert_rtp(rec2)

    rcp12_eq = float(getrinput_ptr(rcp1))*float(getrinput_ptr(rcp2))
    angle_add = float(getangleinput_ptr(rcp1))+float(getangleinput_ptr(rcp2))

    rcp_eq = str(round(rcp12_eq, 12))+"∠"+str(round(angle_add, 12))

    #print(rcp_eq)  # the output is = r∠angle format need to convert to rectangular form
    return convert_ptr(rcp_eq)

# Division of Rectangular Coordinates - result in Rectangular form


def div_rr(rec1, rec2):
    # convert to polar coordinates and stores value to a variable
    rcp1 = convert_rtp(rec1)
    rcp2 = convert_rtp(rec2)
    rcp12_eq = 0
    angle_add = 0
    # Zero Division error handling
    if round(float(getrinput_ptr(rcp2)), 16) == 0:
        print("Dividing by zero is not Allowed")
    else:
        rcp12_eq = float(getrinput_ptr(rcp1)) / float(getrinput_ptr(rcp2))
        angle_add = float(getangleinput_ptr(rcp1)) - float(getangleinput_ptr(rcp2))


    rcp_eq = str(round(rcp12_eq, 12))+"∠"+str(round(angle_add, 12))

    #print(rcp_eq)  # the output is = r∠angle format need to convert to rectangular form
    return convert_ptr(rcp_eq)


# Addition of Rectangular Coordinate to Polar Coordinate - result in Rectangular form


def add_rp(rec1, pol1):
    # convert all to rectangular coordinates and stores value to a variable
    rcp1 = rec1
    rcp2 = convert_ptr(pol1)

    rcx_eq = round(float(getxinput_rtp(rcp1))+float(getxinput_rtp(rcp2)), 12)
    rcy_eq = round(float(getyinput_rtp(rcp1))+float(getyinput_rtp(rcp2)), 12)

    # convert imaginary part to a list and insert (+j) or (-j) operator
    list0 = []
    for i in str(rcy_eq):
        list0 += i

    if "-" in list0:
        list0.remove("-")
        list0.insert(0, "-j")
    elif "+" in list0:
        list0.remove("+")
        list0.insert(0, "+j")
    else:
        list0.insert(0, "+j")
    # convert list to a concatenated string
    # value of list is already updated from this line
    ry = ""
    for i in list0:
        ry += i

    rcxy_eq = str(rcx_eq)+str(ry)
    return rcxy_eq

    #print(rcxy_eq)


# Subtraction of Rectangular Coordinate to Polar Coordinate - result in Rectangular form


def sub_rp(rec1, pol1):
    # convert all to rectangular coordinates and stores value to a variable
    rcp1 = rec1
    rcp2 = convert_ptr(pol1)

    rcx_eq = round(float(getxinput_rtp(rcp1))-float(getxinput_rtp(rcp2)), 12)
    rcy_eq = round(float(getyinput_rtp(rcp1))-float(getyinput_rtp(rcp2)), 12)

    # convert imaginary part to a list and insert (+j) or (-j) operator
    list0 = []
    for i in str(rcy_eq):
        list0 += i

    if "-" in list0:
        list0.remove("-")
        list0.insert(0, "-j")
    elif "+" in list0:
        list0.remove("+")
        list0.insert(0, "+j")
    else:
        list0.insert(0, "+j")
    # convert list to a concatenated string
    # value of list is already updated from this line
    ry = ""
    for i in list0:
        ry += i

    rcxy_eq = str(rcx_eq)+str(ry)
    #print(rcxy_eq)
    return rcxy_eq


# Addition of Polar coordinate to Rectangular Coordinate


def add_pr(pol1, rec1):
    # convert all to rectangular coordinates and stores value to a variable
    rcp1 = rec1
    rcp2 = convert_ptr(pol1)

    rcx_eq = round(float(getxinput_rtp(rcp1)) + float(getxinput_rtp(rcp2)), 12)
    rcy_eq = round(float(getyinput_rtp(rcp1)) + float(getyinput_rtp(rcp2)), 12)

    # convert imaginary part to a list and insert (+j) or (-j) operator
    list0 = []
    for i in str(rcy_eq):
        list0 += i

    if "-" in list0:
        list0.remove("-")
        list0.insert(0, "-j")
    elif "+" in list0:
        list0.remove("+")
        list0.insert(0, "+j")
    else:
        list0.insert(0, "+j")
    # convert list to a concatenated string
    # value of list is already updated from this line
    ry = ""
    for i in list0:
        ry += i

    rcxy_eq = str(rcx_eq) + str(ry)
    return rcxy_eq


# Subtraction of Polar coordinate to Rectangular Coordinate


def sub_pr(pol1, rec1):
    # convert all to rectangular coordinates and stores value to a variable
    rcp1 = rec1
    rcp2 = convert_ptr(pol1)

    rcx_eq = round(float(getxinput_rtp(rcp2))-float(getxinput_rtp(rcp1)), 12)
    rcy_eq = round(float(getyinput_rtp(rcp2))-float(getyinput_rtp(rcp1)), 12)

    # convert imaginary part to a list and insert (+j) or (-j) operator
    list0 = []
    for i in str(rcy_eq):
        list0 += i

    if "-" in list0:
        list0.remove("-")
        list0.insert(0, "-j")
    elif "+" in list0:
        list0.remove("+")
        list0.insert(0, "+j")
    else:
        list0.insert(0, "+j")
    # convert list to a concatenated string
    # value of list is already updated from this line
    ry = ""
    for i in list0:
        ry += i

    rcxy_eq = str(rcx_eq) + str(ry)
    #print(rcxy_eq)
    return rcxy_eq

# Division of Rectangular coordinate to Polar Coordinate - Result in rectangular format


def div_rp(rec1, pol1):
    # convert rectangular coordinate to polar
    r_eq = 0
    angle_eq = 0
    pol2 = convert_rtp(rec1)
    # zero division error handling
    if round(float(getrinput_ptr(pol1)),12) == 0:
        print("Magnitude R cannot be zero")
    else:
        r_eq = round(float(getrinput_ptr(pol2))/float(getrinput_ptr(pol1)), 12)
        angle_eq = round(float(getangleinput_ptr(pol2))-float(getangleinput_ptr(pol1)), 12)

    rp_eq = str(r_eq)+"∠"+str(angle_eq)
    #print(rp_eq)
    #print(convert_ptr(rp_eq))
    return convert_ptr(rp_eq)


# Multiplication of Rectangular coordinate to Polar Coordinate - Result in rectangular format

def multi_rp(rec1, pol1):
    # convert rectangular coordinate to polar coordinate
    pol0 = convert_rtp(rec1)
    r01 = round(float(getrinput_ptr(pol0))*float(getrinput_ptr(pol1)), 12)
    angle01 = round(float(getangleinput_ptr(pol0))+float(getangleinput_ptr(pol1)), 12)
    rp_eq = str(r01)+"∠" + str(angle01)
    # convert polar coordinate to rectangular coordinate
    rpxy = convert_ptr(rp_eq)
    #print(rpxy)
    return rpxy


# Multiplication of Polar coordinate to Rectangular Coordinate - Result in rectangular format


def multi_pr(pol1, rec1):
    # convert rectangular coordinate to polar coordinate
    pol2 = convert_rtp(rec1)
    r01 = round(float(getrinput_ptr(pol2))*float(getrinput_ptr(pol1)), 12)
    angle01 = round(float(getangleinput_ptr(pol2))+float(getangleinput_ptr(pol1)), 12)
    rp_eq = str(r01)+"∠" + str(angle01)
    # convert polar coordinate to rectangular coordinate
    prxy = convert_ptr(rp_eq)
    #print(prxy)
    return prxy


# Division of Polar coordinate to Rectangular Coordinate - Result in rectangular format

def div_pr(pol1, rec1):
    # convert rectangular coordinate to polar
    r_eq = 0
    angle_eq = 0
    pol2 = convert_rtp(rec1)
    # formula (a∠b) / (c∠d) = (a/c)∠(b-d)
    # zero division error handling
    if round(float(getrinput_ptr(pol2)), 12) == 0:
        print("Zero Division is not Allowed")
    else:
        r_eq = round(float(getrinput_ptr(pol1))/float(getrinput_ptr(pol2)), 12)
        angle_eq = round(float(getangleinput_ptr(pol1))-float(getangleinput_ptr(pol2)), 12)

    rp_eq = str(r_eq)+"∠"+str(angle_eq)
    #print(rp_eq)
    #print(convert_ptr(rp_eq))
    return convert_ptr(rp_eq)


# Addition of Polar coordinate to Polar Coordinate - Result in rectangular format

def add_pp(pol1, pol2):
    # convert rectangular coordinate and get real values only and rounded off to 12 floating values
    recx_eq = round(float(getxresult_ptr(pol1))+float(getxresult_ptr(pol2)), 12)
    recy_eq = round(float(getyresult_ptr(pol1))+float(getyresult_ptr(pol2)), 12)
    # adding J operator to imaginary part
    # convert to list
    rcy = []
    for i in str(recy_eq):
        rcy += i

    if "-" in rcy:
        rcy.remove("-")
        rcy.insert(0, "-j")
    elif "+" in rcy:
        rcy.remove("+")
        rcy.insert(0, "+j")
    else:
        rcy.insert(0, "+j")
    # convert to concatenated string
    rcy_eq = ""
    for i in rcy:
        rcy_eq += i

    pp_eq = str(recx_eq)+str(rcy_eq)
    #print(pp_eq)
    return pp_eq


# Division of Polar coordinate to Polar Coordinate - Result in rectangular format

def div_pp(pol1, pol2):
    # zero division error handling
    req = 0
    if float(getrinput_ptr(pol2)) == 0:
        print("Zero Division is not allowed")
    else:
        req = round(float(getrinput_ptr(pol1))/float(getrinput_ptr(pol2)), 12)
    angle_eq = round(float(getangleinput_ptr(pol1))-float(getangleinput_ptr(pol2)), 12)

    pp_eq = str(req)+"∠"+str(angle_eq)

    return convert_ptr(pp_eq)


# Subtraction of Polar coordinate to Polar Coordinate - Result in rectangular format


def sub_pp(pol1, pol2):
    ppx = round(float(getxresult_ptr(pol1))-float(getxresult_ptr(pol2)), 12)
    ppy = round(float(getyresult_ptr(pol1))-float(getyresult_ptr(pol2)), 12)

    ppy_list = []
    for i in str(ppy):
        ppy_list += i

    if "-" in ppy_list:
        ppy_list.remove("-")
        ppy_list.insert(0, "-j")
    elif "+" in ppy_list:
        ppy_list.remove("+")
        ppy_list.insert(0, "+j")
    else:
        ppy_list.insert(0, "+j")

    ppyj = ""

    for i in ppy_list:
        ppyj += i

    pp_eq = str(ppx)+ppyj
    return pp_eq


# Multiplication of Polar coordinate to Polar Coordinate - Result in rectangular format


def multi_pp(pol1, pol2):

    req1 = round(float(getrinput_ptr(pol1))*float(getrinput_ptr(pol2)), 14)
    angle_eq1 = round(float(getangleinput_ptr(pol1))+float(getangleinput_ptr(pol2)), 14)
    pp_eqm = str(req1) + "∠" + str(angle_eq1)

    if abs(angle_eq1) > 360:
        pp_eqm1 = (convert_ptr(convert_rtp(convert_ptr(pp_eqm))))
    else:
        pp_eqm1 = convert_ptr(pp_eqm)

    return pp_eqm1





















#div_pr("20∠100", "1+j10")

#multi_rp("1+j10", "20∠100")























#add_rr("5.00012+j12.00", "1+j1.12345")
