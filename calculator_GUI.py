from tkinter import *
import tkinter as tk
import math, re

root = Tk()
root.title("Calculator")

def button_click(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

def button_clear():
    screen.delete(0, END)
    
def write_result(result):
    if result % 1 > 0:
        screen.insert(0, result)
    else:
        screen.insert(0, int(result))

def replace_sqrt(text):
    result = ""
    tmp = False
    for c in text:
        if tmp:
            if not re.fullmatch("[0-9]+", c):
                result += ")"
                tmp = False
        if c == '√':
            if len(result) > 0 and re.fullmatch("[0-9]+", result[len(result) - 1]):
                result += "*"
            result += "math.sqrt("
            tmp = True
            continue
        result += c
    if tmp:
        result += ")"
    return result

def button_equal():
    value = screen.get()
    screen.delete(0, END)
    value = value.replace("x", "*")
    value = value.replace("÷", "/")
    value = value.replace("²", "**2")
    value = replace_sqrt(value)
    
    try:
        result = eval(value) 
        write_result(result)
    except ZeroDivisionError:
        screen.insert(0, "Error!")

# ------------------------------1-line-----------------------------------------------

# Screen
screen = Entry(root, width=28, borderwidth=10, insertwidth=3)
screen.grid(row=0, column=0, columnspan=10)

# ------------------------------2-line-----------------------------------------------

# Buttons
button_clear = Button(root, text='CE', command=button_clear)
button_sqr = Button(root, text='x²', command=lambda: button_click('²'))
button_sqrt = Button(root, text='√', command=lambda: button_click('√'))
button_div = Button(root, text='÷', command=lambda: button_click('÷'))

button_clear.grid(row=1, column=0)
button_sqr.grid(row=1, column=1)
button_sqrt.grid(row=1, column=2)
button_div.grid(row=1, column=3)

# ------------------------------3-line-----------------------------------------------

button_7= Button(root, text='7', command=lambda: button_click(7))
button_8= Button(root, text='8', command=lambda: button_click(8))
button_9 = Button(root, text='9', command=lambda: button_click(9))
button_mul = Button(root, text='x', command=lambda: button_click('x'))

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

# ------------------------------4-line-----------------------------------------------

button_4= Button(root, text='4', command=lambda: button_click(4))
button_5 = Button(root, text='5', command=lambda: button_click(5))
button_6 = Button(root, text='6', command=lambda: button_click(6))
button_sub = Button(root, text='-', command=lambda: button_click('-'))

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

# ------------------------------5-line-----------------------------------------------

button_1 = Button(root, text='1', command=lambda: button_click(1))
button_2 = Button(root, text='2', command=lambda: button_click(2))
button_3 = Button(root, text='3', command=lambda: button_click(3))
button_add = Button(root, text='+', command=lambda: button_click('+'))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# ------------------------------6-line-----------------------------------------------

button_0 = Button(root, text='0 ', command=lambda: button_click(0))
button_dot = Button(root, text='.', command=lambda: button_click('.'))
button_equal = Button(root, text='=', command=button_equal)

button_0.grid(row=5, column=0, columnspan=2)
button_dot.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()