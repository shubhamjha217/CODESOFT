from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("error")
        expression=""
def clear():
    global expression
    expression=""
    equation.set("")
if __name__=="__main__":
    a = Tk()
    a.configure(background="grey")
    a.title("simple calculator")
    a.geometry("270x150")
    equation=StringVar()
    expression_field=Entry(a, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    btn1=Button(a, text='1', fg='black', bg='white', command=lambda: press (1), height=1, width=7)
    btn1.grid(row=2, column=0)
    btn2 = Button(a, text='2', fg="black", bg="white", command=lambda: press(2), height=1, width=7)
    btn2.grid(row=2, column=1)
    btn3 = Button(a, text='3', fg="black", bg="white", command=lambda: press(3), height=1, width=7)
    btn3.grid(row=2,column=2)
    btn4=Button(a, text='4', fg="black", bg="white", command=lambda: press(4), height=1, width=7)
    btn4.grid(row=3, column=0)
    btn5=Button(a, text='5', fg="black", bg="white", command=lambda: press(5), height=1, width=7)
    btn5.grid(row=3, column=1)
    btn6=Button(a, text='6', fg="black", bg="white", command=lambda: press(6), height=1, width=7)
    btn6.grid(row=3, column=2)
    btn7=Button(a, text='7', fg='black', bg='white',command=lambda: press(7), height=1, width=7)
    btn7.grid(row=4, column=0)
    btn8=Button(a, text='8', fg='black', bg='white',command=lambda: press(8), height=1, width=7)
    btn8.grid(row=4, column=1)
    btn9=Button(a, text='9', fg='black', bg='white', command=lambda: press (9), height=1, width=7)
    btn9.grid(row=4, column=2)
    btn0=Button(a, text='0', fg="black", bg="white", command=lambda: press (0), height=1, width=7)
    btn0.grid(row=5, column=0)
    plus=Button(a, text='+', fg='black', bg='white',command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus=Button(a, text='-', fg='black',bg="lightgrey", command=lambda: press ("-"), height=1, width=7)
    minus.grid(row=3, column=3)
    multiply=Button(a, text='*', fg="black", bg="lightgrey",command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
    divide=Button(a, text='/',fg="black", bg="lightgrey",command=lambda: press("/"), height=1, width=7)
    divide.grid(rows=5, column=3)
    equal=Button(a, text='=', fg="black", bg="lightgrey", command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
    clear=Button(a, text="clean", fg='black', bg="Lightgrey",command=clear, height=1, width=7)
    clear.grid(row=5, column=1)
    a.mainloop()
