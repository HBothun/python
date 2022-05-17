from tkinter import *
from math import *
import ast as ast
from tkinter.font import BOLD, ITALIC

calc= Tk()
calc.title('Calculate')
calc.configure(background='purple2')

expression = ''
equation = StringVar()

expression_field = Entry(calc,
    textvariable=equation,
    bg='palevioletred1',
    fg='red4',
    relief=SUNKEN,
    borderwidth=10,
    justify='center'
    )


def neg():
    global expression
    total = str(int(expression) * -1)
    equation.set(total)
    expression = total
def sqa():
    try:
        global expression
        total = str(sqrt(int(expression)))
        equation.set(total)
        expression = ''
    except:
        equation.set(' Error ')
        expression = ''
def clear():
    global expression
    expression = ''
    equation.set('')
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set(' Error ')
        expression = ''


ptn = Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white',
    command = neg,
    text='-/+',
    height=0, width=5
)
pw = Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white',
    command =lambda: press('**'),
    text='^',
    height=0, width=5
)
sqar = Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white',
    command = sqa,
    text='Sqrt',
    height=0, width=5
)
clr = Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white',
    command = clear,
    text='C',
    height=0, width=3
)
num0=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4',
    command=lambda: press(0), 
    text='0', 
    height=1, width=3
)
num1=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(1), 
    text='1', 
    height=1, width=3
)
num2=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(2), 
    text='2', 
    height=1, width=3
)
num3=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(3), 
    text='3', 
    height=1, width=3
)
num4=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(4), 
    text='4', 
    height=1, width=3
)
num5=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4',
    command=lambda: press(5), 
    text='5', 
    height=1, width=3
)
num6=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(6), 
    text='6', 
    height=1, width=3
)
num7=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(7), 
    text='7', 
    height=1, width=3
)
num8=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(8), 
    text='8', 
    height=1, width=3
)
num9=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='orchid4',
    fg='purple4', 
    command=lambda: press(9), 
    text='9', 
    height=1, width=3
)
add=Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white', 
    command=lambda: press('+'), 
    text='+', 
    height=2, width=3
)
sub=Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white', 
    command=lambda: press('-'), 
    text=' - ', 
    height=2, width=3
    )
mult=Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white', 
    command=lambda: press('*'), 
    text=' * ', 
    height=2, width=3
    )
div=Button(calc,
    relief=RAISED,
    borderwidth=5,
    bg='deeppink2',
    fg='white', 
    command=lambda: press('/'), 
    text=' / ', 
    height=2, width=3
    )
elq=Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='deeppink2',
    fg='white', 
    command=equalpress, 
    text='=', 
    height=1, width=3
    )
dec = Button(calc,
    relief=RAISED,
    borderwidth=5,
    font=BOLD,
    bg='deeppink2',
    fg='white',
    command =lambda: press('.'),
    text = '.',
    height=1, width=3 
)


expression_field.grid(row=0, columnspan=4)

clr.grid(row=1, column=3)
sqar.grid(row=1, column=2)
pw.grid(row=1, column=1)
ptn.grid(row=1, column=0)

num7.grid(row=2, column=0)
num8.grid(row=2, column=1)
num9.grid(row=2, column=2)
num4.grid(row=3, column=0)
num5.grid(row=3, column=1)
num6.grid(row=3, column=2)
num1.grid(row=4, column=0)
num2.grid(row=4, column=1)
num3.grid(row=4, column=2)
num0.grid(row=5, column=1)

add.grid(row=5, column=3)
sub.grid(row=4, column=3)
mult.grid(row=3, column=3)
div.grid(row=2, column=3)

dec.grid(row=5, column=0)
elq.grid(row=5, column=2)


calc.mainloop()