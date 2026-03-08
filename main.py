from tkinter import*
from complex_electrical_calc import*


window = Tk()
window.iconbitmap('IIEE2.ico')
window.title("DELA>WYE / WYE>DELTA CONVERTER BY ENGR. APF")
window.geometry('1080x1200')
window.config(padx=10, pady=10)

solsample =''


def convert():
    global zaa, zbb, zcc, solsample

    entry_box = []
    entry_box.insert(0, zab.get())
    entry_box.insert(1, zbc.get())
    entry_box.insert(2, zca.get())
    print("Delta Load Entered ['Zab','Zbc','Zca'] = " + str(entry_box))
    # formula Za = (Zab)(Zca)/(Zab+Zbc+Zca) , Zb = (Zab)(Zbc)/(Zab+Zbc+Zca) , Zc = (Zbc)(Zca)/(Zab+Zbc+Zca)
    za = div_pr(convert_rtp(multi_rr(entry_box[0], entry_box[2])), add_rr(add_rr(entry_box[0], entry_box[1]), entry_box[2]))
    zb = div_pr(convert_rtp(multi_rr(entry_box[0], entry_box[1])), add_rr(add_rr(entry_box[0], entry_box[1]), entry_box[2]))
    zc = div_pr(convert_rtp(multi_rr(entry_box[1], entry_box[2])), add_rr(add_rr(entry_box[0], entry_box[1]), entry_box[2]))
    print("Formula for DELTA-WYE : \nZa = (Zab)(Zca)/(Zab+Zbc+Zca)\nZb = (Zab)(Zbc)/(Zab+Zbc+Zca)\nZc = (Zbc)(Zca)/(Zab+Zbc+Zca) ")
    print("Wye Load Equivalent : " + "\nZa = " + str(za) + "\n" + "Zb = " + str(zb) + "\n" + "Zc = " + str(zc))
    solsample = "Wye Load Equivalent : " + "\nZa = " + str(za) + "\n" + "Zb = " + str(zb) + "\n" + "Zc = " + str(zc)

    mylabel_result = Label(window, text="Result in a+jb: ", fg="red", width=10, height=1)
    mylabel_result.grid(row=5, column=0, rowspan=1)


    mylabel_Za = Label(window, text="Za", fg="red", width=5)
    mylabel_Za.grid(row=6, column=0, rowspan=1)

    mylabel_Zb = Label(window, text="Zb", fg="red", width=5)
    mylabel_Zb.grid(row=7, column=0, rowspan=1)

    mylabel_Zc = Label(window, text="Zc", fg="red", width=5)
    mylabel_Zc.grid(row=8, column=0, rowspan=1)

    za_entry = Entry(window, width=30)
    za_entry.grid(row=6, column=1)
    za_entry.insert(0, za)
    zaa = za_entry


    zb_entry = Entry(window, width=30)
    zb_entry.grid(row=7, column=1)
    zb_entry.insert(0, zb)
    zbb = zb_entry



    zc_entry = Entry(window, width=30)
    zc_entry.grid(row=8, column=1)
    zc_entry.insert(0, zc)
    zcc = zc_entry


    mybutton_convert = Button(window, width=10, bg="#ff6813", text="Convert a∠θ", command=convert_ab)
    mybutton_convert.grid(row=5, column=1, )


def convert_ab():
    mylabel_result = Label(window, text="Result in a∠θ: ", fg="#ff6813", width=10, height=1)
    mylabel_result.grid(row=9, column=0, rowspan=1)

    mylabel_Za = Label(window, text="Za", fg="#ff6813", width=5)
    mylabel_Za.grid(row=10, column=0, rowspan=1)

    mylabel_Zb = Label(window, text="Zb", fg="#ff6813", width=5)
    mylabel_Zb.grid(row=11, column=0, rowspan=1)

    mylabel_Zc = Label(window, text="Zc", fg="#ff6813", width=5)
    mylabel_Zc.grid(row=12, column=0, rowspan=1)

    pp1 = convert_rtp(zaa.get())
    zap_entry = Entry(window, width=30)
    zap_entry.grid(row=10, column=1)
    zap_entry.insert(0, pp1)

    pp2 = convert_rtp(zbb.get())
    zbp_entry = Entry(window, width=30)
    zbp_entry.grid(row=11, column=1)
    zbp_entry.insert(0, pp2)

    pp3 = convert_rtp(zcc.get())
    zcp_entry = Entry(window, width=30)
    zcp_entry.grid(row=12, column=1)
    zcp_entry.insert(0, pp3)

    print("Result in a∠θ: " + "Za = " + str(pp1) + ", " + "Zb = " + str(pp2) + ", " + "Zc = " + str(pp3))


def convert1():
    global zaa_wye, zbb_wye, zcc_wye

    entry_box1 = []
    entry_box1.insert(0, za_wye.get())
    entry_box1.insert(1, zb_wye.get())
    entry_box1.insert(2, zc_wye.get())
    print("Wye Load Entered ['Zab','Zbc','Zca'] = " + str(entry_box1))
    # formula Zab = ((Za)(Zb)+(Za)(Zc)+(Zb)(Zc))/Zc , Zbc = ((Za)(Zb)+(Za)(Zc)+(Zb)(Zc))/Za , Zca = Zbc = ((Za)(Zb)+(Za)(Zc)+(Zb)(Zc))/Zb
    zab_result = div_rr(add_rr(add_rr(multi_rr(entry_box1[0], entry_box1[1]), multi_rr(entry_box1[0], entry_box1[2])), multi_rr(entry_box1[1], entry_box1[2])), entry_box1[2])
    zbc_result = div_rr(add_rr(add_rr(multi_rr(entry_box1[0], entry_box1[1]), multi_rr(entry_box1[0], entry_box1[2])), multi_rr(entry_box1[1], entry_box1[2])), entry_box1[0])
    zca_result = div_rr(add_rr(add_rr(multi_rr(entry_box1[0], entry_box1[1]), multi_rr(entry_box1[0], entry_box1[2])), multi_rr(entry_box1[1], entry_box1[2])), entry_box1[1])
    print(
        "Formula for WYE-DELTA : \nZab = ((Za)(Zb)+(Za)(Zc)+(Zb)(Zc))/Zc\nZbc = ((Za)(Zb)+(Za)(Zc)+(Zb)(Zc))/Za\nZca = Zbc = ((Za)(Zb)+(Za)(Zc)+(Zb)(Zc))/Zb")
    print("DELTA Load Equivalent : " + "\nZab = " + str(zab_result) + "\n" + "Zbc = " + str(zbc_result) + "\n" + "Zca = " + str(zca_result))

    mylabel_result1 = Label(window, text="Result in a+jb: ", fg="#990bb9", width=10, height=1)
    mylabel_result1.grid(row=5, column=5, rowspan=1)

    mylabel_Zab = Label(window, text="Zab", fg="#990bb9", width=5)
    mylabel_Zab.grid(row=6, column=5, rowspan=1)

    mylabel_Zbc = Label(window, text="Zbc", fg="#990bb9", width=5)
    mylabel_Zbc.grid(row=7, column=5, rowspan=1)

    mylabel_Zca = Label(window, text="Zca", fg="#990bb9", width=5)
    mylabel_Zca.grid(row=8, column=5, rowspan=1)

    zab_entry = Entry(window, width=30)
    zab_entry.grid(row=6, column=6)
    zab_entry.insert(0, zab_result)
    zaa_wye = zab_entry

    zbc_entry = Entry(window, width=30)
    zbc_entry.grid(row=7, column=6)
    zbc_entry.insert(0, zbc_result)
    zbb_wye = zbc_entry

    zca_entry = Entry(window, width=30)
    zca_entry.grid(row=8, column=6)
    zca_entry.insert(0, zca_result)
    zcc_wye = zca_entry

    mybutton_convert = Button(window, width=10, bg="#990bb9", text="Convert a∠θ", command=convert_ba)
    mybutton_convert.grid(row=5, column=6, )


def convert_ba():
    mylabel_result = Label(window, text="Result in a∠θ: ", fg="#990bb9", width=10, height=1)
    mylabel_result.grid(row=9, column=5, rowspan=1)

    mylabel_Zab = Label(window, text="Zab", fg="#990bb9", width=5)
    mylabel_Zab.grid(row=10, column=5, rowspan=1)

    mylabel_Zbc = Label(window, text="Zbc", fg="#990bb9", width=5)
    mylabel_Zbc.grid(row=11, column=5, rowspan=1)

    mylabel_Zca = Label(window, text="Zca", fg="#990bb9", width=5)
    mylabel_Zca.grid(row=12, column=5, rowspan=1)

    pp1_wye = convert_rtp(zaa_wye.get())
    zap_entry = Entry(window, width=30)
    zap_entry.grid(row=10, column=6)
    zap_entry.insert(0, pp1_wye)

    pp2_wye = convert_rtp(zbb_wye.get())
    zbp_entry = Entry(window, width=30)
    zbp_entry.grid(row=11, column=6)
    zbp_entry.insert(0, pp2_wye)

    pp3_wye = convert_rtp(zcc_wye.get())
    zcp_entry = Entry(window, width=30)
    zcp_entry.grid(row=12, column=6)
    zcp_entry.insert(0, pp3_wye)

    print("Result in a∠θ: " + "Zab = " + str(pp1_wye) + ", " + "Zbc = " + str(pp2_wye) + ", " + "Zca = " + str(pp3_wye))


canvas = Canvas(window, height=567, width=500,bg="white")
#canvas.create_line(0,0,500,500,fill="blue", width=5)
#canvas.create_line(0,500,500,0,fill="red", width=5)
#canvas.create_rectangle(50,50,250,250, fill = "purple")
#points = [250,0,0,500,100,100]
# delta main
points = [0, 500, 250, 67, 500, 500]
# delta points
points_bc = [205, 489, 295, 489, 295, 511, 205, 511]
points_ca = [93, 317, 138, 239, 157, 250, 112, 328]
points_ab = [343, 250, 362, 239, 407, 317, 388, 329]
# wye points
points_a = [239, 257, 239, 166, 261, 166, 261, 257]
points_b = [330, 415, 341, 396, 420, 441, 409, 460]
points_c = [80, 441, 159, 396, 170, 415, 91, 460]

canvas.create_polygon(points, fill="orange", outline="black", width=3)   # passing coordinates points
# wye line A
canvas.create_line(250, 67, 250, 356, fill="blue", width=3)
# wye line B
canvas.create_line(250, 356, 500, 500, fill="blue", width=3)
# wye line C
canvas.create_line(250, 356, 0, 500, fill="blue", width=3)

# delta loads
# Phase BC
canvas.create_polygon(points_bc, fill="orange", outline="black", width=3)
canvas.create_text(250, 500, fill="red", text="Zbc")

# Phase CA
canvas.create_polygon(points_ca, fill="orange", outline="black", width=3)
canvas.create_text(125, 283, fill="red", text="Zca")
# Phase AB
canvas.create_polygon(points_ab, fill="orange", outline="black", width=3)
canvas.create_text(375, 283, fill="red", text="Zab")

# wye loads
# phase a
canvas.create_polygon(points_a, fill="cyan", outline="blue", width=3)
canvas.create_text(250, 211, fill="red", text="Za")
# phase b
canvas.create_polygon(points_b, fill="cyan", outline="blue", width=3)
canvas.create_text(375, 428, fill="red", text="Zb")
# phase c
canvas.create_polygon(points_c, fill="cyan", outline="blue", width=3)
canvas.create_text(125, 428, fill="red", text="Zc")



#canvas.create_arc(0,0,500,500, fill="green",style=PIESLICE,start=90)
#canvas.create_arc(0,0,500,500, fill="red",extent=180,width=10)
#canvas.create_arc(0,0,500,500, fill="white",extent=180,start=180,width=10)
#canvas.create_oval(190,190,310,310, fill="white", width=10)
canvas.grid(row=1, column=3, columnspan=2, rowspan=50)

#*******************************************************************************

mybutton = Button(window, width=10, bg="#ff6813", text="Compute", command=convert)
mybutton.grid(row=1, column=0,)

mylabel_button = Label(window, text="DELTA - WYE (a+jb)", fg="green")
mylabel_button.grid(row=1, column=1)


#Phase AB input
mylabel_ab = Label(window, text="Zab", width=5, fg="#b604ff")
mylabel_ab.grid(row=2, column=0)

zab = Entry(window, width=30)
zab.grid(row=2, column=1)

#Phase BC input
mylabel_bc = Label(window, text="Zbc", width=5, fg="#b604ff")
mylabel_bc.grid(row=3, column=0)

zbc = Entry(window, width=30)
zbc.grid(row=3, column=1)


#Phase CA input
mylabel_ca = Label(window, text="Zca", width=5, fg="#b604ff")
mylabel_ca.grid(row=4,column=0)

zca = Entry(window, width=30)
zca.grid(row=4, column=1)

#**********************************************************************************

mybutton1 = Button(window, width=10, bg="#990bb9", text="Compute", command=convert1)
mybutton1.grid(row=1, column=5,)

mylabel_button1 = Label(window, text="WYE - DELTA (a+jb)", fg="green")
mylabel_button1.grid(row=1, column=6)

#Phase A input
mylabel_a = Label(window, text="Za", width=5, fg="#e75802")
mylabel_a.grid(row=2, column=5)

za_wye = Entry(window, width=30)
za_wye.grid(row=2, column=6)

#Phase B input
mylabel_b = Label(window, text="Zb", width=5, fg="#e75802")
mylabel_b.grid(row=3, column=5)

zb_wye = Entry(window, width=30)
zb_wye.grid(row=3, column=6)

#Phase C input
mylabel_c = Label(window, text="Zb", width=5, fg="#e75802")
mylabel_c.grid(row=4, column=5)

zc_wye = Entry(window, width=30)
zc_wye.grid(row=4, column=6)

# Solution Entry

mylabel_sol= Label(window, text="Solution", width=10, fg="#e75802")
mylabel_sol.grid(row=51, column=0)

sol_text = Text(window, fg="#e75802", bg="#fcfce5")
sol_text.grid(row=52, column=0, columnspan=20)
sol_text.insert(1.0, solsample)


#************************************************************************************

mylabel = Label(window, text="DELTA - WYE / WYE - DELTA CONVERTER", font=20, fg="#ff7902")
mylabel.grid(row=0, column=1, columnspan=6)
window.mainloop()



