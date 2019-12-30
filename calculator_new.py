from tkinter import *
from tkinter import ttk


def btn_click(numbers):
    global expression
    expression = expression + str(numbers)
    text_input.set(expression)


def btn_clear():
    global expression
    text_input.set('')
    expression = ''


def evaluate_expression():
    global expression
    text_input.set(eval(expression))
    expression = ''


calc = Tk()
calc.title('Calculator')
expression = ''
text_input = StringVar()
text_display = ttk.Entry(calc, font=('Arial', 20, 'bold'), textvariable=text_input, justify='right').grid(columnspan=4)

btn7 = ttk.Button(calc, text='7', command=(lambda: btn_click(7))).grid(row=1, column=0)
btn8 = ttk.Button(calc, text='8', command=(lambda: btn_click(8))).grid(row=1, column=1)
btn9 = ttk.Button(calc, text='9', command=(lambda: btn_click(9))).grid(row=1, column=2)
btn_divide = ttk.Button(calc, text='/', command=(lambda: btn_click('/'))).grid(row=1, column=3)

btn4 = ttk.Button(calc, text='4', command=(lambda: btn_click(4))).grid(row=2, column=0)
btn5 = ttk.Button(calc, text='5', command=(lambda: btn_click(5))).grid(row=2, column=1)
btn6 = ttk.Button(calc, text='6', command=(lambda: btn_click(6))).grid(row=2, column=2)
btn_multiply = ttk.Button(calc, text='x', command=(lambda: btn_click('*'))).grid(row=2, column=3)

btn1 = ttk.Button(calc, text='1', command=(lambda: btn_click(1))).grid(row=3, column=0)
btn2 = ttk.Button(calc, text='2', command=(lambda: btn_click(2))).grid(row=3, column=1)
btn3 = ttk.Button(calc, text='3', command=(lambda: btn_click(3))).grid(row=3, column=2)
btn_subtract = ttk.Button(calc, text='-', command=(lambda: btn_click('-'))).grid(row=3, column=3)

btn0 = ttk.Button(calc, text='0', command=(lambda: btn_click(0))).grid(row=4, column=0)
btn_clear = ttk.Button(calc, text='C', command=btn_clear).grid(row=4, column=1)
btn_equal = ttk.Button(calc, text='=', command=evaluate_expression).grid(row=4, column=2)
btn_plus = ttk.Button(calc, text='+', command=(lambda: btn_click('+'))).grid(row=4, column=3)

calc.mainloop()
