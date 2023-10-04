from functions import *
from tkinter import *

def convertion():
    mode = radio_state.get()
    num = entry.get()
    if mode == 0:
        r = dec_to_bin(num)
    elif mode == 1:
        r = bin_to_dec(num)
    elif mode == 2:
        r = hex_to_dec(num)
    elif mode == 3:
        r = dec_to_hex(num)
    elif mode == 4:
        r = bin_to_hex(num)
    else:
        r = hex_to_bin(num)
    entry.delete(0, END)
    entry.insert(0, str(r))


window = Tk()
window.title("Number basis conveter")
window.minsize(width=400, height=200)


radio_state = IntVar()
radiobutton0 = Radiobutton(text="10 to 2", value=0, variable=radio_state)
radiobutton1 = Radiobutton(text="2 to 10", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="16 to 10", value=2, variable=radio_state)
radiobutton3 = Radiobutton(text="10 to 16", value=3, variable=radio_state)
radiobutton4 = Radiobutton(text="2 to 16", value=4, variable=radio_state)
radiobutton5 = Radiobutton(text="16 to 2", value=5, variable=radio_state)

option_label = Label(text='Chose a mode')
option_label.grid(row=0, column=1)

for i in range(6):
    locals()[f'radiobutton{i}'].grid(row=i//3+1, column=i%3)

label_up = Label(text='Type a number to convert')
label_up.grid(row=3, column=1)
entry = Entry(width=36)
entry.grid(row=4, column=1)
button = Button(text='Convert', command=convertion)
button.grid(row=5, column=1)


window.mainloop()