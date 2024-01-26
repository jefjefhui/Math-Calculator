# A6,Chi Heng Jeffrey Hui,CIS 345, T TH 12:00 PM
from tkinter import *
from tkinter.ttk import *
import math

thestring = ''
neg=True

def string_creation(numbers):
    """The create the string base on different situation"""
    global thestring,textinbox

    #if sqrt evaluate using math.sqrt else




    if numbers=='sq':
     thestring = str(math.sqrt(eval(thestring)))
     textinbox.set(thestring)
    # elif numbers=='=':
    #     textinbox.set(eval(thestring))
  #  if numbers=='dot':
   #     thestring=thestring+
    elif numbers=='bs':
        thestring=thestring[:-1]
        textinbox.set(thestring)
    elif numbers=='.':
        if thestring[-1]=='.':
            pass
        else:
            thestring = thestring + '.'
            textinbox.set(thestring)
    elif numbers=='pm':
        global neg
        if neg:
         #append - make neg false
         thestring='-'+thestring
         #textinbox.set(thestring)
         neg=False



        else:
         #slice/remove - and makeneg true
         thestring=thestring[1:]
         #textinbox.set(thestring)
         neg=True







    else:
      thestring = thestring + str(numbers)
    textinbox.set(thestring)


def doingthecalculations():
    """This function handle exception and equal button"""
    global thestring
    try:
        thestring=str(eval(thestring))
        textinbox.set(thestring)
    except:
        a=("Doesn't crash/ Error")
        textinbox.set(a)
        thestring=''






def reset():
    """The function handle the all cancel button """
    global thestring,textinbox
    thestring=''
    textinbox.set('')













#window stuff
window = Tk()
textinbox = StringVar()
window.title('Calculator')
window.geometry("320x150")
window.configure(background='light blue')

# The display window
display=Entry(window,width=50,textvariable=textinbox,text=textinbox,state=DISABLED)
display.grid(row=0,columnspan=4,)
# Clear button
clear = Button(window,text='C',command=reset)
clear.grid(row=1, column=0)

# backspace button
arrow=Button(window,text='→',command=lambda:string_creation('bs'))
arrow.grid(row=1,column=1)

# plus minus button
plusminus = Button(window,text='+/-',command=lambda :string_creation('pm'))
plusminus.grid(row=1, column=2)

# Square root button
squareroot = Button(window,text='√',command=lambda :string_creation('sq'))
squareroot.grid(row=1, column=3)

# seven
seven = Button(window,text='7',command= lambda:string_creation(7))
seven.grid(row=2,column=0)

# eight
eight = Button(window,text='8',command= lambda:string_creation(8))
eight.grid(row=2,column=1)

# nine
nine = Button(window,text='9',command=lambda:string_creation(9))
nine.grid(row=2, column=2)

# Division button
division = Button(window,text='÷',command=lambda:string_creation('/'))
division.grid(row=2, column=3)

# four
four = Button(window,text='4',command=lambda:string_creation(4))
four.grid(row=3, column=0)

# five
five = Button(window,text='5',command=lambda:string_creation(5))
five.grid(row=3, column=1)

# Six
Six = Button(window,text='6',command=lambda:string_creation(6))
Six.grid(row=3,column=2)

# Multiplication button
multiplication=Button(window,text='X',command=lambda:string_creation('*'))
multiplication.grid(row=3, column=3)

# one
one=Button(window,text='1',command=lambda:string_creation(1))
one.grid(row=4, column=0)

# two
two=Button(window,text='2',command=lambda:string_creation(2))
two.grid(row=4, column=1)

# three
three=Button(window,text='3',command=lambda:string_creation(3))
three.grid(row=4, column=2)

# subtraction button
subtraction=Button(window,text='-',command=lambda:string_creation('-'))
subtraction.grid(row=4, column=3)

#zero
zero=Button(window,text='0',command=lambda:string_creation(0))
zero.grid(row=5, column=0)

#dot
dot=Button(window,text='.',command=lambda:string_creation('.'))
dot.grid(row=5,column=1)

#equal
equal=Button(window,text='=',command=doingthecalculations)
equal.grid(row=5,column=2)

# Addition button
addition=Button(window,text='+',command=lambda :string_creation('+'))
addition.grid(row=5, column=3)


window.mainloop()
