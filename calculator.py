from tkinter import *
import math

# Create main window
root = Tk()

# Set application name
root.title('Calculator')
# Set window size
root.geometry('215x250+150+150')
# Set window transparency
root.attributes("-alpha", 0.9)
# Set the main window background color
root["background"] = "#ffffff"

# Sets a StringVar variable
result_num = StringVar()
# Initialize a character whose result_num is empty
result_num.set('')

# Set a Label to display the value of result_num, and set the size of the Label
Label(root,
      textvariable=result_num, height=2, width=29, justify=LEFT, anchor=SE
      ).grid(row=1,column=1, columnspan=4)

# Set the first row button
button_reset=Button(root, text='C', width=5, relief=FLAT, background="#b1b2b2")
button_back=Button(root, text='←', width=5, relief=FLAT, background="#b1b2b2")
button_division=Button(root, text='÷', width=5, relief=FLAT, background="#b1b2b2")
button_multiplication=Button(root, text='x', width=5, relief=FLAT, background="#b1b2b2")
button_reset.grid(row=2, column=1, padx=4, pady=2)
button_back.grid(row=2, column=2, padx=4, pady=2)
button_division.grid(row=2, column=3, padx=4, pady=2)
button_multiplication.grid(row=2, column=4, padx=4, pady=2)

# Set the second row button
button_7=Button(root, text='7', width=5, relief=FLAT, background="#eacda1")
button_8=Button(root, text='8', width=5, relief=FLAT, background="#eacda1")
button_9=Button(root, text='9', width=5, relief=FLAT, background="#eacda1")
button_subtraction=Button(root, text='-', width=5, relief=FLAT, background="#b1b2b2")
button_7.grid(row=3, column=1, padx=4, pady=2)
button_8.grid(row=3, column=2, padx=4, pady=2)
button_9.grid(row=3, column=3, padx=4, pady=2)
button_subtraction.grid(row=3, column=4, padx=4, pady=2)

#Set the third row button
button_4=Button(root, text='4', width=5, relief=FLAT, background="#eacda1")
button_5=Button(root, text='5', width=5, relief=FLAT, background="#eacda1")
button_6=Button(root, text='6', width=5, relief=FLAT, background="#eacda1")
button_pluss=Button(root, text='+', width=5, relief=FLAT, background="#b1b2b2")
button_4.grid(row=4, column=1, padx=4, pady=2)
button_5.grid(row=4, column=2, padx=4, pady=2)
button_6.grid(row=4, column=3, padx=4, pady=2)
button_pluss.grid(row=4, column=4, padx=4, pady=2)

# Set the fourth row button
button_1=Button(root, text='1', width=5, relief=FLAT, background="#eacda1")
button_2=Button(root, text='2', width=5, relief=FLAT, background="#eacda1")
button_3=Button(root, text='3', width=5, relief=FLAT, background="#eacda1")
button_equal=Button(root, text='=', width=5, height=3, relief=FLAT, background="#b1b2b2")
button_1.grid(row=5, column=1, padx=4, pady=2)
button_2.grid(row=5, column=2, padx=4, pady=2)
button_3.grid(row=5, column=3, padx=4, pady=2)
button_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

#Set the fifth row button
button_0=Button(root, text='0', width=13, relief=FLAT, background="#eacda1")
button_dot=Button(root, text='.', width=5, relief=FLAT, background="#eacda1")
button_0.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
button_dot.grid(row=6, column=3, padx=4, pady=2)

# Set the sixth row button
button_exp=Button(root, text='^', width=5, relief=FLAT, background="#b1b2b2")
button_cos=Button(root, text='cos', width=5, relief=FLAT, background="#b1b2b2")
button_sin=Button(root, text='sin', width=5, relief=FLAT, background="#b1b2b2")
button_tan=Button(root, text='tan', width=5, relief=FLAT, background="#b1b2b2")
button_exp.grid(row=7, column=1, padx=4, pady=2)
button_cos.grid(row=7, column=2, padx=4, pady=2)
button_sin.grid(row=7, column=3, padx=4, pady=2)
button_tan.grid(row=7, column=4, padx=4, pady=2)

def click(x):
    result_num.set(result_num.get() + x)

def calculation():
    try:
        # read record
        opt_str = result_num.get()
        # calculation
        result = eval(opt_str)
        # display the output
        result_num.set(str(result))
    except:
        # display "error"
        result_num.set("error")

def reset():
    result_num.set('')

def back():
    temp_equ = result_num.get()
    result_num.set(temp_equ[:-1])

def cosine():
    try:
        opt_str = result_num.get()
        result = eval(opt_str)
        result_num.set(math.cos(result))
    except:
        result_num.set("error")

def sine():
    try:
        opt_str = result_num.get()
        result = eval(opt_str)
        result_num.set(math.sin(result))
    except:
        result_num.set("error")

def tangent():
    try:
        opt_str = result_num.get()
        result = eval(opt_str)
        result_num.set(math.tan(result))
    except:
        result_num.set("error")

button_1.config(command=lambda: click('1'))
button_2.config(command=lambda: click('2'))
button_3.config(command=lambda: click('3'))
button_4.config(command=lambda: click('4'))
button_5.config(command=lambda: click('5'))
button_6.config(command=lambda: click('6'))
button_7.config(command=lambda: click('7'))
button_8.config(command=lambda: click('8'))
button_9.config(command=lambda: click('9'))
button_0.config(command=lambda: click('0'))
button_pluss.config(command=lambda: click('+'))
button_subtraction.config(command=lambda: click('-'))
button_multiplication.config(command=lambda: click('*'))
button_division.config(command=lambda: click('/'))
button_dot.config(command=lambda: click('.'))
button_equal.config(command=calculation)
button_reset.config(command=reset)
button_back.config(command=back)
button_exp.config(command=lambda: click('**'))
button_cos.config(command=cosine)
button_sin.config(command=sine)
button_tan.config(command=tangent)

root.mainloop()  
