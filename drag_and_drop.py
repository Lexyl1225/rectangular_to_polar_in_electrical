from tkinter import *


def drag_start(event):
   widget = event.widget
   widget.startX = event.x
   widget.startY = event.y

def drag_motion(event):
   widget = event.widget
   x = widget.winfo_x() - widget.startX + event.x   # event.x = current position , delta x = widget.winfo_x() - widget.startX
   y = widget.winfo_y() - widget.startY + event.y   # event.x = current position , delta x = widget.winfo_x() - widget.startX
   widget.place(x=x, y=y)

window = Tk()


label = Label(window, text="Test Block1", bg="red", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, text="Test Block2", bg="blue", width=10, height=5)
label2.place(x=100, y=100)


label.bind("<Button-1>", drag_start)      # first binding
label.bind("<B1-Motion>", drag_motion)    # second binding


label2.bind("<Button-1>", drag_start)       # first binding
label2.bind("<B1-Motion>", drag_motion)     # second binding


window.mainloop()

