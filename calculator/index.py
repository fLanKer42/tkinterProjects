#This index file will basically launch the GUI of the program
#main file
#A simple calculator.


class globe:
    f_num = 0
    sign = '_'

from tkinter import *
root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def build():
    #define buttons
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
    button_ad = Button(root, text="+", padx=39, pady=20, command=lambda: button_click('+'))
    button_sb = Button(root, text='-', padx=40, pady=20, command=lambda: button_click('-'))
    button_multi = Button(root, text='x', padx=40, pady=20, command=lambda: button_click('*'))
    button_div = Button(root, text='/', padx=40, pady=20, command=lambda: button_click('/'))
    button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: button_click('='))
    button_clear = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_click('clear'))

    #put buttons on screen
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_ad.grid(row=6, column=0)
    button_equal.grid(row=6, column=1, columnspan=2)

    button_sb.grid(row=5, column=0)
    button_multi.grid(row=5, column=1)
    button_div.grid(row=5, column=2)

    root.mainloop()

def button_click(number):
    if number == 'clear':
        e.delete(0, END)
        globe.f_num = 0
        globe.sign = '_'
        return
    elif number == '+':
        first_num = e.get()
        globe.f_num = int(first_num)
        if globe.sign == '+':
            first_num = first_num + globe.f_num
        globe.f_num = int(first_num)
        globe.sign = '+'
        e.delete(0, END)
        return
    elif number == '=':
        second_number = e.get()
        e.delete(0, END)
        if globe.sign == '+':
            e.insert(0, int(second_number) + globe.f_num)
            globe.sign = '_'
        elif globe.sign == '_':
            e.insert(0, int(second_number))
        elif globe.sign == '*':
            e.insert(0, int(second_number)* globe.f_num)
            globe.sign = '_'
        elif globe.sign == '-':
            e.insert(0, globe.f_num - int(second_number))
            globe.sign = '_'
        elif globe.sign == '/':
            e.insert(0, globe.f_num/int(second_number))
            globe.sign = '_'
        return
    elif number == '-':
        first_num = e.get()
        globe.f_num = int(first_num)
        globe.sign = '-'
        e.delete(0, END)
        return
    elif number == '*':
        first_num = e.get()
        globe.f_num = int(first_num)
        globe.sign = '*'
        e.delete(0, END)
        return
    elif number == '/':
        first_num = e.get()
        globe.f_num = int(first_num)
        globe.sign = '/'
        e.delete(0, END)
        return
    else :
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        return

build()
