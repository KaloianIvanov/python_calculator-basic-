#Basic Tkinter setup
from tkinter import *
import tkinter as tk
import math

root = Tk()
root.title("kaloian's calculator")



#variables and entry/text boxes
entry = Entry(root,width=10,font=('', 30))
entry.grid(row=0,column=0,columnspan=4)
global operation
global first 
global second
operation = 1


#Functions
def add(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear():
    global operation
    global first 
    global second

    operation = 1
    entry.delete(0, END)

def minus():
    global operation
    global first 
    global second

    if operation == "+":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
        operation = "-"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "-":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
        operation = "-"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "*":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
        operation = "-"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "/":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
        operation = "-"
        first = entry.get()
        entry.delete(0, END)
    else:
        operation = "-"
        first = entry.get()

    entry.delete(0, END)\
     
def plus():
    global operation
    global first 
    global second
    

    if operation == "+":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
        operation = "+"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "-":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
        operation = "+"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "*":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
        operation = "+"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "/":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
        operation = "+"
        first = entry.get()
        entry.delete(0, END)
    else:
        operation = "+"
        first = entry.get()
        entry.delete(0, END)

def multiply():

    global operation
    global first 
    global second
    

    if operation == "+":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
        operation = "*"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "-":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
        operation = "*"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "*":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
        operation = "*"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "/":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
        operation = "*"
        first = entry.get()
        entry.delete(0, END)
    else:
        operation = "*"
        first = entry.get()
        entry.delete(0, END)

def divide():
    global operation
    global first 
    global second

    if operation == "+":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
        operation = "/"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "-":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
        operation = "/"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "*":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
        operation = "/"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "/":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
        operation = "/"
        first = entry.get()
        entry.delete(0, END)
    else:
        operation = "/"
        first = entry.get()

    entry.delete(0, END)\

def enter():
    global operation
    global first 
    global second
    if operation == "+":
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
    elif operation == "-":
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
    elif operation == "*":
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
    elif operation == "/":
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
    elif operation == "**":
        entry.delete(0, END)
        result = int(first) * int(first)
        entry.insert(0, int(result))
    elif operation == "√":
        entry.delete(0, END)
        result = math.sqrt(int(first))
        entry.insert(0, int(result))

def squared():
    global operation
    global first 
    global second
    

    if operation == "+":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
        operation = "**"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "-":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
        operation = "**"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "*":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
        operation = "**"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "/":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
        operation = "**"
        first = entry.get()
        entry.delete(0, END)
    else:
        operation = "**"
        first = entry.get()
        entry.delete(0, END)

def rt_squared():
    global operation
    global first 
    global second
    

    if operation == "+":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) + int(second)
        entry.insert(0, int(result))
        operation = "√"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "-":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) - int(second)
        entry.insert(0, int(result))
        operation = "√"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "*":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) * int(second)
        entry.insert(0, int(result))
        operation = "√"
        first = entry.get()
        entry.delete(0, END)
    elif operation == "/":
        second = entry.get()
        entry.delete(0, END)
        result = int(first) / int(second)
        entry.insert(0, int(result))
        operation = "√"
        first = entry.get()
        entry.delete(0, END)
    else:
        operation = "√"
        first = entry.get()
        entry.delete(0, END)

#Creation and size of buttons
btn1 = tk.Button(root,text="1",padx=24,pady=20,command = lambda:add(1))
btn2 = tk.Button(root,text="2",padx=24,pady=20,command = lambda:add(2))
btn3 = tk.Button(root,text="3",padx=24,pady=20,command = lambda:add(3))
btn4 = tk.Button(root,text="4",padx=24,pady=20,command = lambda:add(4))
btn5 = tk.Button(root,text="5",padx=24,pady=20,command = lambda:add(5))
btn6 = tk.Button(root,text="6",padx=24,pady=20,command = lambda:add(6))
btn7 = tk.Button(root,text="7",padx=24,pady=20,command = lambda:add(7))
btn8 = tk.Button(root,text="8",padx=24,pady=20,command = lambda:add(8))
btn9 = tk.Button(root,text="9",padx=24,pady=20,command = lambda:add(9))
btn0 = tk.Button(root,text="0",padx=24,pady=20,command = lambda:add(0))

btnplus = tk.Button(root,text="+",padx=22,pady=19,font=('', 10),command = plus)
btnminus = tk.Button(root,text="-",padx=24,pady=19,font=('', 10),command = minus)
btndivide = tk.Button(root,text="/",padx=24,pady=19,font=('', 10),command = divide)
btnmultiply = tk.Button(root,text="*",padx=22,pady=18,font=('', 11),command = multiply)
btnsquared = tk.Button(root,text="^",padx=23,pady=18,font=('', 11),command = squared)
btnrt_squared = tk.Button(root,text="√",padx=21,pady=18,font=('', 11),command = rt_squared)
btnenter = tk.Button(root,text="ENTER",padx=41,pady=20,command = enter)
btnclr = tk.Button(root,text="CLEAR",padx=41,pady=20,command = clear)


#Positions of buttons
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn0.grid(row=4,column=0,)

btnclr.grid(row=5,column=0,columnspan=2)
btnplus.grid(row=1,column=3)
btnminus.grid(row=2,column=3)
btndivide.grid(row=3,column=3)
btnmultiply.grid(row=4,column=3)
btnsquared.grid(row=4,column=2)
btnrt_squared.grid(row=4,column=1)
btnenter.grid(row=5,column=2,columnspan=2)



#Tkinter refresh loop
root.mainloop()
