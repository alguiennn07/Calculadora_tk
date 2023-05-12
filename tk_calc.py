import tkinter as tk

i = 0
ventana = tk.Tk()
ventana.geometry('476x448+420+90')
ventana.resizable(False,False)#EJE X, EJE Y
ventana.iconbitmap(r"C:\Users\moham\OneDrive\Bureau\PYTHON\proyectos\favicon_calc.ico")
caja = tk.Entry(ventana, width=28, font='calibri 25')
caja.grid(row=0, column=0, columnspan=999, padx=0, pady=15)
ventana.title('Calculadora')
def copiar():
    
    ventana.clipboard_append(caja.get())
def insertar_op(valor):
    global i
    caja.insert(i, valor)
    i += 1

def delete():
    caja.delete(0, tk.END)
    i = 0

def calc():
    operacion = caja.get()
    try:
        resultado = eval(operacion)
        delete()
        caja.insert(0, resultado)
        i = 0
    except:
        delete()
        caja.insert(0, 'Syntax error')
    

boton_igual = tk.Button(ventana, text='=', command=calc, width=12, height=5)
boton_igual.grid(row=5, column=2)

sum = tk.Button(ventana, text='+', command=lambda: insertar_op('+'), width=12, height=5)
multiply = tk.Button(ventana, text='X', width=12, height=5,command=lambda: insertar_op('*'))
substract = tk.Button(ventana, text='-', width=12, height=5, command=lambda: insertar_op('-'))
divide = tk.Button(ventana, text='/' , width=12, height=5,command=lambda: insertar_op('/'))
parentheses1 = tk.Button(ventana, text='(', width=12, height=5, command=lambda: insertar_op('('))
parentheses2 = tk.Button(ventana, text=')', width=12, height=5, command=lambda: insertar_op(')'))
one = tk.Button(ventana, text=1, width=12, height=5, command=lambda: insertar_op('1'))
two = tk.Button(ventana, text=2, width=12, height=5, command=lambda: insertar_op('2'))
three = tk.Button(ventana, text=3, width=12, height=5, command=lambda: insertar_op('3'))
four = tk.Button(ventana, text=4, width=12, height=5, command=lambda: insertar_op('4'))
five = tk.Button(ventana, text=5, width=12, height=5, command=lambda: insertar_op('5'))
six = tk.Button(ventana, text=6, width=12, height=5, command=lambda: insertar_op('6'))
seven = tk.Button(ventana, text=7, width=12, height=5, command=lambda: insertar_op('7'))
eight = tk.Button(ventana, text=8, width=12, height=5, command=lambda: insertar_op('8'))
nine = tk.Button(ventana, text=9, width=12, height=5, command=lambda: insertar_op('9'))
zero = tk.Button(ventana, text=0, width=26, height=5, command=lambda: insertar_op('0'))
copy=tk.Button(ventana,text='Copy',command=copiar,width=67,padx=0)
copy.grid(row=6,column=0,columnspan=6)
del_num = tk.Button(ventana, text='AC', width=26, height=5, command=delete)
del_num.grid(row=2, column=3,columnspan=2,padx=0)                   #  

one.grid(row=4 ,column=0)
two.grid(row= 4,column=1)
three.grid(row= 4,column= 2)

four.grid(row=3, column=0)
five.grid(row=3, column=1)
six.grid(row=3, column=2)

seven.grid(row=2, column=0)
eight.grid(row=2, column=1)
nine.grid(row=2, column=2)
zero.grid(row=5 ,column= 0,columnspan=2)

sum.grid(row=4, column=3)
multiply.grid(row=3, column=3)
substract.grid(row=4, column=4)
divide.grid(row=3, column=4)
parentheses1.grid(row=5, column=3)
parentheses2.grid(row=5, column=4)
ventana.mainloop()
