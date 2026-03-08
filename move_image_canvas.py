from tkinter import *


def moving_up(event):
    canvas.move(myimage, 0, -10)


def moving_down(event):
    canvas.move(myimage, 0, 10)


def moving_left(event):
    canvas.move(myimage, -10, 0)


def moving_right(event):
    canvas.move(myimage, 10, 0)


window = Tk()
# binding with small w,s,a,d this does not work on capital W,A,S,D
window.bind("<w>", moving_up)
window.bind("<s>", moving_down)
window.bind("<a>", moving_left)
window.bind("<d>", moving_right)
# binding with arrow keys
window.bind("<Up>", moving_up)
window.bind("<Down>", moving_down)
window.bind("<Left>", moving_left)
window.bind("<Right>", moving_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage =PhotoImage(file='edit.png')
myimage = canvas.create_image(0,0,image=photoimage, anchor=NW)

window.mainloop()

