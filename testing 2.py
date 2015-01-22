from tkinter import *


mGui = Tk()
mGui.title('Title')

v = StringVar()

# Variable to hold the input
inp = None

L1 = Label(mGui, text = 'Name')
L1.pack(side = LEFT)

E1 = Entry(mGui, textvariable = v, bd = 5)
E1.pack(side = RIGHT)

def userinput():
    # Declare 'inp' to be global
    global inp
    a = input(v.get())
   
    # Update the variable
    inp = a


b = Button(mGui, text = 'Submit', command = userinput)
b.pack(side = BOTTOM)


mGui.mainloop()
